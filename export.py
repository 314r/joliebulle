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




import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import xml.etree.ElementTree as ET
from xml.dom import minidom
import model.constants

class Export (QtCore.QObject):
    def prettify(self,elem):

        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")
        
    def exportXML(self,recipe) :
        self.recipes = ET.Element('RECIPES')
        recipeTag = ET.SubElement(self.recipes, 'RECIPE')
        name = ET.SubElement(recipeTag, 'NAME')
        name.text = recipe.name
        version = ET.SubElement(recipeTag, 'VERSION')
        version.text = "1"
        type = ET.SubElement(recipeTag, 'TYPE')
        if recipe.type == model.constants.RECIPE_TYPE_ALL_GRAIN:
            type.text = "All Grain"
        elif recipe.type == mode.constants.RECIPE_TYPE_EXTRACT:
            type.text = "Extract"
        elif recipe.type == mode.constants.RECIPE_PARTIAL_MASH:
            type.text = "Partial Mash"
        brewerR = ET.SubElement(recipeTag, 'BREWER')
        brewerR.text = recipe.brewer
        
        
        style = ET.SubElement(recipeTag, 'STYLE')
        sNom = ET.SubElement(style, 'NAME')
        sNom.text = recipe.style
        sVersion = ET.SubElement(style, 'VERSION')
        sVersion.text = '1'
        sCategory = ET.SubElement(style, 'CATEGORY')
        sCategoryNumber = ET.SubElement (style, 'CATEGORY_NUMBER')
        sStyleLetter = ET.SubElement (style, 'STYLE_LETTER')
        sStyleGuide = ET.SubElement (style, 'STYLE_GUIDE')
        sType =ET.SubElement(style, 'TYPE')
        sType.text = 'Ale'
        sOgMin = ET.SubElement (style, 'OG_MIN')
        sOgMax = ET.SubElement (style, 'OG_MAX')
        sFgMin = ET.SubElement (style, 'FG_MIN')
        sFgMax = ET.SubElement (style, 'FG_MAX')
        sIbuMin = ET.SubElement (style, 'IBU_MIN')
        sIbuMax = ET.SubElement (style, 'IBU_MAX')
        sColorMin = ET.SubElement (style, 'COLOR_MIN')
        sColorMax = ET.SubElement (style, 'COLOR_MAX')
        
        
        batch_size = ET.SubElement(recipeTag, 'BATCH_SIZE')
        batch_size.text = str(recipe.volume)
        boil_size = ET.SubElement(recipeTag, 'BOIL_SIZE')
        boil_time = ET.SubElement(recipeTag, 'BOIL_TIME')
        boil_time.text = str(recipe.boil)
        efficiency = ET.SubElement(recipeTag, 'EFFICIENCY')
        efficiency.text = str(recipe.efficiency)
        originalGravity = ET.SubElement(recipeTag, 'OG')
        originalGravity.text = str(recipe.compute_OG())
        finalGravity = ET.SubElement(recipeTag, 'FG')
        finalGravity.text = str(recipe.compute_FG())
        
        hops = ET.SubElement(recipeTag, 'HOPS')
        for h in recipe.listeHops:
            hop = ET.SubElement(hops, 'HOP')
            hNom = ET.SubElement(hop, 'NAME')
            hVersion = ET.SubElement(hop, 'VERSION')
            hVersion.text = '1'
            hNom.text = h.name
            hAmount = ET.SubElement(hop, 'AMOUNT')
            hAmount.text = str(h.amount/1000)
            hForm = ET.SubElement(hop, 'FORM')
            if h.form == model.constants.HOP_FORM_LEAF:
                hForm.text = 'Leaf'
            elif h.form == model.constants.HOP_FORM_PELLET:
                hForm.text = 'Pellet'
            elif h.form == model.constants.HOP_FORM_PLUG:
                hForm.text = 'Plug'   
                
            hTime = ET.SubElement(hop, 'TIME')
            hTime.text = str(h.time)
            hAlpha = ET.SubElement(hop, 'ALPHA')
            hAlpha.text = str(h.alpha)
            hUse = ET.SubElement(hop, 'USE')
            if h.use == model.constants.HOP_USE_BOIL :
                hUse.text = 'Boil'
            if h.use == model.constants.HOP_USE_DRY_HOP :
                hUse.text = 'Dry Hop'  
            if h.use == model.constants.HOP_USE_MASH :
                hUse.text = 'Mash'
            if h.use == model.constants.HOP_USE_FIRST_WORT :
                hUse.text = 'First Wort' 
            if h.use == model.constants.HOP_USE_AROMA :
                hUse.text = 'Aroma'  
            else :
                hUse.text = 'Boil'

        fermentables = ET.SubElement(recipeTag, 'FERMENTABLES')
        for f in recipe.listeFermentables:
            fermentables.append(f.toXml())
            
        miscs = ET.SubElement(recipeTag, 'MISCS')
        for m in recipe.listeMiscs:
            misc = ET.SubElement(miscs, 'MISC')
            dNom = ET.SubElement(misc, 'NAME')
            dNom.text = m.name
            dVersion = ET.SubElement(misc, 'VERSION')
            dVersion.text = '1'
            dAmount = ET.SubElement(misc, 'AMOUNT')
            dAmount.text = str(m.amount/1000)
            dType = ET.SubElement(misc, 'TYPE')
            dType.text = m.type
            dTime = ET.SubElement(misc, 'TIME')
            dTime.text = str(m.time)
            dUse = ET.SubElement(misc, 'USE')
            if m.use == model.constants.MISC_USE_BOIL :
                dUse.text = 'Boil'
            if m.use == model.constants.MISC_USE_MASH :
                dUse.text = 'Mash'
            if m.use == model.constants.MISC_USE_PRIMARY :
                dUse.text = 'Primary'        
            if m.use == model.constants.MISC_USE_SECONDARY :
                dUse.text = 'Secondary'
            if m.use == model.constants.MISC_USE_BOTTLING :
                dUse.text = 'Bottling'       
            else :
                dUse.text = 'Boil'
        
        yeasts=ET.SubElement(recipeTag, 'YEASTS')  
        for y in recipe.listeYeasts :
            yeast = ET.SubElement(yeasts, 'YEAST')
            lNom = ET.SubElement(yeast, 'NAME')
            lVersion = ET.SubElement(yeast, 'VERSION')
            lVersion.text = '1'
            lType = ET.SubElement(yeast ,'TYPE')
            lType = 'Ale'
            lNom.text = y.name
            lForm = ET.SubElement(yeast, 'FORM')
            lForm.text = y.form
            lLabo = ET.SubElement(yeast, 'LABORATORY')
            lLabo.text = y.labo
            lProd = ET.SubElement(yeast, 'PRODUCT_ID')
            lProd.text = y.productId
            lAtten = ET.SubElement(yeast, 'ATTENUATION')
            lAtten.text = str(y.attenuation)
            
        waters=ET.SubElement(recipeTag, 'WATERS')
        
        mash=ET.SubElement(recipeTag, 'MASH') 
        mName = ET.SubElement(mash, 'NAME')
        mName.text = recipe.mash.name
        mVersion = ET.SubElement(mash, 'VERSION')
        mVersion.text = '1'
        mGrainTemp = ET.SubElement(mash, 'GRAIN_TEMP')
        mGrainTemp.text = str(recipe.mash.grainTemp)
        mTunTemp = ET.SubElement(mash, 'TUN_TEMP')
        mTunTemp.text = str(recipe.mash.tunTemp)
        mSpargeTemp = ET.SubElement(mash, 'SPARGE_TEMP')
        mSpargeTemp.text = str(recipe.mash.spargeTemp)
        mPh = ET.SubElement(mash, 'PH')
        mPh.text = str(recipe.mash.ph)
        mSteps = ET.SubElement(mash, 'MASH_STEPS')
        
        for s in recipe.mash.listeSteps:
            mashStep =ET.SubElement(mSteps, 'MASH_STEP')           
            stepName = ET.SubElement(mashStep, 'NAME')
            stepName.text = s.name
            stepVersion = ET.SubElement(mashStep, 'VERSION')
            stepVersion.text = '1'
            stepType = ET.SubElement(mashStep, 'TYPE')
            stepType.text = s.type
            stepTime = ET.SubElement(mashStep, 'STEP_TIME')
            stepTime.text = str(s.time)
            stepTemp = ET.SubElement(mashStep, 'STEP_TEMP')
            stepTemp.text = str(s.temp)
            stepVol = ET.SubElement(mashStep, 'INFUSE_AMOUNT')
            stepVol.text = str(s.infuseAmount)

        try :
            notes = ET.SubElement(recipeTag, 'NOTES') 
            notes.text = self.recipe.recipeNotes
        except :
            pass       


    def enregistrer(self,s) :
       # print (ET.tostring(self.recipes))
        
        ET.ElementTree(self.recipes).write(s,encoding="utf-8")
        


