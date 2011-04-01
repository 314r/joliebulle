#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­



#JolieBulle 2.1
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

from editorH_ui import *
import xml.etree.ElementTree as ET
from xml.dom import minidom


class DialogH(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.base = ImportBase()
        self.base.importBeerXML()
        
        self.ui.listWidgetHoublons.addItems(self.base.liste_houblons)
        self.ui.comboBoxForme.addItem(self.trUtf8('Feuille'))
        self.ui.comboBoxForme.addItem(self.trUtf8('Pellet'))
        self.connect(self.ui.listWidgetHoublons, QtCore.SIGNAL("itemSelectionChanged ()"), self.voir)  
        self.connect(self.ui.pushButtonNouveau, QtCore.SIGNAL("clicked()"), self.nouveau)
        self.connect(self.ui.pushButtonEnlever, QtCore.SIGNAL("clicked()"), self.enlever)
        self.connect(self.ui.pushButtonAjouter, QtCore.SIGNAL("clicked()"), self.ajouter)
        
        self.ui.lineEditNom.setEnabled(False)
        self.ui.spinBoxAlpha.setEnabled(False)
        self.ui.comboBoxForme.setEnabled(False)
        self.ui.pushButtonAjouter.setEnabled(False)
        
        
    def voir(self) :
        i = self.ui.listWidgetHoublons.currentRow()
        self.ui.lineEditNom.setEnabled(True)
        self.ui.spinBoxAlpha.setEnabled(True)
        self.ui.comboBoxForme.setEnabled(True)   
        self.ui.pushButtonAjouter.setEnabled(True)
          
        self.ui.lineEditNom.setText(self.base.liste_houblons[i])
        self.ui.spinBoxAlpha.setValue(self.base.liste_hAlpha[i])
        
        if self.base.liste_hForm[i] == "Leaf" :
            self.ui.comboBoxForme.setCurrentIndex(0)
        elif self.base.liste_hForm[i] == "Pellet" :
            self.ui.comboBoxForme.setCurrentIndex(1)
        else :
            self.ui.comboBoxForme.setCurrentIndex(0)

    def ajouter(self) :
      
        nom = self.ui.lineEditNom.text()
        self.base.liste_houblons.append(nom)
        self.base.liste_houblons.sort()
        i = self.base.liste_houblons.index(nom)
        f = len(self.base.liste_ingr)
        
        self.base.liste_hAlpha.insert(i, self.ui.spinBoxAlpha.value())
        if self.ui.comboBoxForme.currentIndex() is 0 :
            self.base.liste_hForm.insert(i, 'Leaf')
        elif self.ui.comboBoxForme.currentIndex() is 1 :
            self.base.liste_hForm.insert(i, 'Pellet')   
        else :
            self.base.liste_hForm.insert(i, 'Leaf')
       
        self.ui.listWidgetHoublons.clear()   
        self.ui.listWidgetHoublons.addItems(self.base.liste_houblons)    
        
        databaseXML = open('database.xml')
        database = ET.parse(databaseXML)
        root= database.getroot()
        databaseXML.close()  
        
        hop = ET.Element('HOP')
        name = ET.SubElement(hop ,'NAME')
        name.text = nom
        alpha = ET.SubElement(hop, 'ALPHA')
        alpha.text = str(self.base.liste_hAlpha[i])
        form = ET.SubElement(hop, 'FORM')
        form.text = self.base.liste_hForm[i]
        
        root.insert(i + f, hop)
        #databaseXML = open('database.xml', 'w')
        #databaseXML.write(ET.tostring(root))
        #databaseXML.close()
        databaseXML = open('database.xml', 'wb')
        database._setroot(root)
        database.write(databaseXML, encoding="UTF-8")
        databaseXML.close()
        
        
    def nouveau(self) :
        self.ui.lineEditNom.setEnabled(True)
        self.ui.spinBoxAlpha.setEnabled(True)
        self.ui.comboBoxForme.setEnabled(True)   
        self.ui.pushButtonAjouter.setEnabled(True)
        
        self.ui.lineEditNom.setText('')
        self.ui.spinBoxAlpha.setValue(0)
        self.ui.comboBoxForme.setCurrentIndex(0)
        
    def enlever(self) :
        i = self.ui.listWidgetHoublons.currentRow()
        f = len(self.base.liste_ingr)
        
        del self.base.liste_houblons[i]
        del self.base.liste_hForm[i]
        del self.base.liste_hAlpha[i]
        self.ui.listWidgetHoublons.clear()
        self.ui.listWidgetHoublons.addItems(self.base.liste_houblons)
         
        databaseXML = open('database.xml')
        database = ET.parse(databaseXML)
        root= database.getroot()
        databaseXML.close()    
        iterator = root.getiterator("HOP")
        item = iterator[i] 
        root.remove(item)
        #databaseXML = open('database.xml', 'w')
        #databaseXML.write(ET.tostring(root))
        #databaseXML.close()            
        databaseXML = open('database.xml', 'wb')
        database._setroot(root)
        database.write(databaseXML, encoding="UTF-8")
        databaseXML.close()
        
