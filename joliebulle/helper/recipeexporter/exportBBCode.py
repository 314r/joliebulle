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

from PyQt5.QtCore import QCoreApplication

from view.hopview import *
from view.yeastview import *
from view.miscview import *
from view.recipeview import *
from view.mashstepview import *


def exportBBCode(recipe):
    recipeView = RecipeView(recipe)
    generatedBbcode = '[b]%s\n[i]%s[/i][/b]\n\n' % (recipe.name, recipeView.recipeTypeDisplay())

    generatedBbcode += QCoreApplication.translate("Export", "Densité initiale : ") + "%.3f\n" % recipe.compute_OG()
    generatedBbcode += QCoreApplication.translate("Export", "Densité finale : ") + "%.3f\n" % recipe.compute_FG()
    generatedBbcode += QCoreApplication.translate("Export", "Teinte : ") + "%.0f EBC\n" % recipe.compute_EBC()
    generatedBbcode += QCoreApplication.translate("Export", "Amertume : ") + "%.0f IBU\n" % recipe.compute_IBU()
    generatedBbcode += QCoreApplication.translate("Export", "Alcool (vol) : ") + "%.1f %%\n\n" % recipe.compute_ABV()

    generatedBbcode += QCoreApplication.translate("Export", "Rendement : ") + "%.1f %%\n" % recipe.efficiency
    generatedBbcode += QCoreApplication.translate("Export", "Ingrédients prévus pour un brassin de") + " %.1fL\n\n" % recipe.volume

    generatedBbcode += "[b]" + QCoreApplication.translate("Export", "Grains et sucres") + "\n"
    generatedBbcode += "----------------------[/b]\n"
    for f in recipe.listeFermentables:
        generatedBbcode += "%.0f g %s\n" % (f.amount, f.name)
    generatedBbcode += "\n"

    generatedBbcode += "[b]" + QCoreApplication.translate("Export", "Houblons") + "\n"
    generatedBbcode += "----------------------[/b]\n"
    for h in recipe.listeHops:
        hView = HopView(h)
        generatedBbcode += "%.0f g %s (α %s%%, %s) @ %s min (%s)\n" % (
            h.amount, h.name, h.alpha, hView.hopFormDisplay(), h.time, hView.hopUseDisplay())
    generatedBbcode += "\n"

    if len(recipe.listeMiscs) > 0:
        generatedBbcode += "[b]" + QCoreApplication.translate("Export", "Ingrédients divers") + "\n"
        generatedBbcode += "----------------------[/b]\n"
        for m in recipe.listeMiscs:
            mView = MiscView(m)
            generatedBbcode += "%.0f g %s @ %.0f min (%s)\n" % (m.amount, m.name, m.time, mView.miscUseDisplay())
        generatedBbcode += "\n"

    generatedBbcode += "[b]" + QCoreApplication.translate("Export", "Levures") + "\n"
    generatedBbcode += "----------------------[/b]\n"
    for y in recipe.listeYeasts:
        yView = YeastView(y)
        generatedBbcode += yView.yeastDetailDisplay() + "\n"
    generatedBbcode += "\n"

    generatedBbcode += "[b]" + QCoreApplication.translate("Export", "Brassage") + "\n"
    generatedBbcode += "----------------------[/b]\n"
    generatedBbcode += "%s\n" %(recipe.mash.name)
    generatedBbcode += "pH : %s\n\n" %(recipe.mash.ph)
    generatedBbcode += QCoreApplication.translate("Export", "Étapes : ") +"\n"
    for step in recipe.mash.listeSteps:
        mashStepView = MashStepView(step)
        generatedBbcode += step.name + " : " + QCoreApplication.translate("Export", "palier de type")+ " " + \
                           mashStepView.mashTypeDisplay() + " " + QCoreApplication.translate("Export", "à") + " " + \
                           step.temp +" °C "+ QCoreApplication.translate("Export", "pendant") + " " + step.time + " " + \
                           QCoreApplication.translate("Export", "minutes") + "\n"
    generatedBbcode += "\n" + QCoreApplication.translate("Export", "Rinçage : ") + recipe.mash.spargeTemp +" °C\n"
    generatedBbcode += "\n"

    if recipe.recipeNotes is not None:
        generatedBbcode += "[b]" + QCoreApplication.translate("Export", "Notes") + \
                          "\n----------------------[/b]\n" + recipe.recipeNotes

    return generatedBbcode
