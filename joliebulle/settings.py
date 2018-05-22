#!/usr/bin/python3
#­*­coding: utf­8 -­*­



import os
from sys import platform
import codecs
import PyQt5
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class Settings:
    def __init__ (self) :
        self.conf = QtCore.QSettings("joliebulle", "joliebulle")
        #self.conf.setValue("pathUnix", os.path.join(os.path.expanduser("~"), ".config", "joliebulle", "recettes")) 
        #self.conf.setValue("pathWin32", os.path.join(os.path.expanduser("~"), "AppData", "Local", "joliebulle", "recettes"))
