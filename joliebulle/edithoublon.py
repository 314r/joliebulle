#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­



#joliebulle 3.3
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




import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from base import *
from globals import *
import view.base

from editorH_ui import *
import xml.etree.ElementTree as ET
from xml.dom import minidom
import model.constants


class DialogH(QtGui.QDialog):
    baseChanged = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.base = ImportBase()
        #self.base.importBeerXML()

        self.ui.listViewHoublons.setModel( view.base.getHopsQtModel() )
        self.ui.comboBoxForme.addItem(self.trUtf8('Feuille'))
        self.ui.comboBoxForme.addItem(self.trUtf8('Pellet'))
        self.ui.comboBoxForme.addItem(self.trUtf8('Cône'))

        self.connect(self.ui.listViewHoublons.selectionModel(), QtCore.SIGNAL("currentChanged(const QModelIndex &, const QModelIndex &)"), self.voir)
        self.connect(self.ui.pushButtonNouveau, QtCore.SIGNAL("clicked()"), self.nouveau)
        self.connect(self.ui.pushButtonEnlever, QtCore.SIGNAL("clicked()"), self.enlever)
        self.connect(self.ui.pushButtonAjouter, QtCore.SIGNAL("clicked()"), self.ajouter)
        self.ui.buttonBox.rejected.connect(self.rejected)
        
        self.ui.lineEditNom.setEnabled(False)
        self.ui.spinBoxAlpha.setEnabled(False)
        self.ui.comboBoxForme.setEnabled(False)
        self.ui.pushButtonAjouter.setEnabled(False)

        
    def setModel(self):
        self.ui.listViewHoublons.setModel( view.base.getHopsQtModel() )
        self.connect(self.ui.listViewHoublons.selectionModel(), QtCore.SIGNAL("currentChanged(const QModelIndex &, const QModelIndex &)"), self.voir)
        
    def voir(self, current, previous) :

        self.ui.lineEditNom.setEnabled(True)
        self.ui.spinBoxAlpha.setEnabled(True)
        self.ui.comboBoxForme.setEnabled(True)   
        self.ui.pushButtonAjouter.setEnabled(True) 

        h = current.data(view.constants.MODEL_DATA_ROLE)
        
        self.ui.lineEditNom.setText(h.name)
        self.ui.spinBoxAlpha.setValue(h.alpha)
        
        if model.constants.HOP_FORM_LEAF == h.form :
            self.ui.comboBoxForme.setCurrentIndex(0)
        elif model.constants.HOP_FORM_PELLET == h.form :
            self.ui.comboBoxForme.setCurrentIndex(1)
        elif model.constants.HOP_FORM_PLUG == h.form  :
            self.ui.comboBoxForme.setCurrentIndex(2)
        else :
            self.ui.comboBoxForme.setCurrentIndex(0)

    def ajouter(self) :
        h = Hop()
        h.name = self.ui.lineEditNom.text()
        h.alpha = self.ui.spinBoxAlpha.value()
        if self.ui.comboBoxForme.currentIndex() is 0 :
            h.form = model.constants.HOP_FORM_LEAF
        elif self.ui.comboBoxForme.currentIndex() is 1 :
            h.form = model.constants.HOP_FORM_PELLET
        elif self.ui.comboBoxForme.currentIndex() is 2 :
            h.form = model.constants.HOP_FORM_PLUG
        else :
            h.form = model.constants.HOP_FORM_LEAF
        ImportBase.addHop(h) 
        self.setModel()

        
    def nouveau(self) :
        self.ui.lineEditNom.setEnabled(True)
        self.ui.spinBoxAlpha.setEnabled(True)
        self.ui.comboBoxForme.setEnabled(True)   
        self.ui.pushButtonAjouter.setEnabled(True)
        
        self.ui.lineEditNom.setText('')
        self.ui.spinBoxAlpha.setValue(0)
        self.ui.comboBoxForme.setCurrentIndex(2)
        
    def enlever(self) :
        selection = self.ui.listViewHoublons.selectionModel().selectedIndexes()
        for index in selection :
            h = index.data(view.constants.MODEL_DATA_ROLE)
        ImportBase().delHop(h)
        self.setModel()
        
    def rejected(self) :     
        self.baseChanged.emit()        
