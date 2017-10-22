#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.6
#Copyright (C) 2010-2016 Pierre Tavares
#Copyright (C) 2012-2015 joliebulle's authors
#See AUTHORS file.

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
from xml.etree import ElementTree
import model.constants
from model.fermentable import Fermentable
from model.hop import Hop
from model.mash import Mash
from model.mashstep import MashStep
from model.misc import Misc
from model.recipe import Recipe
from model.yeast import Yeast
import re

logger = logging.getLogger(__name__)


def importBSMXRecipe(data):
    logger.debug("Start parsing BSMX recipe")
    
    #BSMX format use not valid entities
    def correct_bsmx_entities(text):
        text = re.sub('(ld|rd|rs)quo;', 'quot;', text)
        text = text.replace('&deg;', '°')
        return text
    try:
        tree = ElementTree.fromstring(correct_bsmx_entities(open(data, 'r').read()))
    except TypeError:
        tree = data
    except FileNotFoundError:
        tree = ElementTree.fromstring(correct_bsmx_entities(data))
    except:
        raise

    recipe = Recipe()

    recipe_root = tree.find('.//Recipe')

    recipe.name = recipe_root.find('F_R_NAME').text
    recipe.brewer = recipe_root.find('F_R_BREWER').text
    equipment = recipe_root.find('F_R_EQUIPMENT')
    recipe.volume = bsmx_volume_conversion(float(equipment.find('F_E_BATCH_VOL').text))
    recipe.efficiency = float(equipment.find('F_E_EFFICIENCY').text)
    recipe.boil = float(equipment.find('F_E_BOIL_TIME').text)
    bsmx_type = {
        '0': model.constants.RECIPE_TYPE_EXTRACT,
        '1': model.constants.RECIPE_TYPE_PARTIAL_MASH,
        '2': model.constants.RECIPE_TYPE_ALL_GRAIN
    }
    recipe.type = bsmx_type[recipe_root.find('F_R_TYPE').text]
    style = recipe_root.find('F_R_STYLE')
    recipe.style = '%s%s. %s' % (style.find('F_S_NUMBER').text, chr(64+int(style.find('F_S_LETTER').text) % 26),
                                 style.find('F_S_NAME').text)
    recipe.recipeNotes = recipe_root.find('F_R_NOTES').text
    recipe.mash = importBSMXMash(recipe_root.find('F_R_MASH'))

    elements = recipe_root.find('Ingredients').find('Data')
    for element in elements.findall('Grain'):
        recipe.listeFermentables.append(importBSMXFermentable(element))
    for element in elements.findall('Hops'):
        recipe.listeHops.append(importBSMXHop(element))
    for element in elements.findall('Yeast'):
        recipe.listeYeasts.append(importBSMXYeast(element))
    for element in elements.findall('Misc'):
        recipe.listeMiscs.append(importBSMXMisc(element))

    logger.debug("End parsing BSMX recipe")
    return recipe


def importBSMXFermentable(data):
    fermentable = Fermentable()
    fermentable.name = data.find('F_G_NAME').text
    # 1 oz = 28.3495231 gr
    fermentable.amount = float(data.find('F_G_AMOUNT').text)*28.3495231
    fermentable.fyield = float(data.find('F_G_YIELD').text)
    # 1 SRM = 1.97 EBC
    fermentable.color = float(data.find('F_G_COLOR').text)*1.97
    fermentable.recommendMash = data.find('F_G_RECOMMEND_MASH').text == '1'
    fermentable.useAfterBoil = data.find('F_G_ADD_AFTER_BOIL').text == '1'
    bsmx_type_grain = {
        '0': model.constants.FERMENTABLE_TYPE_GRAIN,
        '1': model.constants.FERMENTABLE_TYPE_EXTRACT,
        '2': model.constants.FERMENTABLE_TYPE_SUGAR,
        '3': model.constants.FERMENTABLE_TYPE_ADJUNCT,
        '4': model.constants.FERMENTABLE_TYPE_DRY_EXTRACT
    }
    # If the fermentable type is not known, we assume it is sugar
    fermentable.type = bsmx_type_grain.get(data.find('F_G_TYPE').text, model.constants.FERMENTABLE_TYPE_SUGAR)
    return fermentable


def importBSMXHop(data):
    hop = Hop()
    hop.name = data.find('F_H_NAME').text
    # 1 oz = 28.3495231 gr
    hop.amount = float(data.find('F_H_AMOUNT').text)*28.3495231
    hop.alpha = float(data.find('F_H_ALPHA').text)
    bsmx_hop_form = {
        '0': model.constants.HOP_FORM_LEAF,
        '1': model.constants.HOP_FORM_PELLET,
        '2': model.constants.HOP_FORM_PLUG
    }
    hop.form = bsmx_hop_form.get(data.find('F_H_TYPE').text, model.constants.HOP_FORM_LEAF)
    bsmx_hop_usage = {
        '0': model.constants.HOP_USE_BOIL,
        '1': model.constants.HOP_USE_DRY_HOP,
        '2': model.constants.HOP_USE_FIRST_WORT,
        '3': model.constants.HOP_USE_MASH,
        '4': model.constants.HOP_USE_AROMA
    }
    hop.use = bsmx_hop_usage.get(data.find('F_H_USE').text, model.constants.HOP_USE_BOIL)
    if hop.use == model.constants.HOP_USE_DRY_HOP:
        hop.time = float(data.find('F_H_DRY_HOP_TIME').text)
    else:
        hop.time = float(data.find('F_H_BOIL_TIME').text)
    return hop


def importBSMXMash(data):
    mash = Mash()
    mash.name = data.find('F_MH_NAME').text
    mash.grainTemp = "%.2f" % farenheit_to_celsius(float(data.find('F_MH_GRAIN_TEMP').text))
    mash.tunTemp = "%.2f" % farenheit_to_celsius(float(data.find('F_MH_TUN_TEMP').text))
    mash.spargeTemp = "%.2f" % farenheit_to_celsius(float(data.find('F_MH_SPARGE_TEMP').text))
    mash.ph = "%.1f" % float(data.find('F_MH_PH').text)
    mashSteps = data.find('steps').find('Data').findall('MashStep')
    for step in mashSteps:
        mash.listeSteps.append(importBSMXMashStep(step))
    return mash


def importBSMXMashStep(data):
    mashStep = MashStep()
    mashStep.name = data.find('F_MS_NAME').text
    bsmx_step_type = {
        '0': model.constants.MASH_STEP_INFUSION,
        '1': model.constants.MASH_STEP_DECOCTION,
        '2': model.constants.MASH_STEP_TEMPERATURE
    }
    mashStep.type = bsmx_step_type.get(data.find('F_MS_TYPE').text, model.constants.MASH_STEP_INFUSION)
    mashStep.time = "%.0f" % float(data.find('F_MS_STEP_TIME').text)
    mashStep.temp = "%.1f" % farenheit_to_celsius(float(data.find('F_MS_STEP_TEMP').text))
    mashStep.infuseAmount = bsmx_volume_conversion(float(data.find('F_MS_TUN_VOL').text))
    return mashStep


def importBSMXMisc(data):
    misc = Misc()
    misc.name = data.find('F_M_NAME').text
    # 1 tsp (US) = 4.92892161458 gr
    misc.amount = float(data.find('F_M_AMOUNT').text) * 4.92892161458
    misc.time = float(data.find('F_M_TIME').text)
    misc.type = data.find('F_M_USE_FOR').text
    bsmx_misc_usage = {
        '1': model.constants.MISC_USE_BOIL,
        '5': model.constants.MISC_USE_MASH
    }
    misc.use = bsmx_misc_usage.get(data.find('F_M_TYPE').text, model.constants.MISC_USE_BOIL)
    return misc


def importBSMXYeast(data):
    yeast = Yeast()
    yeast.name = data.find('F_Y_NAME').text
    yeast.labo = data.find('F_Y_LAB').text
    yeast.productId = data.find('F_Y_PRODUCT_ID').text
    yeast.attenuation = (float(data.find('F_Y_MIN_ATTENUATION').text) + float(data.find('F_Y_MAX_ATTENUATION').text))/2
    bsmx_yeast_form = {
        '0': model.constants.YEAST_FORM_LIQUID,
        '1': model.constants.YEAST_FORM_DRY,
        '2': model.constants.YEAST_FORM_CULTURE,
        '3': model.constants.YEAST_FORM_SLANT
    }
    yeast.form = bsmx_yeast_form.get(data.find('F_Y_FORM').text, model.constants.YEAST_FORM_DRY)
    return yeast


def bsmx_volume_conversion(vol):
    """
    Convertit un volume provenant d'un fichier BSMX en L
    Volume_L = (Volume_BSMX / 128) * 3.785
    """
    return vol / 128 * 3.785


def farenheit_to_celsius(temperature):
    return (temperature - 32) * 5/9