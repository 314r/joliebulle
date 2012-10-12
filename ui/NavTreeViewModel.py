import logging
from PyQt4 import QtCore
from plugins.ExtensionPoints import NavTreeViewExtensionPoint
from uuid import getnode

class TreeNode:
    def __init__(self, id, label, parent=None, row=None):
        self.logger = logging.getLogger(__name__)
        self.id = id
        self.label = label
        self.parent = parent
        self.row = row
        self.children = []
        self.provider = None

    def __str__(self):
        return "TreeNode:id=" + self.id

class NavTreeViewModel(QtCore.QAbstractItemModel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = logging.getLogger(__name__)

        from ui import NavTreeViewDefaultsExtension
        self.initModel()
        self.logger.debug("%s root nodes registered: %s", len(self._root.children), self._root.children)

    def getNodeById(self, nodeList, nodeId):
        for node in nodeList:
            if node.id == nodeId:
                return node
        return None

    def nodeExists(self, nodeList, nodeId):
        if self.getNodeById(nodeList, nodeId) is not None:
            return True
        return False


    def initModel(self):
        self._root = TreeNode(None, 'Root', None, 0)
        i=0
        self.getItemsFromExtensions(self._root)

    def getItemsFromExtensions(self, parent):
        for p in NavTreeViewExtensionPoint.plugins:
            for item in p().getItems(parent.id):             #For each root item declared by plugin
                if not self.nodeExists(parent.children, item['id']):      #If item doesn't already exists
                    newItem = TreeNode(item['id'], item['label'], parent)  #Add it
                    newItem.row = len(parent.children)
                    newItem.provider=p()
                    self.getItemsFromExtensions(newItem)    #recursive call
                    parent.children.append(newItem)

    def columnCount(self, parent=None):
        return 1

    def index(self, row, column, parent):
        self.logger.debug("index(row=%s,column=%s,parent=%s", row, column, parent)
        if not parent.isValid():
            node = self._root.children[row]
            return self.createIndex(row, column, node)
        else:
            parentItem = parent.internalPointer()
            return self.createIndex(row, column, parentItem.children[row])

    def rowCount(self, parent):
        self.logger.debug("rowCount(parent=%s)", parent)
        if not parent.isValid():
            return len(self._root.children)
        else:
            parentItem = parent.internalPointer()
            return len(parentItem.children)

    def data(self, index, role):
        self.logger.debug("data(index=%s,role=%s)", index, role)
        if not index.isValid():
            return None
        if role == QtCore.Qt.DisplayRole and index.column() == 0:
            item = index.internalPointer()
            return item.label
    
    def parent(self, index):
        self.logger.debug("parent(index=%s)", index)
        if not index.isValid():
            return QtCore.QModelIndex()
        node = index.internalPointer()
        if node.parent is None:
            return QtCore.QModelIndex()
        else:
            return self.createIndex(node.parent.row, 0, node.parent)
