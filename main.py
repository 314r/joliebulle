#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­



#BeerReader
#Copyright (C) 2010 Pierre Tavares

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
from reader import *
from recette import *
from export import *


import xml.etree.ElementTree as ET



class AmountDelegate(QtGui.QItemDelegate):
    def __init__(self, parent=None):
            QtGui.QItemDelegate.__init__(self, parent)



    def createEditor(self, parent, option, index) :
        self.listeF = AppWindow()
        i=self.listeF.nbreFer
        h=self.listeF.nbreHops

        row=index.row()
        if row < i+h:
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
        
        #model.setData(index, QtCore.QVariant(value))
        model.setData(index, value)
        
        
        
        
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
        
        #model.setData(index, QtCore.QVariant(value))
        model.setData(index, value)
                            
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class AppWindow(QtGui.QMainWindow,Ui_MainWindow):

    nbreFer=0
    nbreHops=0
    
        
        
  
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        #calculs = Calculs()
        
        
        
        #Les connections
        self.connect(self.actionOuvrir, QtCore.SIGNAL("triggered()"), self.ouvrir_clicked)
        self.connect(self.actionAbout, QtCore.SIGNAL("triggered()"), self.about)
        self.connect(self.doubleSpinBoxRendemt, QtCore.SIGNAL("valueChanged(QString)"), self.rendemt_changed)
        self.connect(self.doubleSpinBox_2Volume, QtCore.SIGNAL("valueChanged(QString)"), self.volume_changed)
        self.connect(self.pushButtonEssai, QtCore.SIGNAL("clicked()"), self.enregistrer)
        
        
        #Les modeles et vues du widget central
        self.modele = QtGui.QStandardItemModel(0, 4)
        self.connect(self.modele, QtCore.SIGNAL("dataChanged(QModelIndex,QModelIndex)"), self.reverseMVC)
        liste_headers = ["Ingrédients","Quantité","Temps","Acide Alpha"]
        self.modele.setHorizontalHeaderLabels(liste_headers)
        
        self.deleg = AmountDelegate(self)
        self.tableViewF.setItemDelegateForColumn(1,self.deleg)
        
        self.delegT = TimeDelegate(self)
        self.tableViewF.setItemDelegateForColumn(2,self.delegT)

        self.delegA = AlphaDelegate(self)
        self.tableViewF.setItemDelegateForColumn(3,self.delegA)     

        self.tableViewF.setModel(self.modele)
        self.tableViewF.setColumnWidth(0,250)
        
        #self.tableViewF.setEditTriggers(QtGui.QAbstractItemView.CurrentChanged)
        
        #self.modeleP = QtGui.QStandardItemModel(1, 5)
        #self.tableViewB.setModel(self.modeleP)
        
        #liste_headersMash = ["Palier","Type","Temps","Température","Quantité"]
        #self.modeleP.setHorizontalHeaderLabels(liste_headersMash)

    #cette fonction est appelee chaque fois que des donnees du modele changent
    def reverseMVC(self) : 
    
        
        
        i = 0
        while i < AppWindow.nbreFer :
            i = i+1
            
            index = self.modele.index(i-1,1)
            value = self.modele.data(index, QtCore.Qt.DisplayRole)
            self.liste_fAmount[i-1] = float(value)

            
            
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

            
        print (self.liste_hAlpha)
        self.calculs_recette()  
        

        
        
    def MVC(self) : 
        #recette.labelRecetteV.setText(recette.nomRecette)
        
        

        
        i=0
        while i < AppWindow.nbreFer :
            i=i+1
            for item in self.liste_ingr : 
                item = QtGui.QStandardItem(self.liste_ingr[i-1])
                self.modele.setItem(i-1,0,item)
            for amount in self.liste_fAmount : 
                amount = QtGui.QStandardItem("%.0f" %(self.liste_fAmount[i-1]))
                self.modele.setItem(i-1,1,amount)

        
        

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



                
        m = 0
        while m < self.nbreDivers :
            m = m+1
            for item in self.liste_divers :
                item = QtGui.QStandardItem(self.liste_divers[m-1] + ' [' +self.liste_dType[m-1] + ']')
                self.modele.setItem(i+h+m-1, 0, item)
                
            for item in self.liste_dAmount : 
                  amount = QtGui.QStandardItem("%.0f" %(self.liste_dAmount[m-1]) )
                  self.modele.setItem(i+h+m-1, 1, amount)



        l=0
        while l < self.nbreLevures : 
            l=l+1
            for item in self.liste_levuresDetail : 
                item = QtGui.QStandardItem(self.liste_levuresDetail[l-1])
                self.modele.setItem( i+h+l-1,0,item)
                
                
                
        

        
        
        #p = 0
        #while p < self.nbrePaliers :
            #p = p+1
            #for item in self.liste_paliers : 
            #   item = QtGui.QStandardItem(self.liste_paliers[p-1])
            #   self.modeleP.setItem( p-1,0,item)
            #for pType in self.liste_pType : 
            #   pType = QtGui.QStandardItem(self.liste_pType[p-1])
            #   self.modeleP.setItem( p-1,1,pType)  
            #for pTime in self.liste_pTime : 
            #   pTime = QtGui.QStandardItem(self.liste_pTime[p-1] + ' min')
            #   self.modeleP.setItem( p-1,2,pTime)
            #for pTemp in self.liste_pTemp : 
            #   pTemp = QtGui.QStandardItem("%.0f" %(self.liste_pTemp[p-1]) + ' °C')
            #   self.modeleP.setItem( p-1,3,pTemp)              
            #for pQte in self.liste_pQte : 
            #   pQte = QtGui.QStandardItem("%.1f"%(self.liste_pQte[p-1]) + ' l')
            #   self.modeleP.setItem( p-1,4,pQte)   


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


    
        self.labelRecetteV.setText(self.nomRecette)
        self.labelGenreV.setText(self.styleRecette)
        self.doubleSpinBox_2Volume.setValue(float(self.volume))
        self.doubleSpinBoxRendemt.setValue(self.rendement)
        try : 
            self.spinBoxBoil.setValue(float(self.boil))
        except :
            self.spinBoxBoil.setValue (0)
    
    
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
                    
                    
                    
            self.liste_levuresDetail.append (self.lLabo +' ' + self.lProd +' ' + self.lNom)
                    
                    
                    
        
        
        
        #Ingredients divers
        self.nbreDivers = len(misc)
        self.liste_divers = list ()
        self.liste_dAmount = list ()
        self.liste_dType = list ()
        self.dNom = ''
        self.dAmount = 0
        self.dType = ''
        
        
        m = 0
        while  m < self.nbreDivers :
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


        #self.labelBrassageV.setText(self.bNom)

                    
        
        
        
        
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
        #si RECOMMAND_MASH = False ne pas tenir compte du rendement du brassage
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
            if self.liste_fType [o-1] == 'Extract' :
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
                        
        
        
    
        
        
        
        
        
    def ouvrir_clicked (self) : 
        
        self.s = QtGui.QFileDialog.getOpenFileName(self,
              "Ouvrir un fichier",
              "",
              )
        

        self.importBeerXML()
        self.calculs_recette()
        self.MVC()
        
        recette=Recette()
        print (recette.toto)
    
    def about(self) : 
        QtGui.QMessageBox.about(self,
                self.trUtf8("A propos"),
                self.trUtf8("<h1>JolieBulle</h1> <b>version 1.0</b><br/>copyright (c) 2010 Pierre Tavares<p> JoliBulle est une liseuse de recettes au format BeerXML.</p><p><a href =http://www.gnu.org/licenses/gpl-3.0.html>Licence : Version 3 de la Licence Générale Publique GNU</a></p><p>Certaines icônes proviennent du pack Faenza par Tiheum (Matthieu James), également distribué sous licence GPL.</p>"))
        
            
    def rendemt_changed(self) :
      
        if not self.s :
            pass
        else :
            print("toto")
            self.rendement = self.doubleSpinBoxRendemt.value()
            print(self.rendement)
            self.calculs_recette()
            
    def volume_changed(self) :
      
        if not self.s :
            pass
              
        else :
            self.volume = self.doubleSpinBox_2Volume.value()
            self.calculs_recette()
        
    def plus_dix(self) :

        if not self.s :
            pass

        else :
            self.liste_fAmount[1] = self.liste_fAmount[1] + 10
            self.MVC()
            self.calculs_recette()
        

    def enregistrer (self) :
        exp=Export()
        exp.exportXML(self.nomRecette, self.styleRecette, self.volume, self.boil, self.rendement, AppWindow.nbreHops, self.liste_houblons, self.liste_hAmount, self.liste_hForm, self.liste_hTime, self.liste_hAlpha, AppWindow.nbreFer, self.fNom, self.fAmount ,self.fType, self.fYield, self.fMashed, self.color, self.liste_ingr, self.liste_fAmount, self.liste_fType, self.liste_fYield, self.liste_fMashed, self.liste_color, self.dNom, self.dAmount, self.dType, self.nbreDivers, self.liste_divers, self.liste_dAmount, self.liste_dType, self.nbreLevures, self.lNom, self.lForm, self.lLabo, self.lProd, self.lAtten, self.liste_levures, self.liste_lForm, self.liste_lLabo, self.liste_lProdid, self.liste_levureAtten)
        exp.enregistrer(self.s)

    
        
        
    







if __name__ == "__main__":

    QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("utf-8"))
    app = QtGui.QApplication(sys.argv)

    main_window = AppWindow()
    main_window.show()

    app.exec_()
