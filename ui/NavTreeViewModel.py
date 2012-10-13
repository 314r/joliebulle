import logging
from PyQt4 import QtCore

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

    def __init__(self, parent=None, root=None):
        super().__init__(parent)
        self.logger = logging.getLogger(__name__)

        self._root = root
        self.logger.debug("%s root nodes registered: %s", len(self._root.children), self._root.children)

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
