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
        self.navTreeView.clicked.connect(self.item_clicked)
        
        self.current_view = None
        
        #self.initModel()
    def item_clicked(self, index):
        if index.isValid:
            item = index.internalPointer()
            self.logger.debug("Item id=%s clicked", item.id)

            view = item.provider.get_view(self, item)
            if view is not None:
                if self.current_view is not None:
                    self.mainWidget.layout().removeWidget(self.current_view)
                self.mainWidget.layout().addWidget(view)
                self.current_view = view
        
    def initExtensions(self):
        self._root = TreeNode(None, 'Root', None, 0)
        self.get_items_from_extensions(self._root)

    def get_items_from_extensions(self, parent):
        from ui import NavTreeViewDefaultsExtension
        for p in NavTreeViewExtensionPoint.plugins:
            for item in p().get_items(parent.id):             #For each root item declared by plugin
                if not self.nodeExists(parent.children, item['id']):      #If item doesn't already exists
                    newItem = TreeNode(item['id'], item['label'], parent)  #Add it
                    newItem.row = len(parent.children)
                    newItem.provider=p()
                    self.get_items_from_extensions(newItem)    #recursive call
                    parent.children.append(newItem)

    def get_node_by_id(self, nodeList, nodeId):
        for node in nodeList:
            if node.id == nodeId:
                return node
        return None

    def nodeExists(self, nodeList, nodeId):
        if self.get_node_by_id(nodeList, nodeId) is not None:
            return True
        return False


