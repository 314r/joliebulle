#!/usr/bin/python3
#­*­coding: utf­8 -­*­



#JolieBulle 2.5
#Copyright (C) 2010-2011 Pierre Tavares

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
from base import *
from globals import *
from stepAdjust_ui import *
from brewCalc import *

class DialogStepAdjust(QtGui.QDialog):
    
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_DialogStepBrewday()
        self.ui.setupUi(self)
        self.brewCalc = CalcBrewday()
        self.ui.doubleSpinBoxWaterTemp.valueChanged.connect(self.waterTempChanged)
        
        
    def setFields (self, targetTemp, targetRatio, infuseAmount, waterTemp, grainWeight, listVol, currentRow, listTemp) :
        self.ui.labelTargetTemp.setText(str(targetTemp))
        self.ui.doubleSpinBoxTargetRatio.setValue(float(targetRatio))
        self.ui.doubleSpinBoxInfuseAmount.setValue(float(infuseAmount))
        self.ui.doubleSpinBoxWaterTemp.setValue(float(waterTemp))
        self.grainWeight = float(grainWeight)
        self.listVol = listVol
        self.currentRow = currentRow
        self.targetTemp = targetTemp
        self.listTemp = listTemp
        
    def waterTempChanged(self) :
        waterTemp = self.ui.doubleSpinBoxWaterTemp.value()
        i = self.currentRow

        mashTemp = self.listTemp[i-2] 
        
        self.brewCalc.calcInfusionStep(self.currentRow-1, self.grainWeight, self.listVol, self.targetTemp, mashTemp, waterTemp)
        print(self.currentRow, self.grainWeight, self.listVol, self.targetTemp, mashTemp, waterTemp)
        self.infuseVol = self.brewCalc.infuseVol
        self.ui.doubleSpinBoxInfuseAmount.setValue(float(self.infuseVol))
        self.listVol[i] = self.ui.doubleSpinBoxInfuseAmount.value()
        
        ################### A revoir !
        
    def infuseAmountChanged(self) :
        pass



        
        
    def targetRatioChanged(self) : 
        pass
        
    
        
        
