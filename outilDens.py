#!/usr/bin/python3
#­*­coding: utf­8 -­*­



#JolieBulle 2.8
#Copyright (C) 2010-2013 Pierre Tavares

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
from base import *

from densimetre_ui import *
import xml.etree.ElementTree as ET
from xml.dom import minidom


class DialogOutilDens(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_DialogDensimetre()
        self.ui.setupUi(self)
        
        #self.connect(self.ui.doubleSpinBoxTempEchan, QtCore.SIGNAL("valueChanged(QString)"), self.corrDens)
        #self.connect(self.ui.doubleSpinBoxTempCalib, QtCore.SIGNAL("valueChanged(QString)"), self.corrDens)
        #self.connect(self.ui.doubleSpinBoxDens, QtCore.SIGNAL("valueChanged(QString)"), self.corrDens)
        
        self.ui.doubleSpinBoxTempEchan.valueChanged.connect(self.corrDens)
        self.ui.doubleSpinBoxTempCalib.valueChanged.connect(self.corrDens)
        self.ui.doubleSpinBoxDens.valueChanged.connect(self.corrDens)
        
    def corrDens (self) :
        
        #on recupere les valeurs
        self.dens = self.ui.doubleSpinBoxDens.value()
        self.calib = self.ui.doubleSpinBoxTempCalib.value()
        self.temp = self.ui.doubleSpinBoxTempEchan.value()
        
        #calcul du facteur de correction
        self.facteurCorr = ((self.dens-(self.calib+288.9414)/(508929.2*(self.calib+68.12963))*(self.calib-3.9863)**2)/(1-(self.temp+288.9414)/(508929.2*(self.temp+68.12963))*(self.temp-3.9863)**2))-self.dens
      
        #la densité corrigee
        self.densCorr = self.dens + self.facteurCorr
               
        self.ui.labelDensCorr.setText("%.3f" %self.densCorr)
