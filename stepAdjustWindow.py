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
from preferences_ui import *

class DialogStepAdjust(QtGui.QDialog):
    stepAdjustBrewdayClosed = QtCore.pyqtSignal(float, float, float,list, int, list)
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_DialogStepBrewday()
        self.ui.setupUi(self)
        self.brewCalc = CalcBrewday()
        
        self.ui.doubleSpinBoxWaterTemp.valueChanged.connect(self.waterTempChanged)
        self.ui.doubleSpinBoxInfuseAmount.valueChanged.connect(self.infuseAmountChanged)
        self.ui.buttonBox.accepted.connect(self.accepted)
        
        
    def setFields (self, targetTemp, targetRatio, infuseAmount, waterTemp, grainWeight, listVol, currentRow, listTemp, strikeTargetTemp) :
        self.ui.doubleSpinBoxInfuseAmount.blockSignals(True)
        self.ui.doubleSpinBoxWaterTemp.blockSignals(True)
        self.ui.labelTargetTemp.setText(str(targetTemp))
        self.ui.doubleSpinBoxTargetRatio.setValue(float(targetRatio))
        self.ui.doubleSpinBoxInfuseAmount.setValue(float(infuseAmount))
        self.ui.doubleSpinBoxWaterTemp.setValue(float(waterTemp))
        self.grainWeight = float(grainWeight)
        self.listVol = listVol
        self.currentRow = currentRow
        self.targetTemp = targetTemp
        self.listTemp = listTemp
        self.ui.doubleSpinBoxInfuseAmount.blockSignals(False)
        self.ui.doubleSpinBoxWaterTemp.blockSignals(False)
        self.strikeTemp = strikeTargetTemp
        
    def waterTempChanged(self) :
        waterTemp = self.ui.doubleSpinBoxWaterTemp.value()
        i = self.currentRow
        
        if i != 0 :
            if i == 1 :
                mashTemp = self.strikeTemp
            else :
                mashTemp = self.listTemp[i-2] 
            
            self.brewCalc.calcInfusionStep(self.currentRow-1, self.grainWeight, self.listVol, self.targetTemp, mashTemp, waterTemp, 'Infusion')
#            print('ce qui est passé :',self.currentRow, self.grainWeight, self.listVol, self.targetTemp, mashTemp, waterTemp)
#            print('la liste des temperatures :', self.listTemp)
            self.infuseVol = self.brewCalc.infuseVol
            self.ui.doubleSpinBoxInfuseAmount.blockSignals(True)
            self.ui.doubleSpinBoxInfuseAmount.setValue(float(self.infuseVol))
            self.ui.doubleSpinBoxInfuseAmount.blockSignals(False)
            self.listVol[i] = self.ui.doubleSpinBoxInfuseAmount.value()
            
            newRatio = sum(self.listVol[0:i+1])/(self.grainWeight/1000)
            self.ui.doubleSpinBoxTargetRatio.setValue(newRatio)
            
        #le calcul est différent pour le premier palier d'empatage      
        else :
        #ratio = (0.4*(Ttarget-Tgrain)) / (Tstrike-Ttarget-fudgeFactor)
            Ttarget = float(self.targetTemp)
            Tstrike = self.ui.doubleSpinBoxWaterTemp.value()
            Tgrain = int(settings.conf.value("GrainTemp"))
            fudgeFactor = float(settings.conf.value("FudgeFactor"))
            ratio = (0.4*(Ttarget-Tgrain)) / (Tstrike-Ttarget-fudgeFactor)
            self.infuseVol= ratio * (self.grainWeight/1000)

            self.ui.doubleSpinBoxInfuseAmount.blockSignals(True)
            self.ui.doubleSpinBoxInfuseAmount.setValue(float(self.infuseVol))
            self.ui.doubleSpinBoxInfuseAmount.blockSignals(False)
            self.listVol[i] = self.ui.doubleSpinBoxInfuseAmount.value()
            
            newRatio = sum(self.listVol[0:i+1])/(self.grainWeight/1000)
            self.ui.doubleSpinBoxTargetRatio.setValue(newRatio)            
           
            
        
        
        
    def infuseAmountChanged(self) :
        i = self.currentRow
        if i != 0 :
            if i == 1 :
                mashTemp = self.strikeTemp
            else :
                mashTemp = self.listTemp[i-2] 
            #Vm = Wgrain (0.4 + ratio)
            #Tstrike = (Ttarget*(Vstrike+Vm) - (Vm*Tmash)) / Vstrike
            actualVol = sum(self.listVol[0:i])
            ratio = actualVol / (self.grainWeight/1000)
#            print('actualvol :', actualVol)
            Vm = (self.grainWeight/1000)*(0.4+ratio)
            self.waterTemp = ((self.targetTemp*(self.ui.doubleSpinBoxInfuseAmount.value()+Vm)-(Vm*float(mashTemp))) / self.ui.doubleSpinBoxInfuseAmount.value()) + float(settings.conf.value("FudgeFactor"))
            self.ui.doubleSpinBoxWaterTemp.blockSignals(True)
            self.ui.doubleSpinBoxWaterTemp.setValue(self.waterTemp)
            self.ui.doubleSpinBoxWaterTemp.blockSignals(False)
            
            self.listVol[i] = self.ui.doubleSpinBoxInfuseAmount.value()
            newRatio = sum(self.listVol[0:i+1])/(self.grainWeight/1000)
            self.ui.doubleSpinBoxTargetRatio.setValue(newRatio)
            
        #le calcul est différent pour le premier palier d'empatage   
        else :            
            #Tstrike = [Ttarget + (0.4 * (Ttarget - Tgrain) / ratio)] + FF 
            ratio = self.ui.doubleSpinBoxInfuseAmount.value() / (self.grainWeight/1000)
            Ttarget = float(self.targetTemp)
            Tgrain = int(settings.conf.value("GrainTemp"))
            self.waterTemp = (Ttarget + (0.4 * (Ttarget-Tgrain)/ratio)) + float(settings.conf.value("FudgeFactor"))
            self.ui.doubleSpinBoxWaterTemp.blockSignals(True)
            self.ui.doubleSpinBoxWaterTemp.setValue(self.waterTemp)
            self.ui.doubleSpinBoxWaterTemp.blockSignals(False)
            
            self.listVol[i] = self.ui.doubleSpinBoxInfuseAmount.value()
            newRatio = sum(self.listVol[0:i+1])/(self.grainWeight/1000)
            self.ui.doubleSpinBoxTargetRatio.setValue(newRatio)            
            
        
    def accepted(self) :
        targetRatio = self.ui.doubleSpinBoxTargetRatio.value()
        infuseAmount = self.ui.doubleSpinBoxInfuseAmount.value()
        waterTemp = self.ui.doubleSpinBoxWaterTemp.value()
        listVol = self.listVol
        currentRow = self.currentRow
        listTemp = self.listTemp

        self.stepAdjustBrewdayClosed.emit(targetRatio, infuseAmount, waterTemp,listVol, currentRow, listTemp)
        
      
        
        
      
    
        
        
