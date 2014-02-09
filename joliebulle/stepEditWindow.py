#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.2
#Copyright (C) 2010-2014 Pierre Tavares
#Copyright (C) 2012-2014 joliebulle's authors
#See AUTHORS file.

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 3
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

import codecs
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from stepEditor_ui import *
from model.mashstep import *

class DialogStep(QtGui.QDialog):
    stepChanged = QtCore.pyqtSignal(MashStep)
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
        
        
        
    def fields (self, step) :
        self.ui.lineEditStepName.setText(step.name)
        if step.type == self.trUtf8('''Infusion''') :
            self.ui.comboBoxStepType.setCurrentIndex(0)
        elif step.type== self.trUtf8('''Temperature''') :
            self.ui.comboBoxStepType.setCurrentIndex(1)
        elif step.type == self.trUtf8('''Decoction''') :
            self.ui.comboBoxStepType.setCurrentIndex(2)              
        self.ui.doubleSpinBoxStepTime.setValue(float(step.time))
        self.ui.doubleSpinBoxStepTemp.setValue(float(step.temp))
#        self.ui.doubleSpinBoxStepVol.setValue(float(stepVol))
        
        
        
    def valueChanged (self) :
        self.step = MashStep()
        self.step.name = self.ui.lineEditStepName.text()
        if self.ui.comboBoxStepType.currentIndex() is 0 :
            self.step.type = self.trUtf8('''Infusion''')  
        elif self.ui.comboBoxStepType.currentIndex() is 1 :
            self.step.type = self.trUtf8('''Temperature''') 
        elif self.ui.comboBoxStepType.currentIndex() is 2 :
            self.step.type = self.trUtf8('''Decoction''') 
        self.step.time = self.ui.doubleSpinBoxStepTime.value()
        self.step.temp = self.ui.doubleSpinBoxStepTemp.value()
        self.stepVol = 0
        
    def accepted(self) :
        self.stepChanged.emit(self.step) 
        
