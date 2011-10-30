#!/usr/bin/python3
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
import xml.etree.ElementTree as ET
from xml.dom import minidom


  

class Export :
    
    
    def prettify(self,elem):

        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
        


    
    def exportXML(self,nomRecette, styleRecette, typeRecette, brewer, volume, boil, rendement, OG, FG, nbreHops, liste_houblons,
liste_hAmount, liste_hForm, liste_hTime, liste_hAlpha, nbreFer, fNom, fAmount,
fType, fYield, fMashed, color, liste_ingr, liste_fAmount, liste_fType,
liste_fYield, liste_fMashed, liste_color, dNom, dAmount, dType, nbreDivers, liste_divers, liste_dAmount, liste_dType, nbreLevures, lNom, lForm, lLabo, lProd, lAtten, liste_levures, liste_lForm, liste_lLabo, liste_lProdid, liste_levureAtten) :

        self.recipes = ET.Element('RECIPES')
        recipe = ET.SubElement(self.recipes, 'RECIPE')
        name = ET.SubElement(recipe, 'NAME')
        name.text = nomRecette
        version = ET.SubElement(recipe, 'VERSION')
        version.text = "1"
        type = ET.SubElement(recipe, 'TYPE')
        type.text = typeRecette
        brewerR = ET.SubElement(recipe, 'BREWER')
        brewerR.text = brewer
        style = ET.SubElement(recipe, 'STYLE')
        sNom = ET.SubElement(style, 'NAME')
        sNom.text = styleRecette
        batch_size = ET.SubElement(recipe, 'BATCH_SIZE')
        batch_size.text = str(volume)
        boil_size = ET.SubElement(recipe, 'BOIL_SIZE')
        boil_time = ET.SubElement(recipe, 'BOIL_TIME')
        boil_time.text = str(boil)
        efficiency = ET.SubElement(recipe, 'EFFICIENCY')
        efficiency.text = str(rendement)
        originalGravity = ET.SubElement(recipe, 'OG')
        originalGravity.text = str(OG)
        finalGravity = ET.SubElement(recipe, 'FG')
        finalGravity.text = str(FG)
        
        hops = ET.SubElement(recipe, 'HOPS')
        i=0
        while i < nbreHops :
            i = i+1
            hop = ET.SubElement(hops, 'HOP')
            hNom = ET.SubElement(hop, 'NAME')
            hNom.text = liste_houblons[i-1]
            hAmount = ET.SubElement(hop, 'AMOUNT')
            hAmount.text = str(liste_hAmount[i-1]/1000)
            hForm = ET.SubElement(hop, 'FORM')
            hForm.text = str(liste_hForm[i-1])
            hTime = ET.SubElement(hop, 'TIME')
            hTime.text = str(liste_hTime[i-1])
            hAlpha = ET.SubElement(hop, 'ALPHA')
            hAlpha.text = str(liste_hAlpha[i-1])

        fermentables = ET.SubElement(recipe, 'FERMENTABLES')
        
        i = 0
        while i < nbreFer :
            i = i+1
            fermentable = ET.SubElement(fermentables, 'FERMENTABLE')
            fNom = ET.SubElement(fermentable,'NAME')
            fNom.text = liste_ingr[i-1]
            fAmount = ET.SubElement(fermentable, 'AMOUNT')
            fAmount.text = str(liste_fAmount[i-1]/1000)
            fType = ET.SubElement(fermentable, 'TYPE')
            fType.text = liste_fType[i-1]
            fYield = ET.SubElement(fermentable,'YIELD')
            fYield.text = str(liste_fYield[i-1])
             
            fMashed = ET.SubElement(fermentable,'RECOMMEND_MASH')
            if not liste_fMashed :
                pass
            else :
                fMashed.text = liste_fMashed[i-1]

            color = ET.SubElement(fermentable, 'COLOR')
            color.text = str(liste_color[i-1]/1.97)
            
        miscs = ET.SubElement(recipe, 'MISCS')
        i = 0
        while i < nbreDivers :
            i = i+1
            misc = ET.SubElement(miscs, 'MISC')
            dNom = ET.SubElement(misc, 'NAME')
            dNom.text = liste_divers[i-1]
            dAmount = ET.SubElement(misc, 'AMOUNT')
            dAmount.text = str(liste_dAmount[i-1]/1000)
            dType = ET.SubElement(misc, 'TYPE')
            dType.text = liste_dType[i-1]
        
        yeasts=ET.SubElement(recipe, 'YEASTS')  
        i = 0  
        while i < nbreLevures :
            i = i+1
            yeast = ET.SubElement(yeasts, 'YEAST')
            lNom = ET.SubElement(yeast, 'NAME')
            lNom.text = liste_levures [i-1]
            lForm = ET.SubElement(yeast, 'FORM')
            lForm.text = liste_lForm[i-1]
            lLabo = ET.SubElement(yeast, 'LABORATORY')
            lLabo.text = liste_lLabo[i-1]
            lProd = ET.SubElement(yeast, 'PRODUCT_ID')
            lProd.text = liste_lProdid[i-1]
            lAtten = ET.SubElement(yeast, 'ATTENUATION')
            lAtten.text = str(liste_levureAtten[i-1])
            
        
        #print (ET.tostring(recipes))
        #print (self.prettify(recipes))
        #ET.ElementTree(recipes).write(file=None)
        
        #self.enregistrer()
    def enregistrer(self,s) :
       # print (ET.tostring(self.recipes))
        
        ET.ElementTree(self.recipes).write(s,encoding="utf-8")

