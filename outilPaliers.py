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


import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from outilPaliers_ui import *



class DialogPaliers(QtGui.QDialog):
    
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_DialogPaliers()
        self.ui.setupUi(self)
        self.ui.comboBoxPaliers.addItems([self.trUtf8("empâtage"), self.trUtf8("palier")])
        self.mode()
           
        self.connect(self.ui.comboBoxPaliers, QtCore.SIGNAL("currentIndexChanged(QString)"), self.mode)
        self.connect(self.ui.doubleSpinBoxTargetTemp, QtCore.SIGNAL("valueChanged(QString)"), self.mode)
        self.connect(self.ui.doubleSpinBoxAddedVolume, QtCore.SIGNAL("valueChanged(QString)"), self.mode)
        self.connect(self.ui.doubleSpinBoxGrainW, QtCore.SIGNAL("valueChanged(QString)"), self.mode)
        self.connect(self.ui.doubleSpinBoxGrainT, QtCore.SIGNAL("valueChanged(QString)"), self.mode)
        self.connect(self.ui.doubleSpinBoxFudgeFactor, QtCore.SIGNAL("valueChanged(QString)"), self.mode)
        self.connect(self.ui.doubleSpinBoxMashTemp, QtCore.SIGNAL("valueChanged(QString)"), self.mode)
        self.connect(self.ui.doubleSpinBoxStartWater, QtCore.SIGNAL("valueChanged(QString)"), self.mode)
        
    def mode(self) :
        self.tTarget = self.ui.doubleSpinBoxTargetTemp.value()
        self.tGrain = self.ui.doubleSpinBoxGrainT.value()        
        self.fudgeFactor = self.ui.doubleSpinBoxFudgeFactor.value()
        if self.ui.comboBoxPaliers.currentIndex() is 0 : 
            self.ratio = self.ui.doubleSpinBoxAddedVolume.value() / self.ui.doubleSpinBoxGrainW.value()
            self.strikeMode()
        if self.ui.comboBoxPaliers.currentIndex() is 1 :
            self.mashMode()
            
    def strikeMode(self) :
        #Tstrike = [Ttarget + (0.4 * (Ttarget - Tgrain) / ratio)] + FF       
        self.ui.doubleSpinBoxMashTemp.hide()
        self.ui.label_8.hide()
        self.ui.doubleSpinBoxStartWater.hide()
        self.ui.label_9.hide()
        self.ui.label_4.show()
        self.ui.doubleSpinBoxGrainT.show()  
        self.tStrike = self.tTarget + (0.4*(self.tTarget-self.tGrain)/self.ratio) + self.fudgeFactor
        if self.tStrike > 100 :
            self.ui.labelTempWater.setText (self.trUtf8('''Au-dessus du point d'ébullition. Augmentez la quantité d'eau.'''))
            self.ui.labelRatio.setText("%.1f" %self.ratio)        
        else :
            self.ui.labelTempWater.setText("%.1f" %self.tStrike)
            self.ui.labelRatio.setText("%.1f" %self.ratio)
    
    def mashMode(self) :
        #Vm = Wgrain (0.4 + ratio)
        #Tstrike = (Ttarget*(Vstrike+Vm) - (Vm*Tmash)) / Vstrike
        self.ui.doubleSpinBoxStartWater.show()
        self.ui.doubleSpinBoxMashTemp.show()  
        self.ui.label_8.show()
        self.ui.label_9.show()
        self.ui.label_4.hide()
        self.ui.doubleSpinBoxGrainT.hide()     
        self.ratio = self.ui.doubleSpinBoxStartWater.value()/ self.ui.doubleSpinBoxGrainW.value()
        self.vStrike = self.ui.doubleSpinBoxAddedVolume.value()
        self.tMash = self.ui.doubleSpinBoxMashTemp.value()
        self.vm = self.ui.doubleSpinBoxGrainW.value() * (0.4 + self.ratio)
        self.tStrike = ((self.tTarget*(self.vStrike+self.vm) - (self.vm*self.tMash)) / self.vStrike) + self.fudgeFactor
        self.ratio = (self.ui.doubleSpinBoxAddedVolume.value() + self.ui.doubleSpinBoxStartWater.value())/ self.ui.doubleSpinBoxGrainW.value()
        if self.tStrike > 100 :
            self.ui.labelTempWater.setText (self.trUtf8('''Au-dessus du point d'ébullition. Augmentez la quantité d'eau.'''))
            self.ui.labelRatio.setText("%.1f" %self.ratio)
        else :
            self.ui.labelTempWater.setText("%.1f" %self.tStrike)
            self.ui.labelRatio.setText("%.1f" %self.ratio)
