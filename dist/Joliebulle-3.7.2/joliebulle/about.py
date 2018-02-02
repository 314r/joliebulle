import PyQt5
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from about_ui import *

class DialogAbout(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.ui = Ui_DialogAbout()
        self.ui.setupUi(self)
