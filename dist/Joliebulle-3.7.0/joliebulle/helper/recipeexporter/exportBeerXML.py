#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.6
#Copyright (C) 2010-2016 Pierre Tavares
#Copyright (C) 2012-2015 joliebulle's authors

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


import xml.etree.ElementTree as ET
from model.constants import *

def exportBeerXML(recipe):
    recipes = ET.Element('RECIPES')
    recipeTag = ET.SubElement(recipes, 'RECIPE')
    name = ET.SubElement(recipeTag, 'NAME')
    name.text = recipe.name
    version = ET.SubElement(recipeTag, 'VERSION')
    version.text = "1"
    type = ET.SubElement(recipeTag, 'TYPE')
    if recipe.type == RECIPE_TYPE_ALL_GRAIN:
        type.text = "All Grain"
    elif recipe.type == RECIPE_TYPE_EXTRACT:
        type.text = "Extract"
    elif recipe.type == RECIPE_TYPE_PARTIAL_MASH:
        type.text = "Partial Mash"
    brewerR = ET.SubElement(recipeTag, 'BREWER')
    brewerR.text = recipe.brewer

    style = ET.SubElement(recipeTag, 'STYLE')
    sNom = ET.SubElement(style, 'NAME')
    sNom.text = recipe.style
    sVersion = ET.SubElement(style, 'VERSION')
    sVersion.text = '1'
    sCategory = ET.SubElement(style, 'CATEGORY')
    sCategoryNumber = ET.SubElement(style, 'CATEGORY_NUMBER')
    sStyleLetter = ET.SubElement(style, 'STYLE_LETTER')
    sStyleGuide = ET.SubElement(style, 'STYLE_GUIDE')
    sType = ET.SubElement(style, 'TYPE')
    sType.text = 'Ale'
    sOgMin = ET.SubElement(style, 'OG_MIN')
    sOgMax = ET.SubElement(style, 'OG_MAX')
    sFgMin = ET.SubElement(style, 'FG_MIN')
    sFgMax = ET.SubElement(style, 'FG_MAX')
    sIbuMin = ET.SubElement(style, 'IBU_MIN')
    sIbuMax = ET.SubElement(style, 'IBU_MAX')
    sColorMin = ET.SubElement(style, 'COLOR_MIN')
    sColorMax = ET.SubElement(style, 'COLOR_MAX')

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
        # hops.append(h.toXml())
        hop = ET.SubElement(hops, 'HOP')
        hNom = ET.SubElement(hop, 'NAME')
        hNom.text = h.name
        hVersion = ET.SubElement(hop, 'VERSION')
        hVersion.text = '1'
        hAmount = ET.SubElement(hop, 'AMOUNT')
        hAmount.text = str(h.amount/1000)
        hForm = ET.SubElement(hop, 'FORM')
        if h.form == HOP_FORM_PELLET :
            hForm.text = 'Pellet'
        elif h.form == HOP_FORM_LEAF :
            hForm.text = 'Leaf'
        elif h.form == HOP_FORM_PLUG :
            hForm.text = 'Plug'
        hTime = ET.SubElement(hop, 'TIME')
        hTime.text = str(h.time)
        hAlpha = ET.SubElement(hop, 'ALPHA')
        hAlpha.text = str(h.alpha)
        hUse = ET.SubElement(hop, 'USE')
        hUse.text = h.use
        
        

    fermentables = ET.SubElement(recipeTag, 'FERMENTABLES')
    for f in recipe.listeFermentables:
        # fermentables.append(f.toXml())
        fermentable = ET.SubElement(fermentables, 'FERMENTABLE')
        fName = ET.SubElement(fermentable,'NAME')
        fName.text = f.name
        fVersion = ET.SubElement(fermentable, 'VERSION')
        fVersion.text = '1'            
        fAmount = ET.SubElement(fermentable, 'AMOUNT')
        fAmount.text = str(f.amount/1000)
        fType = ET.SubElement(fermentable, 'TYPE')
        fType.text = f.type
        fYield = ET.SubElement(fermentable,'YIELD')
        fYield.text = str(f.fyield)
        fMashed = ET.SubElement(fermentable,'RECOMMEND_MASH')
        if f.recommendMash:
            fMashed.text = 'TRUE'
        else:
            fMashed.text = 'FALSE'
        fUse = ET.SubElement(fermentable,'ADD_AFTER_BOIL')
        if f.useAfterBoil : 
            fUse.text = 'TRUE'
        else :
            fUse.text = 'FALSE'
        color = ET.SubElement(fermentable, 'COLOR')
        color.text = str(f.color/1.97)

    miscs = ET.SubElement(recipeTag, 'MISCS')
    for m in recipe.listeMiscs:
        # miscs.append(m.toXml())
        misc = ET.SubElement(miscs, 'MISC')
        mName = ET.SubElement(misc, 'NAME')
        mName.text = m.name
        mVersion = ET.SubElement(misc, 'VERSION')
        mVersion.text = '1'
        mAmount = ET.SubElement(misc, 'AMOUNT')
        mAmount.text = str(m.amount/1000)
        mType = ET.SubElement(misc, 'TYPE')
        mType.text = m.type
        mTime = ET.SubElement(misc, 'TIME')
        mTime.text = str(m.time)
        mUse = ET.SubElement(misc, 'USE')
        if m.use == MISC_USE_BOIL :
            mUse.text = 'Boil'
        elif m.use == MISC_USE_MASH :
            mUse.text = 'Mash'
        elif m.use == MISC_USE_PRIMARY : 
            mUse.text = 'Primary'
        elif m.use == MISC_USE_SECONDARY :
            mUse.text = 'Secondary'  
        elif m.use == MISC_USE_BOTTLING :
            mUse.text = 'Bottling'


    yeasts = ET.SubElement(recipeTag, 'YEASTS')
    for y in recipe.listeYeasts:
        yeast = ET.SubElement(yeasts, 'YEAST')
        lNom = ET.SubElement(yeast, 'NAME')
        lVersion = ET.SubElement(yeast, 'VERSION')
        lVersion.text = '1'
        lType = ET.SubElement(yeast, 'TYPE')
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

    waters = ET.SubElement(recipeTag, 'WATERS')

    mash = ET.SubElement(recipeTag, 'MASH')
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
        mashStep = ET.SubElement(mSteps, 'MASH_STEP')
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

    try:
        notes = ET.SubElement(recipeTag, 'NOTES')
        notes.text = recipe.recipeNotes
    except:
        pass

    return ET.tostring(recipes, "unicode")
        


