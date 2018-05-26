#!/usr/bin/python3
#­*­coding: utf­8 -­*­


import logging
from xml.etree import ElementTree
import model.constants
from model.fermentable import Fermentable
from model.hop import Hop
from model.mash import Mash
from model.mashstep import MashStep
from model.misc import Misc
from model.recipe import Recipe
from model.yeast import Yeast

logger = logging.getLogger(__name__)


def importBeerXMLRecipe(data):
    logger.debug("Start parsing recipe")
    try:
        tree = ElementTree.parse(data)
    except TypeError:
        tree = data
    except FileNotFoundError:
        tree = ElementTree.fromstring(data)
    except:
        raise

    recipe = Recipe()
    recipe.path = data

    presentation = tree.find('.//RECIPE')
    fermentables = tree.findall('.//FERMENTABLE')
    hops = tree.findall('.//HOP')
    levures = tree.findall('.//YEAST')
    misc = tree.findall('.//MISC')
    style = tree.find('.//STYLE')
    mash = tree.find('.//MASH')

    for element in presentation:
        if 'NAME' == element.tag:
            recipe.name = element.text
            logger.debug(" Recipe name: %s", recipe.name)
        if 'BREWER' == element.tag:
            recipe.brewer = element.text
            logger.debug(" Recipe brewer: %s", recipe.brewer)
        if 'TYPE' == element.tag:
            if "All Grain" == element.text:
                recipe.type = model.constants.RECIPE_TYPE_ALL_GRAIN
            elif "Partial Mash" == element.text:
                recipe.type = model.constants.RECIPE_TYPE_PARTIAL_MASH
            elif "Extract" == element.text:
                recipe.type = model.constants.RECIPE_TYPE_EXTRACT
            logger.debug(" Recipe type: %s", recipe.type)
        if "BATCH_SIZE" == element.tag:
            recipe.volume = float(element.text)
            logger.debug(" Recipe volume: %s", recipe.volume)
        if "EFFICIENCY" == element.tag:
            recipe.efficiency = float(element.text)
            logger.debug(" Recipe efficiency: %s", recipe.efficiency)
        if "BOIL_TIME" == element.tag:
            recipe.boil = float(element.text)
            logger.debug(" Recipe boil time: %s", recipe.boil)
        if "NOTES" == element.tag:
            recipe.recipeNotes = element.text
            logger.debug(" Recipe notes: %s", recipe.recipeNotes)
    try:
        for element in style:
            if "NAME" == element.tag:
                recipe.style = element.text
    except TypeError:
        recipe.style = ""

    try:
        recipe.mash = importBeerXMLMash(mash)
    except:
        pass

    for element in fermentables:
        recipe.listeFermentables.append(importBeerXMLFermentable(element))
    for element in hops:
        recipe.listeHops.append(importBeerXMLHop(element))
    for element in levures:
        recipe.listeYeasts.append(importBeerXMLYeast(element))
    for element in misc:
        recipe.listeMiscs.append(importBeerXMLMisc(element))

    logger.debug("End parsing recipe")
    return recipe


def importBeerXMLFermentable(data):
    fermentable = Fermentable()

    for child in data:
        if 'NAME' == child.tag:
            fermentable.name = child.text
        elif 'AMOUNT' == child.tag:
            fermentable.amount = 1000*(float(child.text))
        elif 'TYPE' == child.tag:
            if 'Grain' == child.text:
                fermentable.type = model.constants.FERMENTABLE_TYPE_GRAIN
            elif 'Sugar' == child.text:
                fermentable.type = model.constants.FERMENTABLE_TYPE_SUGAR
            elif 'Extract' == child.text:
                fermentable.type = model.constants.FERMENTABLE_TYPE_EXTRACT
            elif 'Dry Extract' == child.text:
                fermentable.type = model.constants.FERMENTABLE_TYPE_DRY_EXTRACT
            elif 'Adjunct' == child.text:
                fermentable.type = model.constants.FERMENTABLE_TYPE_ADJUNCT
            else:
                logger.warn ("Unkown fermentable type '%', assuming 'Sugar' by default", child.text)
                fermentable.type = model.constants.FERMENTABLE_TYPE_SUGAR
        elif 'YIELD' == child.tag:
            fermentable.fyield = float(child.text)
        elif 'RECOMMEND_MASH' == child.tag:
            fermentable.recommendMash = child.text
        elif 'COLOR' == child.tag:
            #ATTENTION ! le format BeerXML utilise des unités SRM !
            #srm*1.97 =ebc
            fermentable.color = float(child.text)*1.97
        elif 'ADD_AFTER_BOIL' == child.tag:
            if child.text == 'FALSE' :
                fermentable.useAfterBoil = False
            elif child.text == 'TRUE':
                fermentable.useAfterBoil = True

    return fermentable


def importBeerXMLHop(data):
    hop = Hop()

    for child in data:
        if 'NAME' == child.tag :
            hop.name = child.text
        elif 'AMOUNT' == child.tag :
            hop.amount = 1000*(float(child.text))
        elif 'FORM' == child.tag :
            if 'Pellet' == child.text:
                hop.form = model.constants.HOP_FORM_PELLET
            elif 'Leaf' == child.text:
                hop.form = model.constants.HOP_FORM_LEAF
            elif 'Plug' == child.text:
                hop.form = model.constants.HOP_FORM_PLUG
            else :
                logger.warn ("Unkown hop form '%s', assuming 'Pellet' by default", child.text)
                hop.form = model.constants.HOP_FORM_PELLET
        elif 'TIME' == child.tag :
            hop.time = float(child.text)
        elif 'ALPHA' == child.tag :
            hop.alpha = float(child.text)
        elif 'USE' == child.tag:
            if 'Boil' == child.text :
                hop.use = model.constants.HOP_USE_BOIL
            elif 'Dry Hop' == child.text or 'Dry Hopping' == child.text:
                hop.use = model.constants.HOP_USE_DRY_HOP
            elif 'Mash' == child.text:
                hop.use = model.constants.HOP_USE_MASH
            elif 'First Wort' == child.text:
                hop.use = model.constants.HOP_USE_FIRST_WORT
            elif 'Aroma' == child.text:
                hop.use = model.constants.HOP_USE_AROMA
            else :
                logger.warn ("Unkown hop use '%s', assuming 'Boil' by default", child.text)
                hop.use = model.constants.HOP_USE_BOIL

    if hop.use == 'Dry Hop':
        hop.time /= 24*60

    return hop


def importBeerXMLMash(data):
    mash = Mash()

    for child in data:
        if 'NAME' == child.tag:
            mash.name = child.text
        if 'GRAIN_TEMP' == child.tag:
            mash.grainTemp = child.text
        if 'TUN_TEMP' == child.tag:
            mash.tunTemp = child.text
        if 'SPARGE_TEMP' == child.tag:
            mash.spargeTemp = "%.1f" % float(child.text)
        if 'PH' == child.tag :
            mash.ph = "%.1f" % float(child.text)

    mashStep = data.findall('.//MASH_STEP')
    for element in mashStep:
        mash.listeSteps.append(importBeerXMLMashStep(element))

    return mash


def importBeerXMLMashStep(data):
    mashStep = MashStep()

    for child in data:
        if 'NAME' == child.tag:
            mashStep.name = child.text
        if 'VERSION' == child.tag:
            mashStep.version = int(child.text)
        if 'TYPE' == child.tag:
            if 'Infusion' == child.text:
                mashStep.type = model.constants.MASH_STEP_INFUSION
            elif 'Temperature' == child.text:
                mashStep.type = model.constants.MASH_STEP_TEMPERATURE
            elif 'Decoction' == child.text:
                mashStep.type = model.constants.MASH_STEP_DECOCTION
        if 'STEP_TIME' == child.tag:
            mashStep.time = "%.0f" % float(child.text)
        if 'STEP_TEMP' == child.tag:
            mashStep.temp = "%.1f" % float(child.text)
        if 'INFUSE_AMOUNT' == child.tag:
            mashStep.infuseAmount = float(child.text)

    return mashStep


def importBeerXMLMisc(data):
    misc = Misc()

    for child in data:
        if 'NAME' == child.tag :
            misc.name = child.text
        elif 'AMOUNT' == child.tag :
            misc.amount = float(child.text)*1000
        elif 'TYPE' == child.tag :
            misc.type = child.text
        elif 'TIME' == child.tag:
            try:
                misc.time = float(child.text)
            except ValueError:
                misc.time = 0.0
                logger.debug("misc time attribute is not numeric:%s", child.text)
        elif 'USE' == child.tag:
            if 'Boil' == child.text:
                misc.use = model.constants.MISC_USE_BOIL
            elif 'Mash' == child.text:
                misc.use = model.constants.MISC_USE_MASH
            elif 'Primary' == child.text:
                misc.use = model.constants.MISC_USE_PRIMARY
            elif 'Secondary' == child.text:
                misc.use = model.constants.MISC_USE_SECONDARY
            elif 'Bottling' == child.text:
                misc.use = model.constants.MISC_USE_BOTTLING
            else:
                logger.warn ("Unkown misc use '%s', assuming 'Boil' by default", child.text)
                misc.use = model.constants.MISC_USE_BOIL

    return misc


def importBeerXMLYeast(data):
    yeast = Yeast()

    for child in data:
        if 'NAME' == child.tag:
            yeast.name = child.text
        elif 'FORM' == child.tag:
            yeast.form = child.text
        elif 'LABORATORY' == child.tag:
            yeast.labo = child.text
        elif 'PRODUCT_ID' == child.tag:
            yeast.productId = child.text
        elif 'ATTENUATION' == child.tag:
            yeast.attenuation = float(child.text)

    return yeast
