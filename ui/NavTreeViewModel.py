import logging
from PyQt4 import QtCore
from plugins.ExtensionPoints import NavTreeViewExtensionPoint

class TreeNode:
    def __init__(self, id, label, parent=None, row=None):
        self.id = id
        self.label = label
        self.parent = parent
        self.row = row

    def __str__(self):
        return "TreeNode:category=" + self.id

class NavTreeViewModel(QtCore.QAbstractItemModel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.logger = logging.getLogger(__name__)

        self._categories = []
        from ui import NavTreeViewDefaultsExtension
        for p in NavTreeViewExtensionPoint.plugins: #For each plugin
            for cat in p().getItems():             #For each category declared by plugin
                if not self.categoryExists(cat['id']):      #If category doesn't already exists
                    newCat = TreeNode(cat['id'], cat['label'])  #Add it
                    self._categories.append(newCat)
        self.logger.debug("%s categories registered: %s", len(self._categories), self._categories)

    def categoryExists(self, catId):
        for cat in self._categories:
            if cat.id == catId:
                return True
        return False

    def getTreeCatoryById(self, id):
        for cat in self._categories:
            if cat.id == id:
                return cat
        return None

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
            return self.createIndex(row, column, list(self._categories)[row])
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
