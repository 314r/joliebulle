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

from PyQt4 import QtCore


class ExportBBCode(QtCore.QObject):
    
    def exportBbcode (self, nomRecette, styleRecette, volume, boil, nbreFer, liste_ingr, liste_fAmount, nbreHops,liste_houblons, liste_hAlpha,liste_hForm,liste_hAmount,liste_hTime,liste_hUse,nbreDivers,liste_divers, liste_dType, liste_dAmount, liste_dTime, liste_dUse, nbreLevures, liste_levuresDetail, rendement, OG, FG, EBC, IBU, ABV, recipeNotes) :
        recetteHeader = "[b]" + nomRecette + "\n"
        recetteHeader += "[i]" + styleRecette + "[/i][/b]\n\n"
        
        specification_texte = "Densité initiale : " + str("%.3f" %(OG)) + "\n"
        specification_texte += "Densité finale : " + str("%.3f" %(FG)) + "\n"
        specification_texte += "Teinte : " + str("%.0f" %(EBC)) + " EBC\n"
        specification_texte += "Amertume : " + str("%.0f" %(IBU)) + " IBU\n"
        specification_texte += "Alcool (vol) : " + str("%.1f" %(ABV)) + " %\n\n"
        
        specification_texte += "Rendement : " + str(rendement) + " %\n"
        specification_texte += "Ingrédients prévus pour un brassin de " + str(volume) + "L \n\n"
        
        grains_texte = "[b]Grains et sucres\n"
        grains_texte += "----------------------[/b]\n"
        i = 0
        while i < nbreFer :
            i=i+1
            grains_texte += str("%.0f" %(liste_fAmount[i-1])) + "g " + liste_ingr[i-1] + "\n"
        grains_texte += "\n"
          
        houblons_texte = "[b]Houblons\n"
        houblons_texte += "----------------------[/b]\n"
        h = 0
        while h < nbreHops : 
            h = h+1    
            houblons_texte += str("%.0f" %(liste_hAmount[h-1])) + "g " + liste_houblons[h-1]  + " (α" +  str(liste_hAlpha[h-1]) +"%" + ", " + liste_hForm[h-1] +") @ " + str("%.0f" %(liste_hTime[h-1])) + "min (" +str(liste_hUse[h-1])  +  ")\n"
        houblons_texte += "\n"
        
        divers_texte = ""
        if nbreDivers > 0:
            divers_texte = "[b]Ingrédients divers\n"
            divers_texte += "----------------------[/b]\n"
            m = 0
            while  m < nbreDivers :
                m = m + 1 
                divers_texte += str("%.0f" %(liste_dAmount[m-1])) + "g " + liste_divers[m-1] +" (" + liste_dType[m-1] +") @ " + str("%.0f" %(liste_dTime[m-1]))+ "min ("+ str(liste_dUse[m-1]) + ")\n"
            divers_texte += "\n"
        
        levures_texte = "[b]Levures\n"
        levures_texte += "----------------------[/b]\n"
        l = 0
        while l < nbreLevures : 
            l = l+1
            levures_texte += liste_levuresDetail[l-1] + "\n"
        levures_texte += "\n"
            
        if recipeNotes != "":
            recipeNotes = "[b]Notes\n" + "----------------------[/b]\n" + recipeNotes
            
        self.generatedBbcode = recetteHeader + specification_texte + grains_texte + houblons_texte + divers_texte + levures_texte + recipeNotes
        
        
    def __str__(self):
        return self.generatedBbcode
