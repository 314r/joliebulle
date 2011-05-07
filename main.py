#!/usr/bin/python3
#­*­coding: utf­8 -­*­



#JolieBulle 2.15
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



import os
from sys import platform
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from reader import *
from export import *
from exportHTML import *
from base import *
from editgrain import *
from edithoublon import *
from editdivers import * 
from editlevures import *
from outilDens import *
from outilAlc import *
from outilDilution import *
from outilEvaporation import *
from globals import *



import xml.etree.ElementTree as ET

class IngDelegate(QtGui.QItemDelegate):
    def __init__(self, parent=None):
        QtGui.QItemDelegate.__init__(self, parent)
    def createEditor(self, parent, option, index) :  
        #return editor
        pass
    def setEditorData(self, spinBox, index):
        pass
    def setModelData(self, spinBox, model, index):
        pass
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

class AmountDelegate(QtGui.QItemDelegate):
    def __init__(self, parent=None):
            QtGui.QItemDelegate.__init__(self, parent)


    def createEditor(self, parent, option, index) :
        self.listeF = AppWindow()
        i=self.listeF.nbreFer
        h=self.listeF.nbreHops
        m=self.listeF.nbreDivers

        row=index.row()
        if row < i+h+m:
            editor = QtGui.QSpinBox(parent)
            editor.setMinimum(0)
            editor.setMaximum(20000)
            editor.installEventFilter(self)

            return editor

    def setEditorData(self, spinBox, index):
        value= int(index.model().data(index, QtCore.Qt.DisplayRole))

        spinBox.setValue(value)
        spinBox.setSuffix(" g")

    def setModelData(self, spinBox, model, index):
        spinBox.interpretText()
        value = spinBox.value()
           
        model.setData(index, value)
        

        self.emit( QtCore.SIGNAL( "pySig"))
        
        
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
        
        
class TimeDelegate(QtGui.QItemDelegate):
    def __init__(self, parent=None):
            QtGui.QItemDelegate.__init__(self, parent)
            

    def createEditor(self, parent, option, index) :

        #le nombre d'ingredients fermentescibles pour lesquels on ne prend pas en compte le temps d'ebullition
        self.listeF = AppWindow()
        i=self.listeF.nbreFer
        h=self.listeF.nbreHops

        row=index.row()
        if row > i-1 and row < i+h:
            editor = QtGui.QSpinBox(parent)
            editor.setMinimum(0)
            editor.setMaximum(20000)
            editor.installEventFilter(self)

            return editor

    def setEditorData(self, spinBox, index):
        value= int(index.model().data(index, QtCore.Qt.DisplayRole))
        
        spinBox.setValue(value)
        spinBox.setSuffix(" min")

    def setModelData(self, spinBox, model, index):
        spinBox.interpretText()
        value = spinBox.value()
        
        #model.setData(index, QtCore.QVariant(value))
        model.setData(index, value)
        self.emit( QtCore.SIGNAL( "pySig"))
                            
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
    

class AlphaDelegate(QtGui.QItemDelegate):
    def __init__(self, parent=None):
            QtGui.QItemDelegate.__init__(self, parent)
            

    def createEditor(self, parent, option, index) :
        
        #le nombre d'ingredients fermentescibles pour lesquels on ne prend pas en compte les acides alpha
        self.listeF = AppWindow()
        i=self.listeF.nbreFer
        h=self.listeF.nbreHops

        row=index.row()
        if row > i-1 and row < i+h:
        
            editor = QtGui.QDoubleSpinBox(parent)
            editor.setMinimum(0)
            editor.setMaximum(20000)
            editor.installEventFilter(self)
            return editor
        else :
            pass
        

    def setEditorData(self, spinBox, index):
        value= float(index.model().data(index, QtCore.Qt.DisplayRole))

        spinBox.setValue(value)
        spinBox.setSuffix(" %")

    def setModelData(self, spinBox, model, index):
        spinBox.interpretText()
        value = spinBox.value()
        
        
        model.setData(index, value)
        self.emit( QtCore.SIGNAL( "pySig"))
                            
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

class ComboBoxDelegate(QtGui.QItemDelegate):


    def __init__(self, parent = None):

        QtGui.QItemDelegate.__init__(self, parent)
        

    def createEditor(self, parent, option, index):
        self.listeF = AppWindow()
        

        i=self.listeF.nbreFer
        h=self.listeF.nbreHops
        row=index.row()
        if row > i-1 and row < i+h :
            editor = QtGui.QComboBox( parent )
            editor.insertItem(0,'Pellet')
            editor.insertItem(1,'Leaf')
        return editor

    def setEditorData( self, comboBox, index ):
        value = index.model().data(index, QtCore.Qt.DisplayRole)
        if value == 'Pellet' : 
            value = 0
        else :
            value = 1
       
        
        comboBox.setCurrentIndex(value)
        
    def setModelData(self, editor, model, index):
        
        value = editor.currentText()
        
        model.setData( index, value )
        self.emit( QtCore.SIGNAL( "pySig"))
       

       

    def updateEditorGeometry( self, editor, option, index ):

        editor.setGeometry(option.rect)
        


class AppWindow(QtGui.QMainWindow,Ui_MainWindow):

    nbreFer=0
    nbreHops=0
    nbreDivers=0
    
    
        
        
  
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.initRep()
        self.dlgEditG = Dialog(self)
        self.dlgEditH = DialogH(self)
        self.dlgEditD = DialogD(self)
        self.dlgEditY = DialogL(self)
        self.dlgOutilDens = DialogOutilDens(self)
        self.dlgOutilAlc = DialogAlc(self)
        self.dlgOutilDilution = DialogDilution(self)
        self.dlgOutilEvaporation = DialogEvaporation(self)
        self.base = ImportBase()
        self.base.importBeerXML()
        self.s=0
        
        self.baseStyleListe = [self.trUtf8('Générique'), '1A. Lite American Lager', '1B. Standard American Lager', '1C. Premium American Lager', '1D. Munich Helles', '1E. Dortmunder Export', '2A. German Pilsner (Pils)', '2B. Bohemian Pilsener', '2C. Classic American Pilsner', '3A. Vienna Lager', '3B. Oktoberfest/Märzen', '4A. Dark American Lager', '4B. Munich Dunkel', '4C. Schwarzbier (Black Beer)', '5A. Maibock/Helles Bock', '5B. Traditional Bock', '5C. Doppelbock', '5D. Eisbock', '6A. Cream Ale', '6B. Blonde Ale', '6C. Kölsch', '6D. American Wheat or Rye Beer', '7A. Northern German Altbier', '7B. California Common Beer', '7C. Düsseldorf Altbier', '8A. Standard/Ordinary Bitter', '8B. Special/Best/Premium Bitter', '8C. Extra Special/Strong Bitter (English Pale Ale)', '9A. Scottish Light 60/-', '9B. Scottish Heavy 70/-', '9C. Scottish Export 80/- ', '9D. Irish Red Ale', '9E. Strong Scotch Ale', '10A. American Pale Ale', '10B. American Amber Ale', '10C. American Brown Ale', '11A. Mild','11B. Southern English Brown', '11C. Northern English Brown Ale', '12A. Brown Porter', '12B. Robust Porter', '12C. Baltic Porter', '13A. Dry Stout', '13B. Sweet Stout', '13C. Oatmeal Stout', '13D. Foreign Extra Stout', '13E. American Stout', '13F. Russian Imperial Stout', '14A. English IPA', '14B. American IPA', '14C. Imperial IPA','15A. Weizen/Weissbier', '15B. Dunkelweizen', '15C. Weizenbock', '15D. Roggenbier (German Rye Beer)','16A. Witbier', '16B. Belgian Pale Ale', '16C. Saison', '16D. Bière de Garde', '16E. Belgian Specialty Ale', '17A. Berliner Weisse', '17B. Flanders Red Ale', '17C. Flanders Brown Ale/Oud Bruin', '17D. Straight (Unblended) Lambic', '17E. Gueuze', '17F. Fruit Lambic', '18A. Belgian Blond Ale', '18B. Belgian Dubbel', '18C. Belgian Tripel', '18D. Belgian Golden Strong Ale', '18E. Belgian Dark Strong Ale', '19A. Old Ale', '19B. English Barleywine', '19C. American Barleywine', '20. Fruit Beer', '21A. Spice, Herb, or Vegetable Beer', '21B. Christmas/Winter Specialty Spiced Beer', '22A. Classic Rauchbier', '22B. Other Smoked Beer', '22C. Wood-Aged Beer', '23. Specialty Beer', '24A. Dry Mead', '24B. Semi-sweet Mead', '24C. Sweet Mead', '25A. Cyser', '25B. Pyment', '25C. Other Fruit Melomel', '26A. Metheglin', '26B. Braggot', '26C. Open Category Mead', '27A. Common Cider', '27B. English Cider', '27C. French Cider', '27D. Common Perry', '27E. Traditional Perry', '28A. New England Cider', '28B. Fruit Cider', '28C. Applewine', '28D. Other Specialty Cider/Perry']
        #Les connections
        self.connect(self.actionOuvrir, QtCore.SIGNAL("triggered()"), self.ouvrir_clicked)
        self.connect(self.actionOuvrir_2, QtCore.SIGNAL("triggered()"), self.ouvrir_clicked)
        self.connect(self.actionNouvelle_recette, QtCore.SIGNAL("triggered()"), self.purge)
        self.connect(self.actionEnregistrer, QtCore.SIGNAL("triggered()"), self.enregistrer)
        self.connect(self.actionEnregistrer_Sous, QtCore.SIGNAL("triggered()"), self.enregistrerSous)
        self.connect(self.actionExporterHtml, QtCore.SIGNAL("triggered()"), self.exporterHtml)
        
        self.connect(self.actionEditGrains, QtCore.SIGNAL("triggered()"), self.editGrains)
        self.connect(self.actionEditHoublons, QtCore.SIGNAL("triggered()"), self.editHoublons)
        self.connect(self.actionEditDivers, QtCore.SIGNAL("triggered()"), self.editDivers)
        self.connect(self.actionEditLevures, QtCore.SIGNAL("triggered()"), self.editLevures)
        
        self.connect(self.actionAbout, QtCore.SIGNAL("triggered()"), self.about)
        self.connect(self.actionCorrectionDens, QtCore.SIGNAL("triggered()"), self.outilDens)
        self.connect(self.actionCalculAlc, QtCore.SIGNAL("triggered()"), self.outilAlc)
        self.connect(self.actionDilution, QtCore.SIGNAL("triggered()"), self.outilDilution)
        self.connect(self.actionEvaporation, QtCore.SIGNAL("triggered()"), self.outilEvaporation)
        
        
        self.connect(self.actionImprimer, QtCore.SIGNAL("triggered()"), self.printRecipe)
         
        self.connect(self.doubleSpinBoxRendemt, QtCore.SIGNAL("valueChanged(QString)"), self.rendemt_changed)
        self.connect(self.doubleSpinBox_2Volume, QtCore.SIGNAL("valueChanged(QString)"), self.volume_changed)
        self.connect(self.pushButtonAjouter_2, QtCore.SIGNAL("clicked()"), self.ajouterF)
        self.connect(self.pushButtonAjouterH, QtCore.SIGNAL("clicked()"), self.ajouterH)
        self.connect(self.pushButtonAjouterY, QtCore.SIGNAL("clicked()"), self.ajouterY)
        self.connect(self.pushButtonAjouterM, QtCore.SIGNAL("clicked()"), self.ajouterM)
        self.connect(self.pushButtonEnlever, QtCore.SIGNAL("clicked()"), self.enlever)
        self.connect(self.pushButtonChangerStyle, QtCore.SIGNAL("clicked()"), self.modifierStyle)
        self.connect(self.pushButtonVolMore, QtCore.SIGNAL("clicked()"), self.volMore)
        self.connect(self.doubleSpinBoxVolPre, QtCore.SIGNAL("valueChanged(QString)"), self.volPreCalc)
        
        self.connect(self.comboBoxStyle, QtCore.SIGNAL("currentIndexChanged(QString)"), self.addStyle)
        #self.connect(self.pushButtonEssai, QtCore.SIGNAL("clicked()"), self.essai)
        
        #Les modeles et vues du widget central
        self.modele = QtGui.QStandardItemModel(0, 6)
        self.connect(self.modele, QtCore.SIGNAL("dataChanged(QModelIndex,QModelIndex)"), self.reverseMVC)
        
        liste_headers = [self.trUtf8("Ingrédients"),self.trUtf8("Quantité (g)"),self.trUtf8("Temps (min)"),self.trUtf8("Acide Alpha (%)"),self.trUtf8("Type"),self.trUtf8("Proportion")]
        self.modele.setHorizontalHeaderLabels(liste_headers)
        
        self.deleg = AmountDelegate(self)
        self.tableViewF.setItemDelegateForColumn(1,self.deleg)
        self.connect(self.deleg, QtCore.SIGNAL( "pySig"), self.modeleProportion)
        
        
        
        self.delegT = TimeDelegate(self)
        self.tableViewF.setItemDelegateForColumn(2,self.delegT)
        self.connect(self.delegT, QtCore.SIGNAL( "pySig"), self.modeleProportion)

        self.delegA = AlphaDelegate(self)
        self.tableViewF.setItemDelegateForColumn(3,self.delegA)
        self.connect(self.delegA, QtCore.SIGNAL( "pySig"), self.modeleProportion)
        
        self.delegC = ComboBoxDelegate(self)
        self.tableViewF.setItemDelegateForColumn(4,self.delegC)  
        self.connect(self.delegC, QtCore.SIGNAL( "pySig"), self.modeleProportion)
        
        self.delegI = IngDelegate(self)
        self.tableViewF.setItemDelegateForColumn(0,self.delegI)
        self.tableViewF.setItemDelegateForColumn(5,self.delegI)

        self.tableViewF.setModel(self.modele)
        self.tableViewF.setColumnWidth(0,250)
        

        
        ##on cree un modele pour les ingredients dispo dans la base
        #self.modeleIngBase = QtGui.QStandardItemModel()
        ##la vue correspondante
        #self.treeViewIng.setModel(self.modeleIngBase)
        ##on va remplir tout ça... avec une autre fonction
        #self.listeIng()
        self.comboBox.addItems(self.base.liste_ingr)
        self.comboBox.setCurrentIndex(10)
        
        self.comboBoxH.addItems(self.base.liste_houblons)
        self.comboBoxH.setCurrentIndex(10)
        
        self.comboBoxY.addItems(self.base.liste_levuresDetail)
        self.comboBoxY.setCurrentIndex(10)
        
        self.comboBoxM.addItems(self.base.liste_divers)
        self.comboBoxM.setCurrentIndex(0)
        
        self.comboBoxStyle.hide()
        self.comboBoxStyle.addItems(self.baseStyleListe)

        self.widgetVol.hide()
        
        self.nouvelle()
        
    def initRep(self) :
        
        
        home = QtCore.QDir(home_dir)
        config = QtCore.QDir(config_dir)
        print (config)
        if not config.exists() :
            print('non')
            home.mkpath (config_dir)
        else :
            pass
        database = QtCore.QFile(database_file)
        if not database.exists() :
            print('''pas de database''')
            database.copy(database_root, database_file)
        else :
            pass
        
    def modeleProportion (self) :
        #Cette fonction est appelée chaque fois que la quantité, les AA ou les temps sont modifiés, via un signal émit par les classes Delegate.
        #Cette fonction inclut les données calculées dans le modèle.
       
        i=0
        while i < AppWindow.nbreFer :
            i=i+1
            for prop in self.liste_fProportion :
                prop = QtGui.QStandardItem("%.0f" %(self.liste_fProportion[i-1]) + "%")
                self.modele.setItem(i-1,5,prop)
                
        h=0
        while h < AppWindow.nbreHops :
            h = h+1
            for prop in self.liste_ibuPart :
                prop = QtGui.QStandardItem("%.1f" %(self.liste_ibuPart[h-1]) + " IBU")
                self.modele.setItem(i+h-1,5,prop)
                
         
    # cette fonction est appelee chaque fois que les donnees du modele changent
    def reverseMVC(self) : 
    
        
        
        i = 0
        while i < AppWindow.nbreFer :
            i = i+1
            
            index = self.modele.index(i-1,1)
            value = self.modele.data(index, QtCore.Qt.DisplayRole)
            self.liste_fAmount[i-1] = float(value)
            
            
            index_fIngr = self.modele.index(i-1,0)
            value_fIngr = self.modele.data(index_fIngr, QtCore.Qt.DisplayRole)
            self.liste_ingr[i-1] = value_fIngr
            
            
            
            
  
            
        h = 0
        while h < AppWindow.nbreHops :
            h = h+1
            
 
            for index in self.liste_hAmount :
                index = self.modele.index(i+h-1,1)
                value = self.modele.data(index, QtCore.Qt.DisplayRole)
                self.liste_hAmount[h-1] = float(value)
            for index in self.liste_hTime :
                index = self.modele.index(i+h-1,2)
                value = self.modele.data(index, QtCore.Qt.DisplayRole)  
                self.liste_hTime[h-1] = float(value)
            for index in self.liste_hAlpha :
                index = self.modele.index(i+h-1,3)
                value = self.modele.data(index, QtCore.Qt.DisplayRole)  
                self.liste_hAlpha[h-1] = float(value)  
            for index in self.liste_hForm :
                index = self.modele.index(i+h-1,4)
                value = str(self.modele.data(index, QtCore.Qt.DisplayRole))
                
                if value == 'None' or value == '' :
                    pass
                else :
                    self.liste_hForm[h-1] = str(value)
            
                

            
       
   
        
        
        m = 0 
        while m < AppWindow.nbreDivers : 
            m = m+1
            for index in self.liste_dAmount :
                index = self.modele.index(i+h+m-1,1)
                value = self.modele.data(index, QtCore.Qt.DisplayRole)
                self.liste_dAmount[m-1] = float(value)
            
       
        
        
       
        self.calculs_recette()  
        print (self.liste_fProportion)
        

    
    def MVC(self) :      

        
        i=0
        while i < AppWindow.nbreFer :
            i=i+1
            for item in self.liste_ingr : 
                item = QtGui.QStandardItem(self.liste_ingr[i-1])
                self.modele.setItem(i-1,0,item)
            for amount in self.liste_fAmount : 
                amount = QtGui.QStandardItem("%.0f" %(self.liste_fAmount[i-1]))
                self.modele.setItem(i-1,1,amount)
            for ftype in self.liste_fType :
                ftype = QtGui.QStandardItem(self.liste_fType[i-1])
                self.modele.setItem(i-1,4,ftype)
            for prop in self.liste_fProportion :
                prop = QtGui.QStandardItem("%.0f" %(self.liste_fProportion[i-1]) + "%")
                self.modele.setItem(i-1,5,prop)

        
        

        h=0
        while h < AppWindow.nbreHops :
            h = h+1
            for item in self.liste_houblons : 
                item = QtGui.QStandardItem(self.liste_houblons[h-1])
                self.modele.setItem(i+h-1,0,item)
            for amount in self.liste_hAmount : 
                amount = QtGui.QStandardItem("%.0f" %(self.liste_hAmount[h-1]) )
                self.modele.setItem(i+h-1,1,amount)
            for time in self.liste_hTime :
                time = QtGui.QStandardItem("%.0f" %(self.liste_hTime[h-1]) )
                self.modele.setItem(i+h-1,2,time)                   
            for alpha in self.liste_hAlpha :
                alpha = QtGui.QStandardItem("%.1f" %(self.liste_hAlpha[h-1]) )
                self.modele.setItem(i+h-1,3,alpha)  
            for form in self.liste_hForm :
                form = QtGui.QStandardItem(str(self.liste_hForm[h-1]))
                self.modele.setItem(i+h-1,4,form)
            for prop in self.liste_ibuPart :
                prop = QtGui.QStandardItem("%.1f" %(self.liste_ibuPart[h-1]) + " IBU")
                self.modele.setItem(i+h-1,5,prop)
            



                
        m = 0
        while m < AppWindow.nbreDivers :
            m = m+1
            for item in self.liste_divers :
                item = QtGui.QStandardItem(self.liste_divers[m-1] + ' [' +self.liste_dType[m-1] + ']')
                self.modele.setItem(i+h+m-1, 0, item)
                
            for amount in self.liste_dAmount : 
                  amount = QtGui.QStandardItem("%.0f" %(self.liste_dAmount[m-1]) )
                  self.modele.setItem(i+h+m-1, 1, amount)



        l=0
        while l < self.nbreLevures : 
            l=l+1
            for item in self.liste_levuresDetail : 
                item = QtGui.QStandardItem(self.liste_levuresDetail[l-1])
                self.modele.setItem( i+h+m+l-1,0,item)
                
                

    def editGrains(self) :
        self.dlgEditG.setModal(True)
        self.dlgEditG.show()
        
    def editHoublons(self) :
        self.dlgEditH.setModal(True)
        self.dlgEditH.show()
        
    def editDivers(self) :
        self.dlgEditD.setModal(True)
        self.dlgEditD.show()   
    
    def editLevures(self) :
        self.dlgEditY.setModal(True)
        self.dlgEditY.show()     
        
    def outilDens(self) : 
        self.dlgOutilDens.setModal(True)
        self.dlgOutilDens.show()
        
    def outilAlc(self) :
        self.dlgOutilAlc.setModal(True)
        self.dlgOutilAlc.show()
        
    def outilDilution(self) :
        self.dlgOutilDilution.setModal(True)
        self.dlgOutilDilution.show()
      
    def outilEvaporation (self) :
        self.dlgOutilEvaporation.setModal(True)
        self.dlgOutilEvaporation.show()
        
    def purge (self) :
        i = (AppWindow.nbreFer + AppWindow.nbreDivers + AppWindow.nbreHops + self.nbreLevures)
        self.modele.removeRows(0,i)
        AppWindow.nbreFer = 0
        AppWindow.nbreHops = 0
        AppWindow.nbreDivers = 0
        self.nouvelle()
        
        
        

       
    def ajouterF(self) :

        
        
        f = AppWindow.nbreFer
        i=self.comboBox.currentIndex()
        
        item = QtGui.QStandardItem(self.base.liste_ingr[i])
        item_fAmount = QtGui.QStandardItem(0)
        self.modele.insertRow(f)

        self.liste_ingr.append(self.base.liste_ingr[i])
        self.liste_fAmount.append(1000)
        self.liste_fYield.append(self.base.liste_fYield[i])
        self.liste_fType.append(self.base.liste_fType[i])
        self.liste_color.append(self.base.liste_color[i])
        self.liste_fMashed.append(self.base.liste_fMashed[i])       
        AppWindow.nbreFer = f + 1
        self.calculs_recette()
        self.MVC()
        
        print (self.liste_fProportion)
        
    def ajouterH(self) : 
        
        f = AppWindow.nbreFer
        h = AppWindow.nbreHops
        i = self.comboBoxH.currentIndex()
        
        itemH = QtGui.QStandardItem(self.base.liste_houblons[i])
        item_hAmount = QtGui.QStandardItem(0)
        item_hForm = QtGui.QStandardItem(self.base.liste_hForm[i])
        item_hTime = QtGui.QStandardItem(0)
        item_hAlpha = QtGui.QStandardItem(self.base.liste_hAlpha[i])
        
        self.modele.insertRow(f+h)
        

        
        self.liste_houblons.append(self.base.liste_houblons[i])
        self.liste_hAmount.append(0)
        self.liste_hForm.append('Leaf')
        self.liste_hTime.append(0)
        self.liste_hAlpha.append(self.base.liste_hAlpha[i])
        
        AppWindow.nbreHops = h + 1
        self.calculs_recette()
        self.MVC()
        
     
    def ajouterM(self) :
        
        l = self.nbreLevures
        f = AppWindow.nbreFer
        h = AppWindow.nbreHops
        m = AppWindow.nbreDivers
        
        i = self.comboBoxM.currentIndex()
        
        itemD = QtGui.QStandardItem(self.base.liste_divers[i])
        item_dAmount = QtGui.QStandardItem(0)
        item_dType = QtGui.QStandardItem(self.base.liste_dType[i])
 
        
        self.modele.insertRow(f+h+m)
        
        self.liste_divers.append(self.base.liste_divers[i])
        self.liste_dAmount.append(0)
        self.liste_dType.append(self.base.liste_dType[i])
        
        AppWindow.nbreDivers = m +1
        self.MVC()
        
       

     
     
     
    def ajouterY(self) :
        l = self.nbreLevures
        f = AppWindow.nbreFer
        h = AppWindow.nbreHops
        m = AppWindow.nbreDivers
        
        i = self.comboBoxY.currentIndex()
        
        itemY = QtGui.QStandardItem(self.base.liste_levures[i])
        item_lForm = QtGui.QStandardItem(self.base.liste_lForm[i])
        item_lLabo = QtGui.QStandardItem(self.base.liste_lLabo[i])
        item_lProdid = QtGui.QStandardItem(self.base.liste_lProdid[i])
        item_levureAtten = QtGui.QStandardItem(self.base.liste_levureAtten[i])
        item_levuresDetail =QtGui.QStandardItem(self.base.liste_levuresDetail[i])
        
        self.modele.insertRow(f+h+m+l)
        
       
        
        self.liste_levures.append(self.base.liste_levures[i])
        self.liste_lForm.append(self.base.liste_lForm[i])
        self.liste_lLabo.append(self.base.liste_lLabo[i])
        self.liste_lProdid.append(self.base.liste_lProdid[i])
        self.liste_levureAtten.append(self.base.liste_levureAtten[i])
        self.liste_levuresDetail.append(self.base.liste_levuresDetail[i])
        
        self.nbreLevures = l + 1
        self.MVC()
        
         
         
        
         
    
    def enlever(self) :
        selection = self.tableViewF.selectionModel()
        indexLigne = selection.currentIndex().row()
        f = AppWindow.nbreFer
        h = AppWindow.nbreHops
        l = self.nbreLevures
        m = AppWindow.nbreDivers
        
        
        if indexLigne < 0 :
            pass
        else :
            if indexLigne < f :
                del self.liste_ingr[indexLigne]
                del self.liste_fAmount[indexLigne]
                del self.liste_fType[indexLigne]
                del self.liste_fYield[indexLigne]
                del self.liste_fMashed[indexLigne]
                del self.liste_color[indexLigne]
                self.modele.removeRow(indexLigne)
                AppWindow.nbreFer = f - 1
                self.reverseMVC()
                
            if indexLigne > f-1 and indexLigne < f+h :      
                del self.liste_houblons[indexLigne-f]
                del self.liste_hAmount[indexLigne-f]
                del self.liste_hForm[indexLigne-f]
                del self.liste_hTime[indexLigne-f]
                del self.liste_hAlpha[indexLigne-f]
                self.modele.removeRow(indexLigne)
                AppWindow.nbreHops = h - 1
                self.reverseMVC()   

                
            if indexLigne > f+h-1 and indexLigne < f+h+m :
                del self.liste_divers[indexLigne-(f+h)]
                del self.liste_dAmount[indexLigne-(f+h)]
                del self.liste_dType[indexLigne-(f+h)]
                self.modele.removeRow(indexLigne)
                AppWindow.nbreDivers = m-1
                self.reverseMVC()
                
            if indexLigne > f+h+m-1 and indexLigne < f+h+m+l :
                del self.liste_levures[indexLigne-(f+h+m)]
                del self.liste_lForm[indexLigne-(f+h+m)]
                del self.liste_lLabo[indexLigne-(f+h+m)]
                del self.liste_lProdid[indexLigne-(f+h+m)]
                del self.liste_levureAtten[indexLigne-(f+h+m)]
                del self.liste_levuresDetail[indexLigne-(f+h+m)]
                self.modele.removeRow(indexLigne)
                self.nbreLevures = l-1
                
                self.reverseMVC()
                
            else :
                pass
            self.calculs_recette()
            self.MVC()
            print (self.liste_fProportion)
            print ("index : " , indexLigne)
 
        


    
    
    def importBeerXML(self) :
        fichierBeerXML = self.s

        

        arbre = ET.parse(fichierBeerXML)

        presentation=arbre.find('.//RECIPE')
        style=arbre.find('.//STYLE')
        fermentables=arbre.findall('.//FERMENTABLE')
        hops = arbre.findall('.//HOP')
        levures = arbre.findall('.//YEAST')
        misc = arbre.findall('.//MISC')
        brassin = arbre.find('.//MASH')
        paliers = arbre.findall('.//MASH_STEP')
        
        
        
        
        #Presentation de la recette
        self.styleRecette =''
        for nom in presentation :
            if nom.tag == "NAME" : 
                    self.nomRecette = nom.text
            
             
        for nom in style :
            if nom.tag == "NAME" : 
                self.styleRecette = nom.text
                
        for batch_size in presentation :
            if batch_size.tag == "BATCH_SIZE" : 
                self.volume = batch_size.text
                
        for efficiency in presentation :
            if efficiency.tag == "EFFICIENCY" : 
                self.rendement= float(efficiency.text)  
        
        for boil in presentation :
            if boil.tag == 'BOIL_TIME' :
                self.boil = boil.text


    
        self.lineEditRecette.setText(self.nomRecette)
        self.lineEditGenre.setText(self.styleRecette)
        self.doubleSpinBox_2Volume.setValue(float(self.volume))
        self.doubleSpinBoxRendemt.setValue(self.rendement)
        try : 
            self.spinBoxBoil.setValue(float(self.boil))
        except :
            self.spinBoxBoil.setValue (0)
        self.doubleSpinBoxVolPre.setValue(float(self.volume))
        
    
    
        #Ingredient fermentescibles
        AppWindow.nbreFer = len(fermentables)
        self.liste_ingr = list()
        self.liste_fAmount = list()
        self.liste_fType = list()
        self.liste_fYield = list()
        self.liste_fMashed = list()
        self.liste_color = list()
        self.fMashed = ''
        
        
        i = 0
        while i < AppWindow.nbreFer :

            i=i+1
            for nom in fermentables[i-1] :
                if nom.tag == 'NAME' :
                    self.fNom = nom.text
                    self.liste_ingr.append(self.fNom)
                    
                if nom.tag =='AMOUNT' :
                    self.fAmount = 1000*(float(nom.text)) 
                    self.liste_fAmount.append(self.fAmount)
                    
                if nom.tag =='TYPE' :
                    self.fType = nom.text 
                    self.liste_fType.append(self.fType)
                    
                if nom.tag == 'YIELD' :
                    self.fYield = float(nom.text)
                    self.liste_fYield.append(self.fYield)
                    
                if nom.tag == 'RECOMMEND_MASH' :
                    self.fMashed = nom.text
                    self.liste_fMashed.append(self.fMashed)
                    
                #ATTENTION ! le format BeerXML utilise des unités SRM ! 
                #srm*1.97 =ebc
                if nom.tag == 'COLOR' :
                    self.color = float(nom.text)*1.97
                    self.liste_color.append(self.color)
                    

        
        
        #Houblons
        
        AppWindow.nbreHops = len(hops)
        self.liste_houblons = list()
        self.liste_hAmount = list()
        self.liste_hForm = list()
        self.liste_hTime = list()
        self.liste_hAlpha = list()
        
        
        
        h = 0
        while h < AppWindow.nbreHops : 
            h = h+1
            for nom in hops [h-1] :
                if nom.tag == 'NAME' :
                    self.hNom = nom.text
                    self.liste_houblons.append(self.hNom)
                    
                if nom.tag =='AMOUNT' :
                    self.hAmount = 1000*(float(nom.text)) 
                    self.liste_hAmount.append(self.hAmount)
                    
                if nom.tag =='FORM' :
                    self.hForm = nom.text 
                    self.liste_hForm.append(self.hForm)
                    
                if nom.tag =='TIME' :
                    self.hTime = float(nom.text)
                    self.liste_hTime.append(self.hTime)
                    
                
                if nom.tag =='ALPHA' :
                    self.hAlpha = float(nom.text)
                    self.liste_hAlpha.append(self.hAlpha)                   
                    
                                                            

        
        
        #Levure 
        self.nbreLevures = len(levures)
        self.liste_levures = list()
        self.liste_lForm = list()
        self.liste_lLabo = list()
        self.liste_lProdid = list()
        self.liste_levuresDetail = list()
        self.liste_levureAtten = list ()
        self.lNom = ""
        self.lLabo =""
        self.lProd =""
        self.lForm = ""
        self.lAtten=""
        
        l = 0
        while l < self.nbreLevures : 
            l = l+1
            for nom in levures [l-1] :
                if nom.tag == 'NAME' :
                    self.lNom = str(nom.text)
                    self.liste_levures.append(self.lNom)    
                    
                if nom.tag == 'FORM' :
                    self.lForm = str(nom.text)
                    self.liste_lForm.append(self.lForm)
                    
                if nom.tag == 'LABORATORY' :
                    self.lLabo = str(nom.text)
                    self.liste_lLabo.append(self.lLabo)
                    
                if nom.tag == 'PRODUCT_ID' :
                    self.lProd = str(nom.text)
                    self.liste_lProdid.append(self.lProd)
                
                if nom.tag == 'ATTENUATION' :
                    self.lAtten = float(nom.text)
                    self.liste_levureAtten.append(self.lAtten)
                    
                    
                    
            self.liste_levuresDetail.append (self.lNom+ ' ' + self.lLabo +' ' + self.lProd)
                    
                    
                    
        
        
        
        #Ingredients divers
        AppWindow.nbreDivers = len(misc)
        self.liste_divers = list ()
        self.liste_dAmount = list ()
        self.liste_dType = list ()
        self.dNom = ''
        self.dAmount = 0
        self.dType = ''
        
        
        m = 0
        while  m < AppWindow.nbreDivers :
            m = m+1
            for nom in misc [m-1] : 
                if nom.tag == 'NAME' :
                    self.dNom = nom.text
                    self.liste_divers.append(self.dNom)
                    
                if nom.tag == 'AMOUNT' :
                    self.dAmount = float(nom.text)*1000
                    self.liste_dAmount.append(self.dAmount)
                    
                if nom.tag == 'TYPE' :
                     self.dType = nom.text
                     self.liste_dType.append(self.dType)

        
        
        #Brassin
        self.bNom = ''
        if not brassin : 
            self.bNom = ''
        else :
            for nom in brassin :
                if nom.tag == 'NAME' :
                    self.bNom = nom.text




                    
        
        
        
        
        #Paliers

        self.nbrePaliers = len(paliers)
        self.liste_paliers = list()
        self.liste_pType = list()
        self.liste_pTime = list()
        self.liste_pTemp = list()
        self.liste_pQte = list()
        
        
        
        
        p = 0
        while p < self.nbrePaliers : 
            p = p+1
            for nom in paliers [p-1] :
                if nom.tag == 'NAME' :
                    self.pNom = nom.text
                    self.liste_paliers.append(self.pNom)    
                    
                if nom.tag == 'TYPE' :
                    self.pType = nom.text
                    self.liste_pType.append(self.pType)
                    
                if nom.tag == 'STEP_TIME' :
                    self.pTime = nom.text
                    self.liste_pTime.append(self.pTime)
                    
                if nom.tag == 'STEP_TEMP' :
                    self.pTemp = float(nom.text)
                    self.liste_pTemp.append(self.pTemp)
                    
        
                if nom.tag == 'INFUSE_AMOUNT' :
                    self.pQte = float(nom.text)
                    self.liste_pQte.append(self.pQte)   
        return AppWindow.nbreFer
                    
    def calculs_recette (self) :
        #Calculs sur les ingredients fermentescibles
        #GU = 383.89*equivSucre/volFinal *rendement
        #si extrait ou sucre ne pas tenir compte du rendement du brassage
        #OG = 1 + (GU/1000)
        
        self.liste_equivSucre = list()
        self.liste_equivSucreMashed = list()
        self.liste_equivSucreNonMashed = list()
        
        
        o = 0
        while o < AppWindow.nbreFer :
            o = o+1
            self.equivSucre = (self.liste_fAmount[o-1]/1000)*(self.liste_fYield[o-1]/100)
            #division par 1000 et 100 pour passer des g aux kg et parce que le rendement est un pourcentage
            self.liste_equivSucre.append(self.equivSucre)
            #for type in self.liste_fType [o-1] :
            if self.liste_fType [o-1] == 'Extract' or self.liste_fType [o-1] == 'Dry Extract' or self.liste_fType [o-1] == 'Sugar':
                self.liste_equivSucreNonMashed.append(self.equivSucre)
            else :
                self.liste_equivSucreMashed.append(self.equivSucre)
        
        self.GU= (383.89*sum(self.liste_equivSucreMashed)/float(self.volume))*((self.rendement)/100) + (383.89*sum(self.liste_equivSucreNonMashed)/float(self.volume))
        self.OG = 1+ (self.GU/1000)     
            


        
        #calcul de la FG. Si il y a plusieurs levures, on recupere l'attenuation la plus elevee.
        self.levureAttenDec = sorted (self.liste_levureAtten, reverse = True)
        if not self.levureAttenDec : 
            self.atten = 0.75
        if self.levureAttenDec :
            self.atten = self.levureAttenDec[0]/100
        
        self.GUF = self.GU*(1-self.atten)
        self.FG = 1 + self.GUF/1000
        
        
        #calcul des proportions pour les grains
        self.liste_fProportion = list()
        poidsTot = sum(self.liste_fAmount)  
        i = 0
        while i < AppWindow.nbreFer :
            i=i+1
            propGrain = (self.liste_fAmount[i-1] / poidsTot)*100
            self.liste_fProportion.append(propGrain)



        
        
        #calcul de l'amertume : methode de Tinseth
        #IBUs = decimal alpha acid utilization * mg/l of added alpha acids
        
        #mg/l of added alpha acids = decimal AA rating * grams hops * 1000 / liters of wort
        #Decimal Alpha Acid Utilization = Bigness Factor * Boil Time Factor
        #Bigness factor = 1.65 * 0.000125^(wort gravity - 1)
        #Boil Time factor = 1 - e^(-0.04 * time in mins) / 4.15
        self.liste_btFactor = list()
        self.liste_ibuPart = list()
        
        for time in self.liste_hTime :
            self.btFactor = (1 - 2.71828182845904523536**(-0.04 * time)) / 4.15
            self.liste_btFactor.append(self.btFactor)
            
        self.bignessFactor = 1.65 * (0.000125**(self.OG - 1))
        i = 0
        while i < len(self.liste_btFactor) :
            i = i+1
            self.aaUtil = self.liste_btFactor[i-1]*self.bignessFactor
            self.mgAA = (self.liste_hAlpha[i-1]/100)*self.liste_hAmount[i-1]*1000 / float(self.volume)
            if self.liste_hForm[i-1] == 'Pellet' :
                self.ibuPart = (self.mgAA * self.aaUtil) + 0.1*(self.mgAA * self.aaUtil)
            else :
                self.ibuPart = self.mgAA * self.aaUtil 
            self.liste_ibuPart.append(self.ibuPart)
            

        self.ibuTot = sum(self.liste_ibuPart)

        
        
        #calcul de la couleur
        #calcul du MCU pour chaque grain :
        #MCU=4.23*EBC(grain)*Poids grain(Kg)/Volume(L)
        #puis addition de tous les MCU
        #puis calcul EBC total :
        #EBC=2.939*MCU^0.6859
        self.liste_mcuPart = list()
        i = 0
        while i < AppWindow.nbreFer :
            i = i + 1
            self.mcuPart  = 4.23*self.liste_color[i-1]*(self.liste_fAmount[i-1]/1000)/float(self.volume)
            self.liste_mcuPart.append(self.mcuPart)
        self.mcuTot = sum(self.liste_mcuPart) 
        self.EBC = 2.939*(self.mcuTot**0.6859)

        
        #calcul ABV
        #ABV = 0.130((OG-1)-(FG-1))*1000
        
        self.ABV = 0.130*((self.OG-1) -(self.FG-1))*1000

            
        
            
        
        self.labelOGV.setText(str("%.3f" %(self.OG)))
        self.labelFGV.setText(str("%.3f" %(self.FG)))
        self.labelEBCV.setText(str("%.0f" %(self.EBC)))
        self.labelIBUV.setText(str("%.0f" %(self.ibuTot)))
        self.labelAlcv.setText(str("%.1f" %(self.ABV)) + '%')
        
        
                        
    def volPreCalc(self) :
        indice = float(self.volume) / self.doubleSpinBoxVolPre.value()       
        self.GUS = self.GU * indice
        self.SG = 1+ (self.GUS/1000) 
        self.labelSG.setText("%.3f" %self.SG)
        
        
    def ouvrir_clicked (self) : 
        
        
        self.s = QtGui.QFileDialog.getOpenFileName(self,
              self.trUtf8("Ouvrir un fichier"),
              "",
              )
        if not self.s :
            pass
        else :
            self.purge()
            self.importBeerXML()
            self.calculs_recette()
            self.MVC()
        

    
    def about(self) : 
        QtGui.QMessageBox.about(self,
                self.trUtf8("A propos"),
                self.trUtf8("<h1>JolieBulle</h1> <b>version 2.15</b><br/>copyright (c) 2010-2011 Pierre Tavares<p> JoliBulle est un logiciel de lecture et de formulation de recettes de brassage.</p><p><a href =http://www.gnu.org/licenses/gpl-3.0.html>Licence : Version 3 de la Licence Générale Publique GNU</a></p><p>Certaines icônes proviennent du pack Faenza par Tiheum (Matthieu James), également distribué sous licence GPL.</p>"))
        
            
    def rendemt_changed(self) :
        if self.checkBoxIng.isChecked() :
            ratio = self.rendement/self.doubleSpinBoxRendemt.value()
            
            i = 0
            while i < AppWindow.nbreFer :
                i = i +1 
                if self.liste_fType[i-1] == 'Extract' :
                    pass
                else :
                    self.liste_fAmount[i-1] = self.liste_fAmount[i-1] * ratio
                    amount = QtGui.QStandardItem("%.0f" %(self.liste_fAmount[i-1]))
                    self.modele.setItem(i-1,1,amount)
            self.rendement = self.doubleSpinBoxRendemt.value()
            self.calculs_recette()      
                    
        else :
            self.rendement = self.doubleSpinBoxRendemt.value()
            self.calculs_recette()
            
    def volume_changed(self) :
      
        if self.checkBoxIng.isChecked() :
            ratio = self.doubleSpinBox_2Volume.value()/float(self.volume)
            
            i = 0
            while i < AppWindow.nbreFer :
                i=i+1
                self.liste_fAmount[i-1] = self.liste_fAmount[i-1] * ratio
                self.volume = self.doubleSpinBox_2Volume.value()
                amount = QtGui.QStandardItem("%.0f" %(self.liste_fAmount[i-1]))
                self.modele.setItem(i-1,1,amount)
            
            h = 0
            while h < AppWindow.nbreHops :
                h = h + 1
                self.liste_hAmount[h-1] = self.liste_hAmount[h-1] * ratio
                self.volume = self.doubleSpinBox_2Volume.value()
                amount = QtGui.QStandardItem("%.3f" %(self.liste_hAmount[h-1]) )
                self.modele.setItem(i+h-1,1,amount)
            
            
            m = 0
            while m < AppWindow.nbreDivers :
                m = m + 1
                self.liste_dAmount[m-1] = self.liste_dAmount[m-1] * ratio
                self.volume = self.doubleSpinBox_2Volume.value()
                amount = QtGui.QStandardItem("%.0f" %(self.liste_dAmount[m-1]) )
                self.modele.setItem(i+h+m-1, 1, amount)
            
            self.calculs_recette()

        else :
            self.volume = self.doubleSpinBox_2Volume.value()
            self.calculs_recette()
        

    def enregistrer (self) :
        exp=Export()
        self.nomRecette = self.lineEditRecette.text()
        self.styleRecette = self.lineEditGenre.text()
        self.boil = self.spinBoxBoil.value()
        if not self.s : 
            self.enregistrerSous()
            
        else :

            
            exp.exportXML(self.nomRecette, self.styleRecette, self.volume, self.boil, self.rendement, AppWindow.nbreHops, self.liste_houblons, self.liste_hAmount, self.liste_hForm, self.liste_hTime, self.liste_hAlpha, AppWindow.nbreFer, self.fNom, self.fAmount ,self.fType, self.fYield, self.fMashed, self.color, self.liste_ingr, self.liste_fAmount, self.liste_fType, self.liste_fYield, self.liste_fMashed, self.liste_color, self.dNom, self.dAmount, self.dType, AppWindow.nbreDivers, self.liste_divers, self.liste_dAmount, self.liste_dType, self.nbreLevures, self.lNom, self.lForm, self.lLabo, self.lProd, self.lAtten, self.liste_levures, self.liste_lForm, self.liste_lLabo, self.liste_lProdid, self.liste_levureAtten)
            exp.enregistrer(self.s)
    
        
    def enregistrerSous (self) :
        exp=Export()
        self.nomRecette = self.lineEditRecette.text()  
        self.styleRecette = self.lineEditGenre.text()
        self.boil = self.spinBoxBoil.value()
        self.s = QtGui.QFileDialog.getSaveFileName (self,
                                                    self.trUtf8("Enregistrer dans un fichier"),
                                                    self.nomRecette,
                                                    "BeerXML (*.xml)")
        exp.exportXML(self.nomRecette, self.styleRecette, self.volume, self.boil, self.rendement, AppWindow.nbreHops, self.liste_houblons, self.liste_hAmount, self.liste_hForm, self.liste_hTime, self.liste_hAlpha, AppWindow.nbreFer, self.fNom, self.fAmount ,self.fType, self.fYield, self.fMashed, self.color, self.liste_ingr, self.liste_fAmount, self.liste_fType, self.liste_fYield, self.liste_fMashed, self.liste_color, self.dNom, self.dAmount, self.dType, AppWindow.nbreDivers, self.liste_divers, self.liste_dAmount, self.liste_dType, self.nbreLevures, self.lNom, self.lForm, self.lLabo, self.lProd, self.lAtten, self.liste_levures, self.liste_lForm, self.liste_lLabo, self.liste_lProdid, self.liste_levureAtten)
        exp.enregistrer(self.s)  
    def exporterHtml (self) :
        self.nomRecette = self.lineEditRecette.text()
        self.styleRecette = self.lineEditGenre.text()
        
        exp = ExportHTML()
        self.h = QtGui.QFileDialog.getSaveFileName (self,
                                                    self.trUtf8("Enregistrer dans un fichier"),
                                                    self.nomRecette,
                                                    "HTML (*.html)")    
        
        self.fileHtml = QtCore.QFile(self.h)
        exp.exportHtml(self.nomRecette,self.styleRecette, self.volume, self.boil, AppWindow.nbreFer, self.liste_ingr, self.liste_fAmount, AppWindow.nbreHops, self.liste_houblons, self.liste_hAlpha, self.liste_hForm, self.liste_hAmount, self.liste_hTime, AppWindow.nbreDivers, self.liste_divers, self.liste_dType, self.liste_dAmount, self.nbreLevures, self.liste_levuresDetail,self.rendement, self.OG, self.FG, self.EBC, self.ibuTot ,self.ABV)
        
        exp.enregistrerHtml(self.fileHtml)
    
    def modifierStyle (self) :
        if self.pushButtonChangerStyle.isChecked () :
            self.comboBoxStyle.show()
        else :
               self.comboBoxStyle.hide()   

    def volMore (self) :
        if self.pushButtonVolMore.isChecked() :
            self.widgetVol.show()
        else :
            self.widgetVol.hide()

               
    def nouvelle(self) :
        
        self.nomRecette = self.trUtf8('Nouvelle Recette')
        self.rendement = 75
        self.volume = '10'
        self.boil = '60'
        self.styleRecette = self.trUtf8('''Générique''')
        
        
        
        #AppWindow.nbreFer = 0
        self.liste_ingr = list()
        self.liste_fAmount = list()
        self.liste_fType = list()
        self.liste_fYield = list()
        self.liste_fMashed = list()
        self.liste_color = list()
        self.fMashed = ''
        self.fNom = ''
        self.fAmount = 0
        self.fType = ''
        self.fYield = 0
        self.color = 0
        
        #AppWindow.nbreHops = 0
        self.liste_houblons = list()
        self.liste_hAmount = list()
        self.liste_hForm = list()
        self.liste_hTime = list()
        self.liste_hAlpha = list()
        
        self.nbreLevures = 0
        self.liste_levures = list()
        self.liste_lForm = list()
        self.liste_lLabo = list()
        self.liste_lProdid = list()
        self.liste_levuresDetail = list()
        self.liste_levureAtten = list ()
        self.lNom = ""
        self.lLabo =""
        self.lProd =""
        self.lForm = ""
        self.lAtten=""
        
        #AppWindow.nbreDivers = 0
        self.liste_divers = list ()
        self.liste_dAmount = list ()
        self.liste_dType = list ()
        self.dNom = ''
        self.dAmount = 0
        self.dType = ''
        
        self.lineEditRecette.setText(self.nomRecette)
        self.lineEditGenre.setText(self.styleRecette)
        self.doubleSpinBox_2Volume.setValue(float(self.volume))
        self.doubleSpinBoxRendemt.setValue(self.rendement)
        try : 
            self.spinBoxBoil.setValue(float(self.boil))
        except :
            self.spinBoxBoil.setValue (0)
            
        
        
            
    def addStyle(self) :
        self.lineEditGenre.setText(self.comboBoxStyle.currentText())
        
        
    def printRecipe (self) :
        printer=QtGui.QPrinter()
        info_texte = "<h1 style=\"font-family : Arial ;\">%s</h1> <br/>\
                    <b>Style :</b> %s <br/> \
                    <b>Volume :</b> %sL<b> ; Rendement :</b> %s%% <br/>\
                    <h2>Liste des ingrédients</h2> "  \
                    %(self.nomRecette, self.styleRecette, self.volume, self.rendement)
        
        grains_texte = "<h3 style =\" text-decoration : underline; \">Grains ou extraits</h3>"           
        i = 0
        while i < AppWindow.nbreFer :
            i=i+1
            grains_texte = grains_texte + "<b>"+ self.liste_ingr[i-1] + " : " + "</b>"+ str(self.liste_fAmount[i-1]) + "g" + "<br/>"
        
        houblons_texte = "<h3 style =\" text-decoration : underline; \">Houblons</h3>"
        h = 0
        while h < AppWindow.nbreHops : 
            h = h+1        
            houblons_texte = houblons_texte + "<b>" + self.liste_houblons[h-1] + "</b>" +  " (" +  str(self.liste_hAlpha[h-1]) +"%" + ", " + self.liste_hForm[h-1] +")" + " : " +"<b>"+ str(self.liste_hAmount[h-1]) + "g"+"</b>" +" pendant " +"<b>" +str(self.liste_hTime[h-1]) +"</b>"+ " minutes" + "<br/>"
        
        divers_texte = "<h3 style =\" text-decoration : underline; \">Divers</h3>"
        m = 0
        while  m < AppWindow.nbreDivers :
            m = m + 1    
            divers_texte = divers_texte +"<b>" +self.liste_divers[m-1] +"</b>"+" (" +self.liste_dType[m-1] +")" + " : " +"<b>" +str(self.liste_dAmount[m-1]) + "g" +"</b>"+"<br/>"
           
        levures_texte = "<h3 style =\" text-decoration : underline; \">Levures</h3>" 
        l = 0
        while l < self.nbreLevures : 
            l = l+1
            levures_texte = levures_texte + self.liste_levuresDetail[l-1] + "<br/>"
           
        texte = info_texte + grains_texte + houblons_texte + divers_texte + levures_texte
        doc=QtGui.QTextDocument()

        doc.setHtml(texte)

            
        
        dialog = QtGui.QPrintDialog(printer)
        dialog.setModal(True)
        dialog.setWindowTitle("Print Document" )
        # dialog.addEnabledOption(QAbstractPrintDialog.PrintSelection)
        if dialog.exec_() == True:
            doc.print_(printer)
       
        
        

if __name__ == "__main__":

    QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("utf-8"))
    app = QtGui.QApplication(sys.argv)
    
    locale = QtCore.QLocale.system().name()
    translator=QtCore.QTranslator ()
    #~ translator.load(("qt_") +locale, QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath))
    translator.load('joliebulle_' + locale)
    app.installTranslator(translator)
    
        
    main_window = AppWindow()
    main_window.show()

    app.exec_()
