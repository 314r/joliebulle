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
from outilDilution_ui import *



class DialogDilution(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_DialogDilution()
        self.ui.setupUi(self)
        
        #self.connect(self.ui.doubleSpinBoxVolInitial, QtCore.SIGNAL("valueChanged(QString)"), self.calculDilution)
        #self.connect(self.ui.doubleSpinBoxDensInitiale, QtCore.SIGNAL("valueChanged(QString)"), self.calculDilution)
        #self.connect(self.ui.doubleSpinBoxVolAjoute, QtCore.SIGNAL("valueChanged(QString)"), self.calculDilution)
        #self.connect(self.ui.doubleSpinBoxDensAjout, QtCore.SIGNAL("valueChanged(QString)"), self.calculDilution)
        #self.connect(self.ui.doubleSpinBoxVolFinal, QtCore.SIGNAL("valueChanged(QString)"), self.calculVolumeReverse)
        
        self.ui.doubleSpinBoxVolInitial.valueChanged.connect(self.calculDilution)
        self.ui.doubleSpinBoxDensInitiale.valueChanged.connect(self.calculDilution)
        self.ui.doubleSpinBoxVolAjoute.valueChanged.connect(self.calculDilution)
        self.ui.doubleSpinBoxDensAjout.valueChanged.connect(self.calculDilution)
        self.ui.doubleSpinBoxVolFinal.valueChanged.connect(self.calculVolumeReverse)
        
    def calculDilution (self) :
        
        #volumeFinal*densFinale = (volumeInitial*densInitiale) + (volumeAjoute*densAjout)
        
        self.volumeInitial = self.ui.doubleSpinBoxVolInitial.value()
        self.densInitiale = self.ui.doubleSpinBoxDensInitiale.value()
        self.volumeAjoute = self.ui.doubleSpinBoxVolAjoute.value()
        self.densAjout = self.ui.doubleSpinBoxDensAjout.value()
        
        self.volumeFinal = self.volumeInitial + self.volumeAjoute
        
        self.densFinale = ((self.volumeInitial*self.densInitiale) + (self.volumeAjoute*self.densAjout)) / self.volumeFinal
               
        self.ui.doubleSpinBoxVolFinal.setValue(self.volumeFinal)
        self.ui.labelDensFinal.setText("<b>%.3f</b>" %self.densFinale)
        
    def calculVolumeReverse (self) :
        
        self.volumeFinal = self.ui.doubleSpinBoxVolFinal.value()
        self.volumeAjoute = self.volumeFinal - self.volumeInitial
        
        self.ui.doubleSpinBoxVolAjoute.setValue(self.volumeAjoute)
        
       
        
    
        
