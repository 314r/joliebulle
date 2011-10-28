import os
from sys import platform
import codecs
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Settings:
    def __init__ (self) :
        
        self.conf = QtCore.QSettings("joliebulle", "joliebulle")
        #self.conf.setValue("pathUnix", os.path.join(os.path.expanduser("~"), ".config", "joliebulle", "recettes")) 
        #self.conf.setValue("pathWin32", os.path.join(os.path.expanduser("~"), "AppData", "Local", "joliebulle", "recettes"))
