#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.2
#Copyright (C) 2010-2014 Pierre Tavares

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

from PyQt4.QtCore import QCoreApplication
import json
from view.fermentableview import *
from view.hopview import *
from view.yeastview import *
from view.miscview import *
from view.recipeview import *
from view.mashstepview import *


def exportJson(recipe) :
	recipeView = RecipeView(recipe)
	data = []
	dic = {}

	dic['name'] = recipe.name
	dic['brewer'] = recipe.brewer
	dic['type'] = recipeView.recipeTypeDisplay()
	dic['volume'] = recipe.volume
	dic['boilTime'] = recipe.boil
	dic['efficiency'] = recipe.efficiency
	dic['ibu'] = "%.0f" %recipe.compute_IBU()
	dic['ebc'] = "%.0f" %recipe.compute_EBC()
	dic['og'] = "%.3f" %recipe.compute_OG()
	dic['fg'] = "%.3f" %recipe.compute_FG()
	dic['bugu'] = "%.1f" %recipe.compute_ratioBUGU()
	dic['alc'] = "%.1f" %recipe.compute_ABV()

	hops = []
	for h in recipe.listeHops:
		hView = HopView(h)
		hop = {}
		hop['name'] = h.name
		hop['form'] = hView.hopFormDisplay()
		hop['alpha'] = h.alpha
		hop['use'] = hView.hopUseDisplay()
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
		fermentable['type'] = fView.fermentableTypeDisplay()
		fermentable['yield'] = "%.1f" %f.fyield
		fermentable['color'] = "%.0f" %f.color
		fermentable['amount'] = f.amount
		if f.useAfterBoil :
			fermentable['after-boil'] = 'true'
		else : 
			fermentable['after-boil'] = 'false'
		fermentables.append(fermentable)
	dic['fermentables'] = fermentables	

	yeasts = []
	for y in recipe.listeYeasts :
		yView = YeastView(y)
		yeast = {}
		yeast['name'] = y.name
		yeast['product_id'] = y.productId
		yeast['labo'] = y.labo
		yeast['form'] = yView.yeastFormDisplay()
		yeast['attenuation'] = y.attenuation
		yeasts.append(yeast)
	dic['yeasts'] = yeasts

	miscs = []
	for m in recipe.listeMiscs :
		mView = MiscView(m)
		misc = {}
		misc['name'] = m.name
		misc['amount'] = m.amount
		misc['type'] = mView.miscTypeDisplay()
		misc['use'] = mView.miscUseDisplay()
		misc['time'] = m.time
		miscs.append(misc)
	dic['miscs'] = miscs

	mashProfile = {}
	mashProfile['name'] = recipe.mash.name
	mashProfile['ph'] = recipe.mash.ph
	mashProfile['sparge'] = recipe.mash.spargeTemp
	
	steps = []
	for s in recipe.mash.listeSteps :
		mashStepView = MashStepView(s)
		step = {}
		step['name'] = s.name
		step['time'] = s.time
		step['temp'] = s.temp
		step['type'] = mashStepView.mashTypeDisplay()
		steps.append(step)
	mashProfile['steps'] = steps
	dic['mashProfile'] = mashProfile

	dic['notes'] = recipe.recipeNotes
	

	data.append(dic)
	data = json.dumps(data)
	data = data.replace("'","&#39;")

	return data
	



