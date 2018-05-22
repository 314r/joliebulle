#!/usr/bin/python3
#­*­coding: utf­8 -­*­



import codecs
import PyQt5
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from stepEditor_ui import *
from model.mashstep import *

class DialogStep(QtWidgets.QDialog):
    stepChanged = QtCore.pyqtSignal(MashStep)
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.comboBoxStepType.addItems(["Infusion", "Température", "Décoction"])

        self.ui.lineEditStepName.textChanged.connect(self.valueChanged)
        self.ui.comboBoxStepType.currentIndexChanged.connect(self.valueChanged)
        self.ui.doubleSpinBoxStepTime.valueChanged.connect(self.valueChanged)
        self.ui.doubleSpinBoxStepTemp.valueChanged.connect(self.valueChanged)
#        self.ui.doubleSpinBoxStepVol.valueChanged.connect(self.valueChanged)

        self.ui.buttonBox.accepted.connect(self.accepted)



    def fields (self, step) :
        self.ui.lineEditStepName.setText(step.name)
        if step.type == self.tr('''Infusion''') :
            self.ui.comboBoxStepType.setCurrentIndex(0)
        elif step.type== self.tr('''Temperature''') :
            self.ui.comboBoxStepType.setCurrentIndex(1)
        elif step.type == self.tr('''Decoction''') :
            self.ui.comboBoxStepType.setCurrentIndex(2)
        self.ui.doubleSpinBoxStepTime.setValue(float(step.time))
        self.ui.doubleSpinBoxStepTemp.setValue(float(step.temp))
#        self.ui.doubleSpinBoxStepVol.setValue(float(stepVol))



    def valueChanged (self) :
        self.step = MashStep()
        self.step.name = self.ui.lineEditStepName.text()
        if self.ui.comboBoxStepType.currentIndex() is 0 :
            self.step.type = self.tr('''Infusion''')
        elif self.ui.comboBoxStepType.currentIndex() is 1 :
            self.step.type = self.tr('''Temperature''')
        elif self.ui.comboBoxStepType.currentIndex() is 2 :
            self.step.type = self.tr('''Decoction''')
        self.step.time = self.ui.doubleSpinBoxStepTime.value()
        self.step.temp = self.ui.doubleSpinBoxStepTemp.value()
        self.stepVol = 0

    def accepted(self) :
        self.stepChanged.emit(self.step)
