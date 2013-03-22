#!/usr/bin/python3
#­*­coding: utf­8 -­*­



#JolieBulle 2.8
#Copyright (C) 2013 Thomas Gerbet

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

from PyQt4 import QtCore
from view.hopview import *
from view.miscview import *
from view.yeastview import *
from view.recipeview import *
from view.mashstepview import *

class ExportBBCode(QtCore.QObject):
    
    def exportBbcode (self, recipe):
        recipeView = RecipeView(recipe)
        recetteHeader = '[b]%s\n[i]%s[/i][/b]\n\n' % (recipe.name, recipeView.recipeTypeDisplay())
        
        specification_texte = self.trUtf8("Densité initiale : ") + str("%.3f" %(recipe.compute_OG())) + "\n"
        specification_texte += self.trUtf8("Densité finale : ") + str("%.3f" %(recipe.compute_FG())) + "\n"
        specification_texte += self.trUtf8("Teinte : ") + str("%.0f" %(recipe.compute_EBC())) + " EBC\n"
        specification_texte += self.trUtf8("Amertume : ") + str("%.0f" %(recipe.compute_IBU())) + " IBU\n"
        specification_texte += self.trUtf8("Alcool (vol) : ") + str("%.1f" %(recipe.compute_ABV())) + " %\n\n"
        
        specification_texte += self.trUtf8("Rendement : ") + str(recipe.efficiency) + " %\n"
        specification_texte += self.trUtf8("Ingrédients prévus pour un brassin de ") + str(recipe.volume) + "L \n\n"
        
        grains_texte = "[b]" + self.trUtf8("Grains et sucres") + "\n"
        grains_texte += "----------------------[/b]\n"
        for f in recipe.listeFermentables:
            grains_texte += "%.0fg %s\n" %(f.amount, f.name)
        grains_texte += "\n"
        
        houblons_texte = "[b]" + self.trUtf8("Houblons") + "\n"
        houblons_texte += "----------------------[/b]\n"
        for h in recipe.listeHops:
            hView = HopView(h)
            houblons_texte += "%.0fg %s (α%s%%, %s) @ %s min(%s)\n" %(h.amount, h.name, h.alpha, hView.hopFormDisplay(), h.time, hView.hopUseDisplay())
        houblons_texte += "\n"
        
        divers_texte = ""
        if len(recipe.listeMiscs) > 0:
            divers_texte = "[b]" + self.trUtf8("Ingrédients divers") + "\n"
            divers_texte += "----------------------[/b]\n"
            for m in recipe.listeMiscs:
                mView = MiscView(m)
                divers_texte += "%.0fg %s @ %.0f min(%s)\n" %(m.amount, m.name, m.time, mView.miscUseDisplay())
            divers_texte += "\n"
        
        levures_texte = "[b]" + self.trUtf8("Levures") + "\n"
        levures_texte += "----------------------[/b]\n"
        for y in recipe.listeYeasts:
            levures_texte += y.name + "\n"
        levures_texte += "\n"

        brassage_texte = "[b]" + self.trUtf8("Brassage") + "\n"
        brassage_texte += "----------------------[/b]\n"
        brassage_texte += "%s\n" %(recipe.mash.name)
        brassage_texte += "pH : %s\n\n" %(recipe.mash.ph)
        brassage_texte += self.trUtf8(" Etapes : ") +"\n"
        for step in recipe.mash.listeSteps:
            mashStepView = MashStepView(step)
            brassage_texte += step.name + " : " + self.trUtf8(" palier de type ")+ mashStepView.mashTypeDisplay() + self.trUtf8(" à ") + step.temp +" °C"+ self.trUtf8(" pendant ")+ step.time + self.trUtf8(" minutes ") + "\n"
        brassage_texte += "\n" + self.trUtf8(" Rinçage : ") + recipe.mash.spargeTemp +" °C\n"
        brassage_texte += "\n"

        recipeNotes = ""
        if recipe.recipeNotes is not None:
            recipeNotes = "[b]" + self.trUtf8("Notes") + "\n----------------------[/b]\n" + recipe.recipeNotes
            
        self.generatedBbcode = recetteHeader + specification_texte + grains_texte + houblons_texte + divers_texte + levures_texte + brassage_texte + recipeNotes
