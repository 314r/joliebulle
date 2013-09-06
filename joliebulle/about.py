import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from about_ui import *

class DialogAbout(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_DialogAbout()
        self.ui.setupUi(self)