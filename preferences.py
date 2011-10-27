import codecs
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from base import *
from globals import *
from preferences_ui import *
import xml.etree.ElementTree as ET
from xml.dom import minidom



class DialogPref(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Preferences()
        self.ui.setupUi(self)
        
