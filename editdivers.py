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
        #self.base.importBeerXML()
        
#        self.ui.listWidgetDivers.addItems(self.base.liste_divers)
        self.ui.listViewDivers.setModel( self.base.getMiscsQtModel() )
        self.ui.comboBoxType.addItem(self.trUtf8("Epice"))
        self.ui.comboBoxType.addItem(self.trUtf8("Clarifiant"))
        self.ui.comboBoxType.addItem(self.trUtf8("Traitement Eau"))
        self.ui.comboBoxType.addItem(self.trUtf8("Herbe"))
        self.ui.comboBoxType.addItem(self.trUtf8("Arôme"))
        self.ui.comboBoxType.addItem(self.trUtf8("Autre"))
        
        self.connect(self.ui.listViewDivers, QtCore.SIGNAL("itemSelectionChanged ()"), self.voir)
        self.connect(self.ui.pushButtonNouveau, QtCore.SIGNAL("clicked()"), self.nouveau)
        self.connect(self.ui.pushButtonEnlever, QtCore.SIGNAL("clicked()"), self.enlever)
        self.connect(self.ui.pushButtonAjouter, QtCore.SIGNAL("clicked()"), self.ajouter)
        self.ui.buttonBox.rejected.connect(self.rejected)
        
        self.ui.lineEditNom.setEnabled(False)
        self.ui.comboBoxType.setEnabled(False)
        self.ui.pushButtonAjouter.setEnabled(False)
        
        
        
    def voir(self) :
        i = self.ui.listViewDivers.currentRow()
        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxType.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)
        
        self.ui.lineEditNom.setText(self.base.liste_divers[i])
        if self.base.liste_dType [i] == 'Spice' :
            self.ui.comboBoxType.setCurrentIndex(0)
        elif self.base.liste_dType [i] == 'Fining' :
            self.ui.comboBoxType.setCurrentIndex(1)
        elif self.base.liste_dType [i] == 'Water Agent' :
            self.ui.comboBoxType.setCurrentIndex(2)
        elif self.base.liste_dType [i] == 'Herb' :
            self.ui.comboBoxType.setCurrentIndex(3)
        elif self.base.liste_dType [i] == 'Flavor' :
            self.ui.comboBoxType.setCurrentIndex(4)
        elif self.base.liste_dType [i] == 'Other' :
            self.ui.comboBoxType.setCurrentIndex(5)
        else :
            self.ui.comboBoxType.setCurrentIndex(0)
            
    def ajouter(self) :
        self.base.importBeerXML()
        nom = self.ui.lineEditNom.text()
        self.base.liste_divers.append(nom)
        self.base.liste_divers.sort()
        i = self.base.liste_divers.index(nom)
        f = len(self.base.liste_ingr)
        h = len(self.base.liste_houblons)
        
        if self.ui.comboBoxType.currentIndex() is 0 :
            self.base.liste_dType.insert(i, 'Spice')
        elif self.ui.comboBoxType.currentIndex() is 1 :
            self.base.liste_dType.insert(i, 'Fining')
        elif self.ui.comboBoxType.currentIndex() is 2 :
            self.base.liste_dType.insert(i, 'Water Agent')
        elif self.ui.comboBoxType.currentIndex() is 3 :
            self.base.liste_dType.insert(i, 'Herb')
        elif self.ui.comboBoxType.currentIndex() is 4 :
            self.base.liste_dType.insert(i, 'Flavor')
        elif self.ui.comboBoxType.currentIndex() is 5 :
              self.base.liste_dType.insert(i, 'Other')   
        else :
              self.base.liste_dType.insert(i, 'Spice')
              
        self.ui.listViewDivers.clear()
        self.ui.listViewDivers.addItems(self.base.liste_divers)
        
        databaseXML = codecs.open(database_file, encoding="utf-8")
        database = ET.parse(databaseXML)
        root= database.getroot()
        databaseXML.close()
        
        divers = ET.Element('MISC')
        name = ET.SubElement(divers, 'NAME')
        name.text = nom
        dtype = ET.SubElement(divers, 'TYPE')
        dtype.text = self.base.liste_dType[i]
        
        root.insert(i + f + h, divers)
        #databaseXML = open('database.xml', 'w')
        #databaseXML.write(ET.tostring(root))
        #databaseXML.close()
        databaseXML = open(database_file, 'wb')
        database._setroot(root)
        database.write(databaseXML, encoding="utf-8")
        databaseXML.close()
        
    def nouveau(self) :
        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxType.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)
        
        self.ui.lineEditNom.setText('')
        self.ui.comboBoxType.setCurrentIndex(0)
        
    def enlever(self) :
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
