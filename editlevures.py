#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­



#JolieBulle 2.3
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
from base import *
from globals import *

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
        self.base.importBeerXML() 
        
        self.ui.listWidgetLevures.addItems(self.base.liste_levuresDetail)
        self.ui.comboBoxForme.addItem(self.trUtf8('Liquide'))
        self.ui.comboBoxForme.addItem(self.trUtf8('Poudre'))
        self.ui.comboBoxForme.addItem(self.trUtf8('Gélose'))
        self.ui.comboBoxForme.addItem(self.trUtf8('Culture'))
        
        self.connect(self.ui.listWidgetLevures, QtCore.SIGNAL("itemSelectionChanged ()"), self.voir)  
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
        
        
    def voir(self) :
        i = self.ui.listWidgetLevures.currentRow()
        
        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxForme.setEnabled(True)
        self.ui.lineEditLabo.setEnabled(True)
        self.ui.lineEditID.setEnabled(True)
        self.ui.spinBoxAtten.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)
        
        self.ui.lineEditNom.setText(self.base.liste_levures[i])
        self.ui.lineEditLabo.setText(self.base.liste_lLabo[i])
        self.ui.lineEditID.setText(self.base.liste_lProdid[i])
        self.ui.spinBoxAtten.setValue(self.base.liste_levureAtten[i])
        
        if self.base.liste_lForm[i] == 'Liquid' :
            self.ui.comboBoxForme.setCurrentIndex(0)
        elif self.base.liste_lForm[i] == 'Dry' :
            self.ui.comboBoxForme.setCurrentIndex(1)
        elif self.base.liste_lForm[i] == 'Slant' :
            self.ui.comboBoxForme.setCurrentIndex(2)
        elif self.base.liste_lForm[i] == 'Culture' :
            self.ui.comboBoxForme.setCurrentIndex(3)
        else :
            self.ui.comboBoxForme.setCurrentIndex(0)
            
    def ajouter(self) :
        self.base.importBeerXML()
        nom = self.ui.lineEditNom.text()
        self.base.liste_levures.append(nom)
        self.base.liste_levures.sort()
        i = self.base.liste_levures.index(nom)
        f = len(self.base.liste_ingr) 
        h = len(self.base.liste_houblons)
        m = len(self.base.liste_divers)
        
        self.base.liste_lLabo.insert(i, self.ui.lineEditLabo.text())
        self.base.liste_lProdid.insert(i, self.ui.lineEditID.text())
        self.base.liste_levureAtten.insert(i, self.ui.spinBoxAtten.value())
                
        if self.ui.comboBoxForme.currentIndex() is 0 :
            self.base.liste_lForm.insert(i, 'Liquid')
        elif self.ui.comboBoxForme.currentIndex() is 1 :
            self.base.liste_lForm.insert(i, 'Dry')
        elif self.ui.comboBoxForme.currentIndex() is 2 :
            self.base.liste_lForm.insert(i, 'Slant')
        elif self.ui.comboBoxForme.currentIndex() is 3 :
            self.base.liste_lForm.insert(i, 'Culture')
        else :
            self.base.liste_lForm.insert(i, 'Dry')
        
        self.base.liste_levuresDetail.insert(i, nom + ' ' + self.base.liste_lLabo[i] + ' ' + self.base.liste_lProdid[i]) 
            
        self.ui.listWidgetLevures.clear()
        self.ui.listWidgetLevures.addItems(self.base.liste_levuresDetail)
        
        databaseXML = codecs.open(database_file, encoding="utf-8")
        database = ET.parse(databaseXML)
        root= database.getroot()
        databaseXML.close()  
        
        levure = ET.Element('YEAST')
        name = ET.SubElement(levure ,'NAME')
        name.text = nom
        forme = ET.SubElement(levure ,'FORM')
        forme.text = self.base.liste_lForm[i]
        labo = ET.SubElement(levure ,'LABORATORY')
        labo.text = self.base.liste_lLabo[i]
        prodid = ET.SubElement(levure ,'PRODUCT_ID')
        prodid.text = self.base.liste_lProdid[i]
        atten = ET.SubElement(levure ,'ATTENUATION')
        atten.text = str(self.base.liste_levureAtten[i])
        
        root.insert(i + f + h + m, levure)
        #databaseXML = open(database_file, 'w')
        #databaseXML.write(ET.tostring(root))
        #databaseXML.close()
        databaseXML = open(database_file, 'wb')
        database._setroot(root)
        database.write(databaseXML, encoding="utf-8")
        databaseXML.close()
        
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
        self.base.importBeerXML()
        i = self.ui.listWidgetLevures.currentRow()
        del self.base.liste_levures[i]
        del self.base.liste_lLabo[i]
        del self.base.liste_lProdid[i]
        del self.base.liste_levureAtten[i]
        del self.base.liste_lForm[i]
        del self.base.liste_levuresDetail[i]
        self.ui.listWidgetLevures.clear()
        self.ui.listWidgetLevures.addItems(self.base.liste_levuresDetail)
        
        databaseXML = codecs.open(database_file, encoding="utf-8")
        database = ET.parse(databaseXML)
        root= database.getroot()
        databaseXML.close()    
        iterator = root.getiterator("YEAST")
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
        self.baseChanged.emit()
        
        
