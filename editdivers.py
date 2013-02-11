#!/usr/bin/python3
#­*­coding: utf­8 -­*­



#JolieBulle 2.7
#Copyright (C) 2010-2012 Pierre Tavares

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
import view.base

from editorM_ui import *
import xml.etree.ElementTree as ET
from xml.dom import minidom



class DialogD(QtGui.QDialog):
    baseChanged = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.base = ImportBase()

        self.ui.listViewDivers.setModel( view.base.getMiscsQtModel() )
        self.ui.comboBoxType.addItem(self.trUtf8("Epice"))
        self.ui.comboBoxType.addItem(self.trUtf8("Clarifiant"))
        self.ui.comboBoxType.addItem(self.trUtf8("Traitement Eau"))
        self.ui.comboBoxType.addItem(self.trUtf8("Herbe"))
        self.ui.comboBoxType.addItem(self.trUtf8("Arôme"))
        self.ui.comboBoxType.addItem(self.trUtf8("Autre"))
        
        self.connect(self.ui.listViewDivers.selectionModel(), QtCore.SIGNAL("currentChanged(const QModelIndex &, const QModelIndex &)"), self.voir)
        self.connect(self.ui.pushButtonNouveau, QtCore.SIGNAL("clicked()"), self.nouveau)
        self.connect(self.ui.pushButtonEnlever, QtCore.SIGNAL("clicked()"), self.enlever)
        self.connect(self.ui.pushButtonAjouter, QtCore.SIGNAL("clicked()"), self.ajouter)
        self.ui.buttonBox.rejected.connect(self.rejected)
        
        self.ui.lineEditNom.setEnabled(False)
        self.ui.comboBoxType.setEnabled(False)
        self.ui.pushButtonAjouter.setEnabled(False)
        
        
        
    def voir(self, current, previous) :
        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxType.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)

        m = current.data(view.constants.MODEL_DATA_ROLE)

        self.ui.lineEditNom.setText(m.name)
        if m.type == 'Spice' :
            self.ui.comboBoxType.setCurrentIndex(0)
        elif m.type == 'Fining' :
            self.ui.comboBoxType.setCurrentIndex(1)
        elif m.type == 'Water Agent' :
            self.ui.comboBoxType.setCurrentIndex(2)
        elif m.type == 'Herb' :
            self.ui.comboBoxType.setCurrentIndex(3)
        elif m.type == 'Flavor' :
            self.ui.comboBoxType.setCurrentIndex(4)
        elif m.type == 'Other' :
            self.ui.comboBoxType.setCurrentIndex(5)
        else :
            self.ui.comboBoxType.setCurrentIndex(0)
            
    def ajouter(self) :
        m = Misc()
        m.name = self.ui.lineEditNom.text()
        
        if self.ui.comboBoxType.currentIndex() is 0 :
            m.type = 'Spice'
        elif self.ui.comboBoxType.currentIndex() is 1 :
            m.type = 'Fining'
        elif self.ui.comboBoxType.currentIndex() is 2 :
            m.type = 'Water Agent'
        elif self.ui.comboBoxType.currentIndex() is 3 :
            m.type = 'Herb'
        elif self.ui.comboBoxType.currentIndex() is 4 :
            m.type = 'Flavor'
        elif self.ui.comboBoxType.currentIndex() is 5 :
              m.type = 'Other'
        else :
              m.type = 'Spice'
        ImportBase.addMisc(m)
        self.ui.listViewDivers.setModel(view.base.getMiscsQtModel() )
        
    def nouveau(self) :
        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxType.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)
        
        self.ui.lineEditNom.setText('')
        self.ui.comboBoxType.setCurrentIndex(0)
        
    def enlever(self) :
        selection = self.ui.listViewDivers.selectionModel().selectedIndexes()
        for index in selection :
            m = index.data(view.constants.MODEL_DATA_ROLE)
            ImportBase().delMisc(m)
        self.ui.listViewDivers.setModel(view.base.getMiscsQtModel() )
        return

        self.base.importBeerXML()
        i = self.ui.listViewDivers.currentRow()
        
        del self.base.liste_divers[i]
        del self.base.liste_dType[i]
        
        self.ui.listViewDivers.clear()
        self.ui.listViewDivers.addItems(self.base.liste_divers)
        
        databaseXML = codecs.open(database_file, encoding="utf-8")
        database = ET.parse(databaseXML)
        root= database.getroot()
        databaseXML.close()    
        iterator = root.getiterator("MISC")
        item = iterator[i] 
        root.remove(item)
        #databaseXML = open('database.xml', 'w')
        #databaseXML.write(ET.tostring(root))
        #databaseXML.close()   
        databaseXML = open(database_file, 'wb')
        database._setroot(root)
        database.write(databaseXML, encoding="utf-8")
        databaseXML.close()
        
    def rejected(self) :     
        self.baseChanged.emit()    
