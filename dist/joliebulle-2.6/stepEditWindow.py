#!/usr/bin/python3
#­*­coding: utf­8 -­*­


import codecs
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from stepEditor_ui import *

class DialogStep(QtGui.QDialog):
    stepChanged = QtCore.pyqtSignal(str,str,float,float,float)
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBoxStepType.addItems(["Infusion", "Température", "Décoction"])
        
        self.ui.lineEditStepName.textChanged.connect(self.valueChanged)
        self.ui.comboBoxStepType.currentIndexChanged.connect(self.valueChanged)
        self.ui.doubleSpinBoxStepTime.valueChanged.connect(self.valueChanged)
        self.ui.doubleSpinBoxStepTemp.valueChanged.connect(self.valueChanged)
#        self.ui.doubleSpinBoxStepVol.valueChanged.connect(self.valueChanged)
        
        self.ui.buttonBox.accepted.connect(self.accepted)
        
        
        
    def fields (self, stepName, stepType, stepTime, stepTemp, stepVol) :
        self.ui.lineEditStepName.setText(stepName)
        if stepType == self.trUtf8('''Infusion''') :
            self.ui.comboBoxStepType.setCurrentIndex(0)
        elif stepType== self.trUtf8('''Temperature''') :
            self.ui.comboBoxStepType.setCurrentIndex(1)
        elif stepType == self.trUtf8('''Decoction''') :
            self.ui.comboBoxStepType.setCurrentIndex(2)              
        self.ui.doubleSpinBoxStepTime.setValue(float(stepTime))
        self.ui.doubleSpinBoxStepTemp.setValue(float(stepTemp))
#        self.ui.doubleSpinBoxStepVol.setValue(float(stepVol))
        
        
        
    def valueChanged (self) :
        self.stepName = self.ui.lineEditStepName.text()
        if self.ui.comboBoxStepType.currentIndex() is 0 :
            self.stepType = self.trUtf8('''Infusion''')  
        elif self.ui.comboBoxStepType.currentIndex() is 1 :
            self.stepType = self.trUtf8('''Temperature''') 
        elif self.ui.comboBoxStepType.currentIndex() is 2 :
            self.stepType = self.trUtf8('''Decoction''') 
        self.stepTime = self.ui.doubleSpinBoxStepTime.value()
        self.stepTemp = self.ui.doubleSpinBoxStepTemp.value()
        self.stepVol = 0
        
    def accepted(self) :
        self.stepChanged.emit(self.stepName,self.stepType,self.stepTime,self.stepTemp,self.stepVol) 
        
