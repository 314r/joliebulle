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
from reader import *
from globals import *

from editorG_ui import *
import xml.etree.ElementTree as ET
from xml.dom import minidom


class Dialog(QtGui.QDialog):
    baseChanged = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.uiMain = Ui_MainWindow ()
        self.base = ImportBase()
        self.base.importBeerXML()
        databaseXML = open(database_file,encoding='utf-8')
        database = ET.parse(databaseXML)
        
        self.ui.listWidgetGrains.addItems(self.base.liste_ingr)
        self.ui.comboBoxType.addItem(self.trUtf8('Grain'))
        self.ui.comboBoxType.addItem(self.trUtf8('Extrait'))
        self.ui.comboBoxType.addItem(self.trUtf8('Extrait sec'))
        self.ui.comboBoxType.addItem(self.trUtf8('Sucre'))
        self.ui.comboBoxType.addItem(self.trUtf8("Complément"))
        self.ui.comboBoxReco.addItem(self.trUtf8('Oui'))
        self.ui.comboBoxReco.addItem(self.trUtf8('Non'))
        
        self.ui.spinBoxCouleur.setMaximum(10000)
        self.ui.spinBoxRendmt.setMaximum(1000)
        
        self.connect(self.ui.listWidgetGrains, QtCore.SIGNAL("itemSelectionChanged ()"), self.voir)
        self.connect(self.ui.pushButtonNouveau, QtCore.SIGNAL("clicked()"), self.nouveau)
        self.connect(self.ui.pushButtonEnlever, QtCore.SIGNAL("clicked()"), self.enlever)
        self.connect(self.ui.pushButtonAjouter, QtCore.SIGNAL("clicked()"), self.ajouter)
        self.ui.radioButtonEBC.toggled.connect(self.toggleUnits)
        self.ui.buttonBox.rejected.connect(self.rejected)
        
        
        self.ui.lineEditNom.setEnabled(False)
        self.ui.comboBoxType.setEnabled(False)
        self.ui.spinBoxRendmt.setEnabled(False)
        self.ui.comboBoxReco.setEnabled(False)
        self.ui.spinBoxCouleur.setEnabled(False)
        self.ui.pushButtonAjouter.setEnabled(False)
        self.ui.pushButtonAjouter.setEnabled(False)
        self.ui.radioButtonSRM.setEnabled(False)
        self.ui.radioButtonEBC.setEnabled(False)
        
    def voir (self) :
        i = self.ui.listWidgetGrains.currentRow()
        
        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxType.setEnabled(True)
        self.ui.spinBoxRendmt.setEnabled(True)
        self.ui.comboBoxReco.setEnabled(True)
        self.ui.spinBoxCouleur.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)
        self.ui.radioButtonSRM.setEnabled(True)
        self.ui.radioButtonEBC.setEnabled(True)        
        self.ui.radioButtonSRM.setChecked(True)
        
        self.ui.lineEditNom.setText(self.base.liste_ingr[i])
        self.ui.spinBoxRendmt.setValue(self.base.liste_fYield[i])
        self.ui.spinBoxCouleur.setValue(self.base.liste_color[i]/1.97)
        
        if self.base.liste_fType[i] == 'Grain' :
            self.ui.comboBoxType.setCurrentIndex(0)      
        elif self.base.liste_fType[i] == 'Extract' :
            self.ui.comboBoxType.setCurrentIndex(1) 
        elif self.base.liste_fType[i] == 'Dry Extract' :
            self.ui.comboBoxType.setCurrentIndex(2)   
        elif self.base.liste_fType[i] == 'Sugar' :
            self.ui.comboBoxType.setCurrentIndex(3)  
        elif self.base.liste_fType[i] == 'Adjunct' :
            self.ui.comboBoxType.setCurrentIndex(4)  
        else :
            self.ui.comboBoxType.setCurrentIndex(0)
            
        if self.base.liste_fMashed[i] =='TRUE' :
            self.ui.comboBoxReco.setCurrentIndex(0) 
        elif self.base.liste_fMashed[i] =='FALSE' :
            self.ui.comboBoxReco.setCurrentIndex(1)      
        else :
            self.ui.comboBoxReco.setCurrentIndex(0)
            
    def toggleUnits (self) :
        
        if self.ui.radioButtonEBC.isChecked() :
            self.ui.spinBoxCouleur.setValue(round(self.ui.spinBoxCouleur.value()*1.97))
        else :
            self.ui.spinBoxCouleur.setValue(round(self.ui.spinBoxCouleur.value()/1.97))
            
    def ajouter (self) :
        self.base.importBeerXML()
        
        #Attention aux unités. Dans la base xml la couleur est en srm, dans la liste de la base la couleur est convertie en EBC
        
        nom = self.ui.lineEditNom.text()
        self.base.liste_ingr.append(nom)
        self.base.liste_ingr.sort()
        i = self.base.liste_ingr.index(nom)
        

        self.base.liste_fYield.insert(i, self.ui.spinBoxRendmt.value())
        self.ui.radioButtonSRM.setChecked(True)
        self.base.liste_color.insert(i, self.ui.spinBoxCouleur.value()*1.97)
        
        if self.ui.comboBoxType.currentIndex() is 0 :
            self.base.liste_fType.insert(i, 'Grain')
        elif self.ui.comboBoxType.currentIndex() is 1 :
            self.base.liste_fType.insert(i, 'Extract') 
        elif self.ui.comboBoxType.currentIndex() is 2 :
            self.base.liste_fType.insert(i, 'Dry Extract')
        elif self.ui.comboBoxType.currentIndex() is 3 :
            self.base.liste_fType.insert(i, 'Sugar')
        elif self.ui.comboBoxType.currentIndex() is 4 :
            self.base.liste_fType.insert(i, 'Adjunct')
            
        if self.ui.comboBoxReco.currentIndex() is 0 :
            self.base.liste_fMashed.insert(i, 'TRUE')
        else :
            self.base.liste_fMashed.insert(i, 'FALSE')
        
        
        self.ui.listWidgetGrains.clear()   
        self.ui.listWidgetGrains.addItems(self.base.liste_ingr)
        
        
        databaseXML = codecs.open(database_file,encoding="utf-8" )
        database = ET.parse(databaseXML)
        root= database.getroot()
        databaseXML.close()

        fermentable = ET.Element('FERMENTABLE')
        name = ET.SubElement(fermentable, 'NAME')
        name.text = nom
        ftype = ET.SubElement(fermentable, 'TYPE')
        ftype.text = self.base.liste_fType[i]
        fyield = ET.SubElement(fermentable, 'YIELD')
        fyield.text = str(self.base.liste_fYield[i])
        color = ET.SubElement(fermentable, 'COLOR')
        color.text = str(self.base.liste_color[i] / 1.97)
        reco = ET.SubElement(fermentable, 'RECOMMEND_MASH')
        reco.text = self.base.liste_fMashed[i]
        
        root.insert(i, fermentable)
        #databaseXML = open(database_file, 'w')
        #databaseXML.write(ET.tostring(root))
        #databaseXML.close()
        databaseXML = open(database_file, 'wb')
        database._setroot(root)
        database.write(databaseXML, encoding="utf-8")
        databaseXML.close()
        
        
        

        
    def nouveau (self) :
        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxType.setEnabled(True)
        self.ui.spinBoxRendmt.setEnabled(True)
        self.ui.comboBoxReco.setEnabled(True)
        self.ui.spinBoxCouleur.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)
        self.ui.radioButtonSRM.setEnabled(True)
        self.ui.radioButtonEBC.setEnabled(True)        
        self.ui.radioButtonSRM.setChecked(True)
        
        self.ui.lineEditNom.setText('')
        self.ui.spinBoxCouleur.setValue(0)
        self.ui.spinBoxRendmt.setValue(0)
        self.ui.comboBoxReco.setCurrentIndex(0)
        self.ui.comboBoxType.setCurrentIndex(0)
        
        
    def enlever (self) :
        self.base.importBeerXML()
        i = self.ui.listWidgetGrains.currentRow()
        del self.base.liste_ingr[i]
        del self.base.liste_fYield[i]
        del self.base.liste_color[i]
        del self.base.liste_fType[i]
        del self.base.liste_fMashed[i]
        self.ui.listWidgetGrains.clear()   
        self.ui.listWidgetGrains.addItems(self.base.liste_ingr)
        
        databaseXML = codecs.open(database_file, encoding='utf-8')
        database = ET.parse(databaseXML)
        root= database.getroot()
        databaseXML.close()
        iterator = root.getiterator("FERMENTABLE")
        item = iterator[i]
        root.remove(item)
        #databaseXML = open(database_file, 'w')
        #databaseXML.write(ET.tostring(root))
        #databaseXML.close()     
        databaseXML = open(database_file, 'wb')
        database._setroot(root)
        database.write(databaseXML, encoding="utf-8")
        databaseXML.close() 
        
    def rejected(self) :     
        #self.emit( QtCore.SIGNAL( "baseChanged"))
        self.baseChanged.emit()
        
        

        
     
