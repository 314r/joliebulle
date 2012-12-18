#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­



#JolieBulle 2.6
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
import logging
import model.constants

logger = logging.getLogger(__name__)

class Fermentable:
    """"A class for storing Fermentable attributes"""

    def __init__(self):
        self.fName = ''
        self.fAmount = 0.0
        self.fType = ''
        self.fYield = 0.0
        self.fRecommendMash = ''
        self.fColor = 0.0
        self.fUse = False

    def __repr__(self):
        return ('fermentable[fName="%s", fAmount=%s, fType=%s, fYield=%s, fRecommendMash=%s, fColor=%s, fUse=%s]' % 
            (self.fName, self.fAmount, self.fType, self.fYield, self.fRecommendMash, self.fColor, self.fUse) )

    @staticmethod
    def parse(element):
        f = Fermentable()
        for balise in element:
            if 'NAME' == balise.tag:
                f.fName = balise.text
            elif 'AMOUNT' == balise.tag:
                f.fAmount = 1000*(float(balise.text))
            elif 'TYPE' == balise.tag:
                f.fType = balise.text
            elif 'YIELD' == balise.tag:
                f.fYield = float(balise.text)
            elif 'RECOMMEND_MASH' == balise.tag:
                f.fRecommendMash = balise.text
            elif 'COLOR' == balise.tag:
                #ATTENTION ! le format BeerXML utilise des unités SRM ! 
                #srm*1.97 =ebc
                f.fColor = float(balise.text)*1.97
            elif 'ADD_AFTER_BOIL' == balise.tag:
                if balise.text == 'FALSE' :
                    f.fUse = False
                elif balise.text == 'TRUE':
                    f.fUse = True
        logger.debug(repr(f))
        return f


class Hop:
    """A class for storing Hops attributes"""
    def __init__(self):
        self.name = ''
        self.amount = 0.0
        self.form = model.constants.HOP_FORM_LEAF
        self.time = 0.0
        self.alpha = 0.0
    
    def __repr__(self):
        return 'hop[name="%s", amount=%s, form=%s, time=%s, alpha=%s]' % (self.name, self.amount, self.form, self.time, self.alpha)

    @staticmethod
    def parse(element):
        h = Hop()
        for balise in element:
            if 'NAME' == balise.tag :
                h.name = balise.text
            elif 'AMOUNT' == balise.tag :
                h.amount = 1000*(float(balise.text)) 
            elif 'FORM' == balise.tag :
                if 'Pellet' == balise.text:
                    h.form = model.constants.HOP_FORM_PELLET
                if 'Leaf' == balise.text:
                    h.form = model.constants.HOP_FORM_LEAF
                if 'Plug' == balise.text:
                    h.form = model.constants.HOP_FORM_PLUG
            elif 'TIME' == balise.tag :
                h.time = float(balise.text)
            elif 'ALPHA' == balise.tag :
                h.alpha = float(balise.text)
        logger.debug(repr(h))
        return h
    

class Yeast:
    """A class for storing Yeast attributes"""
    def __init__(self):
        self.name = ''
        self.form = ''
        self.labo = ''
        self.productId = ''
        self.attenuation = ''
    
    def __repr__(self):
        return ('yeast[name="%s", form=%s, labo=%s, productId=%s, attenuation=%s]' % 
                (self.name, self.form, self.labo, self.productId, self.attenuation))

    @staticmethod
    def parse(element):
        y = Yeast()
        for balise in element:
            if 'NAME' == balise.tag :
                y.name = balise.text
            elif 'FORM' == balise.tag :
                y.form = balise.text
            elif 'LABORATORY' == balise.tag :
                y.labo = balise.text
            elif 'PRODUCT_ID' == balise.tag :
                y.productId = balise.text
            elif 'ATTENUATION' == balise.tag:
                y.attenuation = balise.text
        logger.debug(repr(y))
        return y

class Misc:
    """A class for storing Misc attributes"""
    def __init__(self):
        self.name = ''
        self.amount = 0.0
        self.type = ''
        self.time = 0.0
        self.use = model.constants.MISC_USE_BOIL
    
    def __repr__(self):
        return 'misc[name="%s", amount=%s, type="%s", time=%s, use="%s"]' % (self.name, self.amount, self.type, self.time, self.use)
        
    @staticmethod
    def parse(element):
        m = Misc()
        for balise in element:
            if 'NAME' == balise.tag :
                m.name = balise.text
            elif 'AMOUNT' == balise.tag :
                m.amount = float(balise.text)*1000
            elif 'TYPE' == balise.tag :
                m.type = balise.text
            elif 'TIME' == balise.tag:
                try :
                    m.time = float(balise.text)
                except : 
                    m.time = 0.0
                    logger.debug("misc time attribute is not numeric:%s", balise.text)
            elif 'USE' == balise.tag:
                if 'Boil' == balise.text:
                    m.use = model.constants.MISC_USE_BOIL
                if 'Mash' == balise.text:
                    m.use = model.constants.MISC_USE_MASH
                if 'Primary' == balise.text:
                    m.use = model.constants.MISC_USE_PRIMARY
                if 'Secondary' == balise.text:
                    m.use = model.constants.MISC_USE_SECONDARY
                if 'Bottling' == balise.text:
                    m.use = model.constants.MISC_USE_BOTTLING

        logger.debug(repr(m))
        return m


class Recipe:
    """A class for storing recipes attributes"""
    def __init__(self):
        self.name = ""
        self.brewer = ""
        self.type = model.constants.RECIPE_TYPE_ALL_GRAIN
        self.volume = 0.0
        self.efficiency = 0.0
        self.boil = 0.0
        self.recipeNotes = ""
        self.style = ""
        self.mashName = ""
        self.mashGrainTemp = ""
        self.mashTunTemp = ""
        self.spargeTemp = ""
        self.mashPh = ""
        self.listeFermentables = list()
        self.listeHops = list()
        self.listeYeasts = list()
        self.listeMiscs = list()
        self.listeMashSteps = list()

    def __repr__(self):
        return ('recipe[name="%s", brewer="%s", type=%s, volume=%s, efficiency=%s, boil=%s, recipeNotes="%s", style="%s"]' %
                (self.name, self.brewer, self.type, self.volume, self.efficiency, self.boil, self.recipeNotes, self.style) )
    
    @staticmethod
    def parse(tree):
        logger.debug("Start parsing recipe")
        recipe = Recipe()
        
        presentation=tree.find('.//RECIPE')
        fermentables=tree.findall('.//FERMENTABLE')
        hops = tree.findall('.//HOP')
        levures = tree.findall('.//YEAST')
        misc = tree.findall('.//MISC')
        style=tree.find('.//STYLE')
        mash = tree.find('.//MASH')
        mashStep = mash.findall('.//MASH_STEP')

        for element in presentation :
            if 'NAME' == element.tag : 
                recipe.name = element.text
                logger.debug(" Recipe name: %s", recipe.name)
            if 'BREWER' == element.tag :
                recipe.brewer = element.text
                logger.debug(" Recipe brewer: %s", recipe.brewer)
            if 'TYPE' == element.tag:
                if "All Grain" == element.text :
                    recipe.type = model.constants.RECIPE_TYPE_ALL_GRAIN
                if "Partial Mash" == element.text :
                    recipe.type = model.constants.RECIPE_TYPE_PARTIAL_MASH
                if "Extract" == element.text :
                    recipe.type = model.constants.RECIPE_TYPE_EXTRACT
                logger.debug(" Recipe type: %s", recipe.type)
            if "BATCH_SIZE" == element.tag :
                recipe.volume = float(element.text)
                logger.debug(" Recipe volume: %s", recipe.volume)
            if "EFFICIENCY" == element.tag :
                recipe.efficiency= float(element.text)
                logger.debug(" Recipe efficiency: %s", recipe.efficiency)
            if "BOIL_TIME" == element.tag :
                recipe.boil = float(element.text)
                logger.debug(" Recipe boil time: %s", recipe.boil)
            if "NOTES" == element.tag :
                recipe.recipeNotes = element.text
                logger.debug(" Recipe notes: %s", recipe.recipeNotes)
        
        for element in style :
            if "NAME" == element.tag :
                recipe.style = element.text

        for element in mash:
            if 'NAME' == element.tag :
                recipe.mashName = element.text
            if 'GRAIN_TEMP' == element.tag :
                recipe.mashGrainTemp = element.text
            if 'TUN_TEMP' == element.tag  :
                recipe.mashTunTemp = element.text
            if 'SPARGE_TEMP' == element.tag  :
                recipe.spargeTemp = element.text
            if 'PH' == element.tag :
                recipe.mashPh = element.text

        for element in fermentables:
            recipe.listeFermentables.append( Fermentable.parse(element) )
        for element in hops:
            recipe.listeHops.append(Hop.parse(element))
        for element in levures:
            recipe.listeYeasts.append(Yeast.parse(element))
        for element in misc:
            recipe.listeMiscs.append(Misc.parse(element))
        for element in mashStep:
            recipe.listeMashSteps.append(MashStep.parse(element))

        logger.debug(repr(recipe))
        logger.debug("End parsing recipe")
        return recipe

class MashStep:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.time = ""
        self.temp = ""
        self.infuseAmount = 0.0
        self.version = 1

    @staticmethod
    def parse(element):
        m = MashStep()
        for balise in element:
            if 'NAME' == balise.tag:
                m.name = balise.text
            if 'VERSION' == balise.tag:
                m.version = int(balise.text)
            if 'TYPE' == balise.tag:
                if 'Infusion' == balise.text:
                    m.type = model.constants.MASH_STEP_INFUSION
                elif 'Temperature' == balise.text:
                    m.type = model.constants.MASH_STEP_TEMPERATURE
                elif 'Decoction' == balise.text:
                    m.type = model.constants.MASH_STEP_DECOCTION
            if 'STEP_TIME' == balise.tag:
                m.time = balise.text
            if 'STEP_TEMP' == balise.tag:
                m.temp = balise.text
            if 'INFUSE_AMOUNT' == balise.tag:
                m.infuseAmount = balise.text
