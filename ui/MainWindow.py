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
