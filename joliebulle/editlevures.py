#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­



#joliebulle 3.5
#Copyright (C) 2010-2016 Pierre Tavares
#Copyright (C) 2012-2015 joliebulle's authors
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


from editorY_ui import *
import xml.etree.ElementTree as ET
from xml.dom import minidom


class DialogL(QtGui.QDialog):
    baseChanged = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.base = ImportBase()
        #self.base.importBeerXML() 
        
        self.ui.listViewLevures.setModel( view.base.getYeastsQtModel() )
        self.ui.comboBoxForme.addItem(self.trUtf8('Liquide'))
        self.ui.comboBoxForme.addItem(self.trUtf8('Poudre'))
        self.ui.comboBoxForme.addItem(self.trUtf8('Gélose'))
        self.ui.comboBoxForme.addItem(self.trUtf8('Culture'))
        
        self.connect(self.ui.listViewLevures.selectionModel(), QtCore.SIGNAL("currentChanged(const QModelIndex &, const QModelIndex &)"), self.voir)  
        self.connect(self.ui.pushButtonNouveau, QtCore.SIGNAL("clicked()"), self.nouveau)
        self.connect(self.ui.pushButtonEnlever, QtCore.SIGNAL("clicked()"), self.enlever)
        self.connect(self.ui.pushButtonAjouter, QtCore.SIGNAL("clicked()"), self.ajouter)
        self.ui.buttonBox.rejected.connect(self.rejected)
        
        self.ui.lineEditNom.setEnabled(False)
        self.ui.comboBoxForme.setEnabled(False)
        self.ui.lineEditLabo.setEnabled(False)
        self.ui.lineEditID.setEnabled(False)
        self.ui.spinBoxAtten.setEnabled(False)
        self.ui.pushButtonAjouter.setEnabled(False)

    def setModel(self) :
        self.ui.listViewLevures.setModel( view.base.getYeastsQtModel() ) 
        self.connect(self.ui.listViewLevures.selectionModel(), QtCore.SIGNAL("currentChanged(const QModelIndex &, const QModelIndex &)"), self.voir) 
        
    def voir(self, current, previous) :
        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxForme.setEnabled(True)
        self.ui.lineEditLabo.setEnabled(True)
        self.ui.lineEditID.setEnabled(True)
        self.ui.spinBoxAtten.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)
        
        y = current.data(view.constants.MODEL_DATA_ROLE)

        self.ui.lineEditNom.setText(y.name)
        self.ui.lineEditLabo.setText(y.labo)
        self.ui.lineEditID.setText(y.productId)
        self.ui.spinBoxAtten.setValue(y.attenuation)
        
        if y.form == 'Liquid' :
            self.ui.comboBoxForme.setCurrentIndex(0)
        elif y.form == 'Dry' :
            self.ui.comboBoxForme.setCurrentIndex(1)
        elif y.form == 'Slant' :
            self.ui.comboBoxForme.setCurrentIndex(2)
        elif y.form == 'Culture' :
            self.ui.comboBoxForme.setCurrentIndex(3)
        else :
            self.ui.comboBoxForme.setCurrentIndex(0)
            
    def ajouter(self) :
        y = Yeast()
        y.name = self.ui.lineEditNom.text()
        y.labo = self.ui.lineEditLabo.text()
        y.productId = self.ui.lineEditID.text()
        y.attenuation = self.ui.spinBoxAtten.value()

        if self.ui.comboBoxForme.currentIndex() is 0 :
            y.form =  'Liquid'
        elif self.ui.comboBoxForme.currentIndex() is 1 :
            y.form = 'Dry'
        elif self.ui.comboBoxForme.currentIndex() is 2 :
            y.form = 'Slant'
        elif self.ui.comboBoxForme.currentIndex() is 3 :
            y.form = 'Culture'
        else :
            y.form = 'Dry'

        ImportBase.addYeast(y)
        self.setModel()
        
    def nouveau(self) :
        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxForme.setEnabled(True)
        self.ui.lineEditLabo.setEnabled(True)
        self.ui.lineEditID.setEnabled(True)
        self.ui.spinBoxAtten.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)
        
        self.ui.lineEditNom.setText('')
        self.ui.lineEditLabo.setText('')
        self.ui.lineEditID.setText('')
        self.ui.comboBoxForme.setCurrentIndex(0)
        self.ui.spinBoxAtten.setValue(0)
        
    def enlever(self) :
        selection = self.ui.listViewLevures.selectionModel().selectedIndexes()
        for index in selection :
            y = index.data(view.constants.MODEL_DATA_ROLE)
            ImportBase().delYeast(y)
        self.setModel()
        
    def rejected(self) :     
        self.baseChanged.emit()
        
        
