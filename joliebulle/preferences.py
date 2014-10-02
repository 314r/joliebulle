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
import logging
from PyQt4 import QtGui
from PyQt4 import QtCore
from base import *
from globals import *
from preferences_ui import *
from settings import * 
from globals import *
import xml.etree.ElementTree as ET
from xml.dom import minidom

logger = logging.getLogger(__name__)


class DialogPref(QtGui.QDialog):
    prefAccepted = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        settings = Settings()
        self.ui = Ui_Preferences()
        self.ui.setupUi(self)
        self.ui.lineEditPathLib.setText(recettes_dir)
        try :
            self.ui.spinBoxBoilOff.setValue(int(settings.conf.value("BoilOffRate")))
            self.ui.spinBoxCooling.setValue(int(settings.conf.value("CoolingLoss")))
        except :
            pass
        try :
            self.ui.spinBoxGrainTemp.setValue(int(settings.conf.value("GrainTemp")))
            self.ui.doubleSpinBoxFudgeFactor.setValue(float(settings.conf.value("FudgeFactor")))
        except :
            pass
        try :
            self.ui.doubleSpinBoxGrainRetention.setValue(int(settings.conf.value("GrainRetention")))
        except :
            pass
            
        #les connexions
        self.ui.pushButtonChangeLib.clicked.connect(self.changePushed)
        self.ui.buttonBox.accepted.connect(self.accepted)
        self.ui.buttonBox.rejected.connect(self.rejected)
        
    def changePushed (self) :
        self.d = QtGui.QFileDialog.getExistingDirectory(self,
            self.trUtf8("Choisir un dossier"),
            home_dir,
            )
        if not self.d :
            pass
        else :
            self.ui.lineEditPathLib.setText(self.d)
        
    def accepted(self) :    
        
        if platform == 'win32' :
            settings.conf.setValue("pathWin32", self.ui.lineEditPathLib.text())
        else :
            settings.conf.setValue("pathUnix", self.ui.lineEditPathLib.text())
            logger.debug(settings.conf.value("pathUnix"))
            
        settings.conf.setValue("BoilOffRate", self.ui.spinBoxBoilOff.value())
        settings.conf.setValue("CoolingLoss", self.ui.spinBoxCooling.value())
        settings.conf.setValue("GrainTemp", self.ui.spinBoxGrainTemp.value())
        settings.conf.setValue("FudgeFactor", self.ui.doubleSpinBoxFudgeFactor.value())
        settings.conf.setValue("GrainRetention", self.ui.doubleSpinBoxGrainRetention.value())

        self.prefAccepted.emit()
        
            
    def rejected (self) :
        self.ui.lineEditPathLib.setText(recettes_dir)
