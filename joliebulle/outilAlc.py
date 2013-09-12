 #!/usr/bin/python3
#­*­coding: utf­8 -­*­


#joliebulle 3.0
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

from outilAlc_ui import *
import xml.etree.ElementTree as ET
from xml.dom import minidom


class DialogAlc(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_DialogAlc()
        self.ui.setupUi(self) 
        
        #self.connect(self.ui.doubleSpinBoxDI, QtCore.SIGNAL("valueChanged(QString)"), self.calcAlc)
        #self.connect(self.ui.doubleSpinBoxDF, QtCore.SIGNAL("valueChanged(QString)"), self.calcAlc)
        
        self.ui.doubleSpinBoxDI.valueChanged.connect(self.calcAlc)
        self.ui.doubleSpinBoxDF.valueChanged.connect(self.calcAlc)
        self.ui.doubleSpinBoxSucre.valueChanged.connect(self.calcAlc)
        
    def calcAlc(self) :
        self.OG = self.ui.doubleSpinBoxDI.value()
        self.FG = self.ui.doubleSpinBoxDF.value()
        self.Sucre = self.ui.doubleSpinBoxSucre.value()

        self.ABV = ((((self.OG - self.FG) * 1.05) / self.FG) * 100) / 0.795 + ((self.Sucre * 0.5) / 0.795) / 10
        
        self.ui.labelAlc.setText("%.1f" %self.ABV)
