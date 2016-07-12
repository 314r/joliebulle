#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.6
#Copyright (C) 2010-2016 Pierre Tavares

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

from PyQt5.QtCore import QCoreApplication
import json
from view.fermentableview import *
from view.hopview import *
from view.yeastview import *
from view.miscview import *
from view.recipeview import *
from view.mashstepview import *
from model.constants import *
from settings import *


def exportJson(recipe) :
    recipeView = RecipeView(recipe)
    settings = Settings()
    data = []
    dic = {}

    dic['path'] = recipe.path
    dic['name'] = recipe.name
    if recipe.brewer :
        dic['brewer'] = recipe.brewer
    else :
        dic['brewer'] = "anonymous"
    # dic['type'] = recipeView.recipeTypeDisplay()
    dic['style'] = recipe.style
    if recipe.type == RECIPE_TYPE_ALL_GRAIN:
        dic['type'] = "All Grain"
    elif recipe.type == RECIPE_TYPE_EXTRACT:
        dic['type'] = "Extract"
    elif recipe.type == RECIPE_TYPE_PARTIAL_MASH:
        dic['type'] = "Partial Mash"
    dic['volume'] = recipe.volume
    dic['boilTime'] = recipe.boil
    dic['efficiency'] = recipe.efficiency
    # dic['ibu'] = "%.0f" %recipe.compute_IBU()
    # dic['ebc'] = "%.0f" %recipe.compute_EBC()
    # dic['og'] = "%.3f" %recipe.compute_OG()
    # dic['fg'] = "%.3f" %recipe.compute_FG()
    # dic['bugu'] = "%.2f" %recipe.compute_ratioBUGU()
    # dic['alc'] = "%.1f" %recipe.compute_ABV()

    dic['grainWeight'] = recipe.compute_grainWeight()
    dic['preBoilGu'] = recipe.compute_GU_PreBoil()
    dic['gu'] = recipe.compute_GU()
    dic['coolingLossRate'] = settings.conf.value("CoolingLoss")
    dic['boilOffRate'] = settings.conf.value("BoilOffRate")
    dic['grainTemp'] = settings.conf.value("GrainTemp")
    dic['fudgeFactor'] = settings.conf.value("FudgeFactor")
    dic['grainRetention'] = settings.conf.value("GrainRetention")


    hops = []
    for h in recipe.listeHops:
        hView = HopView(h)
        hop = {}
        hop['name'] = h.name
        if h.form == HOP_FORM_PELLET :
            hop['form'] = "Pellet"
        elif h.form == HOP_FORM_LEAF :
            hop['form'] = "Leaf"
        elif h.form == HOP_FORM_PLUG :
            hop['form'] = "Plug"
        hop['alpha'] = h.alpha
        hop['use'] = h.use
        hop['time'] = h.time
        hop['amount'] = h.amount
        hop['ibuPart'] = "%.1f" %recipe.compute_IBUPart()[h]
        hops.append(hop)
    dic['hops'] = hops

    fermentables = []
    for f in recipe.listeFermentables:
        fView = FermentableView(f)
        fermentable = {}
        fermentable['name'] = f.name
        fermentable['type'] = f.type
        fermentable['fyield'] = f.fyield
        fermentable['color'] = f.color
        fermentable['amount'] = f.amount
        if f.useAfterBoil :
            fermentable['afterBoil'] = 'TRUE'
        else :
            fermentable['afterBoil'] = 'FALSE'
        # fermentable['afterBoilView'] = fView.fermentableUseDisplay()
        fermentable['recoMash'] = f.recommendMash
        fermentables.append(fermentable)
    dic['fermentables'] = fermentables

    yeasts = []
    for y in recipe.listeYeasts :
        yView = YeastView(y)
        yeast = {}
        yeast['name'] = y.name
        yeast['product_id'] = y.productId
        yeast['labo'] = y.labo
        yeast['form'] = y.form
        yeast['attenuation'] = y.attenuation
        yeasts.append(yeast)
    dic['yeasts'] = yeasts

    miscs = []
    for m in recipe.listeMiscs :
        mView = MiscView(m)
        misc = {}
        misc['name'] = m.name
        misc['amount'] = m.amount
        misc['type'] = m.type
        misc['use'] = m.use
        misc['time'] = m.time
        miscs.append(misc)
    dic['miscs'] = miscs

    mashProfile = {}
    mashProfile['name'] = recipe.mash.name
    mashProfile['ph'] = recipe.mash.ph
    mashProfile['sparge'] = recipe.mash.spargeTemp
    mashProfile['tunTemp'] = recipe.mash.tunTemp

    steps = []
    for s in recipe.mash.listeSteps :
        mashStepView = MashStepView(s)
        step = {}
        step['name'] = s.name
        step['time'] = s.time
        step['temp'] = s.temp
        step['type_view'] = mashStepView.mashTypeDisplay()
        step['type'] = s.type
        steps.append(step)
    mashProfile['steps'] = steps
    dic['mashProfile'] = mashProfile

    dic['notes'] = recipe.recipeNotes


    data.append(dic)
    data = json.dumps(data)
    # data = data.replace("'","&#39;")

    return data
