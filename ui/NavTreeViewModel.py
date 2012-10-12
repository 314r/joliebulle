import logging
from PyQt4 import QtCore
from plugins.ExtensionPoints import NavTreeViewExtensionPoint
from uuid import getnode

class TreeNode:
    def __init__(self, id, label, parent=None, row=None):
        self.id = id
        self.label = label
        self.parent = parent
        self.row = row
        self.children = []

    def __str__(self):
        return "TreeNode:category=" + self.id

class NavTreeViewModel(QtCore.QAbstractItemModel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = logging.getLogger(__name__)

        from ui import NavTreeViewDefaultsExtension
        self.initModel()
        self.logger.debug("%s root nodes registered: %s", len(self._nodes), self._nodes)

    def getNodeById(self, nodeId):
        for node in self._nodes:
            if node.id == nodeId:
                return node
        return None

    def nodeExists(self, nodeId):
        if getnode(nodeId) is not None:
            return True
        return False


    def initModel(self):
        self._nodes = []
        for p in NavTreeViewExtensionPoint.plugins: #For each plugin
            for item in p().getItems(None):             #For each root item declared by plugin
                if not self.nodeExists(item['id']):      #If item doesn't already exists
                    newCat = TreeNode(item['id'], item['label'])  #Add it
                    self._nodes.append(newCat)


    def getItemsFromExtensions(self, parent):
        nbContributor = 0
        items = []
        for p in NavTreeViewExtensionPoint.plugins:
            nbContributor +=1 
            itemsList = p().getItems(parent.id)
            items.extend([TreeItem(x['id'], x['label'], parent) for x in itemsList])
            self.logger.debug("%s retreived from %s contributor(s)", len(items), nbContributor)
        return items

    def columnCount(self, parent=None):
        return 1

    def index(self, row, column, parent):
        self.logger.debug("index(row=%s,column=%s,parent=%s", row, column, parent)
        if not parent.isValid():
            node = self._nodes[row]
            index = self.createIndex(row, column, node)
            return index
        parentItem = parent.internalPointer()
        return self.createIndex(row, column, self.getItemsFromExtensions(parentItem)[row])

    def rowCount(self, parent):
        self.logger.debug("rowCount(parent=%s)", parent)
        if not parent.isValid():
            return len(self._categories)
        else:
            parentItem = parent.internalPointer()
            return len(self.getItemsFromExtensions(parentItem))

    def data(self, index, role):
        self.logger.debug("data(index=%s,role=%s)", index, role)
        if not index.isValid():
            return None
        if role == QtCore.Qt.DisplayRole and index.column() == 0:
            item = index.internalPointer()
            return item.label
