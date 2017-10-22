#!/usr/bin/python3
#­*­coding: utf­8 -­*­




import PyQt5
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from preboil_ui import *



class DialogPreBoil(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.ui = Ui_PreEbullitionDialog()
        self.ui.setupUi(self)

    def setData (self, preBoilVol, preBoilGravity, recipeGu, recipeVolume) :
    	self.ui.doubleSpinBoxVolume.setValue(preBoilVol)
    	self.ui.labelGravity.setText("%.3f" %(preBoilGravity))
    	self.recipeGu = recipeGu
    	self.recipeVolume = recipeVolume
    	################################
        #Connexion
        ################################
    	self.ui.doubleSpinBoxVolume.valueChanged.connect(self.theoricGravity)

    def theoricGravity (self) :
	    indice = float(self.recipeVolume)/self.ui.doubleSpinBoxVolume.value()
	    GUS = self.recipeGu * indice
	    SG = 1+(GUS/1000)
	    self.ui.labelGravity.setText("%.3f" %SG)
