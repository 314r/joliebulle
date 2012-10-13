__author__ = 'nico'

import logging
from ui.NavTreeViewModel import *
from PyQt4 import QtGui, QtCore
from ui.MainWindowUI import Ui_MainWindow
from plugins.ExtensionPoints import NavTreeViewExtensionPoint

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.logger = logging.getLogger(__name__)
        
        self._root = None
        self.initExtensions()
        self.navTreeView.setModel(NavTreeViewModel(None, self._root))
        self.navTreeView.clicked.connect(self.test)
        
        #self.initModel()
    def test(self):
        print("CLICKED")
        
    def initExtensions(self):
        self._root = TreeNode(None, 'Root', None, 0)
        self.getItemsFromExtensions(self._root)

    def getItemsFromExtensions(self, parent):
        from ui import NavTreeViewDefaultsExtension
        for p in NavTreeViewExtensionPoint.plugins:
            for item in p().getItems(parent.id):             #For each root item declared by plugin
                if not self.nodeExists(parent.children, item['id']):      #If item doesn't already exists
                    newItem = TreeNode(item['id'], item['label'], parent)  #Add it
                    newItem.row = len(parent.children)
                    newItem.provider=p()
                    self.getItemsFromExtensions(newItem)    #recursive call
                    parent.children.append(newItem)

    def getNodeById(self, nodeList, nodeId):
        for node in nodeList:
            if node.id == nodeId:
                return node
        return None

    def nodeExists(self, nodeList, nodeId):
        if self.getNodeById(nodeList, nodeId) is not None:
            return True
        return False


