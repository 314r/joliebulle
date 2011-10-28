import codecs
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from base import *
from globals import *
from preferences_ui import *
from settings import * 
from globals import *
import xml.etree.ElementTree as ET
from xml.dom import minidom



class DialogPref(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        settings = Settings()
        self.ui = Ui_Preferences()
        self.ui.setupUi(self)
        self.ui.lineEditPathLib.setText(recettes_dir)
        
        self.ui.pushButtonChangeLib.clicked.connect(self.changePushed)
        self.ui.buttonBox.accepted.connect(self.accepted)
        
    def changePushed (self) :
        self.d = QtGui.QFileDialog.getExistingDirectory(self,
            self.trUtf8("Choisir un dossier"),
            home_dir,
            )
        self.ui.lineEditPathLib.setText(self.d)
        
    def accepted(self) :    
        print("okidoki")
        if platform == 'win32' :
            pass
        else :
            settings.conf.setValue("pathUnix", self.ui.lineEditPathLib.text())
            print (settings.conf.value("pathUnix"))
