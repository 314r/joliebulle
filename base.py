#!/usr/bin/python3.1
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




import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import xml.etree.ElementTree as ET
from globals import *



class ImportBase : 


    def importBeerXML(self) :
        fichierBeerXML = database_file
        arbre = ET.parse(fichierBeerXML)

        presentation=arbre.find('.//RECIPE')
        fermentables=arbre.findall('.//FERMENTABLE')
        hops = arbre.findall('.//HOP')
        levures = arbre.findall('.//YEAST')
        misc = arbre.findall('.//MISC')
 
               
        
        #Ingredient fermentescibles
        self.nbreFer = len(fermentables)
        self.liste_ingr = list()
        self.liste_fAmount = list()
        self.liste_fType = list()
        self.liste_fYield = list()
        self.liste_fMashed = list()
        self.liste_color = list()
        self.fMashed = ''
        
        
        i = 0
        while i < self.nbreFer :

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
        
        self.nbreHops = len(hops)
        self.liste_houblons = list()
        self.liste_hAmount = list()
        self.liste_hForm = list()
        self.liste_hTime = list()
        self.liste_hAlpha = list()
        
        
        
        h = 0
        while h < self.nbreHops : 
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
