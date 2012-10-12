__author__ = 'nico'

import logging
from ui.NavTreeViewModel import NavTreeViewModel
from PyQt4 import QtGui, QtCore
from plugins.ExtensionPoints import NavTreeViewExtensionPoint
from ui.MainWindowUI import Ui_MainWindow


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.logger = logging.getLogger(__name__)
        
        self.navTreeView.setModel(NavTreeViewModel())
        
        #self.initModel()

    def initModel(self):
        from ui import NavTreeViewDefaultsExtension
        model = QtGui.QStandardItemModel()
        self.navTreeView.setModel(model)
        
        rootItem = model.invisibleRootItem()
        for cat in self.getDistinctCategories():
            category = QtGui.QStandardItem(cat['label'])
            rootItem.appendRow(category)

        
    def getDistinctCategories(self):
        categories=[]
        for p in NavTreeViewExtensionPoint.plugins: #For each plugin
            for cat in p().getCategories():             #For each category declared by plugin
                if not self.findCateogryInList(categories, cat['id']):      #If category doesn't already exists
                    categories.append(cat)  #Add it
        self.logger.debug("%s distinct categories: %s", len(categories), categories)
        return categories
        
    def findCateogryInList(self, list, catId):
        for cat in list:
            if cat['id'] == catId:
                return cat
        return None

        