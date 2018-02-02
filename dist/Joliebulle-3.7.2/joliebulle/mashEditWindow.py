#!/usr/bin/python3
#­*­coding: utf­8 -­*­



import codecs
import PyQt5
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from mashEditor_ui import *
from model.mash import *

class DialogMash(QtWidgets.QDialog):
    mashChanged = QtCore.pyqtSignal(Mash)
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.ui = Ui_DialogMash()
        self.ui.setupUi(self)
        self.ui.lineEditName.textChanged.connect(self.valueChanged)
        self.ui.doubleSpinBoxPh.valueChanged.connect(self.valueChanged)
#        self.ui.doubleSpinBoxGrainT.valueChanged.connect(self.valueChanged)
#        self.ui.doubleSpinBoxTunT.valueChanged.connect(self.valueChanged)
        self.ui.doubleSpinBoxSpargeT.valueChanged.connect(self.valueChanged)

        self.ui.buttonBox.accepted.connect(self.accepted)

    def fields(self,mash) :
        self.ui.lineEditName.setText(mash.name)
        self.ui.doubleSpinBoxPh.setValue(float(mash.ph))
#        self.ui.doubleSpinBoxGrainT.setValue(float(grainT))
#        self.ui.doubleSpinBoxTunT.setValue(float(tunT))
        self.ui.doubleSpinBoxSpargeT.setValue(float(mash.spargeTemp))

    def valueChanged(self) :
        self.mash = Mash()
        self.mash.name = self.ui.lineEditName.text()
        self.mash.ph = self.ui.doubleSpinBoxPh.value()
        self.mash.grainTemp = 0
        self.mash.tunTemp = 0
        self.mash.spargeTemp =self.ui.doubleSpinBoxSpargeT.value()

    def accepted(self) :
        self.mashChanged.emit(self.mash)
