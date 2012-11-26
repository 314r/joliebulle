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

    @staticmethod
    def parse(element):
        f = Fermentable()
        for balise in element:
            if balise.tag == 'NAME':
                f.fName = balise.text
            elif balise.tag == 'AMOUNT':
                f.fAmount = 1000*(float(balise.text))
            elif balise.tag == 'TYPE':
                f.fType = balise.text
            elif balise.tag == 'YIELD':
                f.fYield = float(balise.text)
            elif balise.tag == 'RECOMMEND_MASH':
                f.fRecommendMash = balise.text
            elif balise.tag == 'COLOR':
                #ATTENTION ! le format BeerXML utilise des unités SRM ! 
                #srm*1.97 =ebc
                f.fColor = float(balise.text)*1.97
        return f


class Hop:
    """"A class for storing Hops attributes"""
    def __init__(self, aAmount, aForm, aTime, aAlpha):
        self.hAmount = aAmount
        self.hForm = aForm
        self.hTime = aTime
        self.hAlpha = aAlpha

class Recipe:
    """A class for storing recipes attributes"""
    def __init__(self):
        self.recipeName = ""
        self.brewer = ""
        self.type = ""
        self.volume = ""
        self.rendement = 0.0
        self.boil = ""
        self.recipeNotes = ""
        self.styleRecette = ""
        self.listeFermentables = []

    @staticmethod
    def parse(tree):
        logger.debug("Start parsing recipe")
        recipe = Recipe()
        
        presentation=tree.find('.//RECIPE')
        fermentables=tree.findall('.//FERMENTABLE')
        style=tree.find('.//STYLE')

        for element in presentation :
            if 'NAME' == element.tag : 
                recipe.recipeName = element.text
                logger.debug(" Recipe name: %s", recipe.recipeName)
            if 'BREWER' == element.tag :
                recipe.brewer = element.text
                logger.debug(" Recipe brewer: %s", recipe.brewer)
            if 'TYPE' == element.tag:
                recipe.type = element.text
                logger.debug(" Recipe type: %s", recipe.type)
            if "BATCH_SIZE" == element.tag :
                recipe.volume = element.text
                logger.debug(" Recipe volume: %s", recipe.volume)
            if "EFFICIENCY" == element.tag :
                recipe.rendement= float(element.text)
                logger.debug(" Recipe efficiency: %s", recipe.rendement)
            if "BOIL_TIME" == element.tag :
                recipe.boil = element.text
                logger.debug(" Recipe boil time: %s", recipe.boil)
            if "NOTES" == element.tag :
                recipe.recipeNotes = element.text
                logger.debug(" Recipe notes: %s", recipe.recipeNotes)
        
        for element in style :
            if "NAME" == element.tag :
                recipe.styleRecette = element.text

        for element in fermentables:
            recipe.listeFermentables.append( Fermentable.parse(element) )

        logger.debug("End parsing recipe")
        return recipe