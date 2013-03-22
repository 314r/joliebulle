
#JolieBulle 2.8
#Copyright (C) 2010-2013 Pierre Tavares

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



import codecs
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from base import *
from globals import *
from view.hopview import *
from view.miscview import *
from view.yeastview import *
from view.mashstepview import *

class ExportHTML(QtGui.QDialog) : 

    def exportRecipeHtml (self, recipe) :
        
        self.recetteHtmlHeader = '''
<!DOCTYPE html>
<html lang="fr">
<head>
<title>%s</title>
<meta charset="utf-8" />
<style type="text/css">
html { font-size:100.01%%; }
body {width:800px;margin:auto;line-height: 1.5;color: #222; font-size:80%%}
h1,h2,h3,h4,h5,h6 { font-weight: normal; color: #111; }
h1 { font-size: 2em; margin-bottom: 0; text-align:center;}
h2 { font-size: 1.5em; line-height: 1; margin-bottom: 2em; margin-top:2em; padding-bottom:0.75em; padding-top:0.75em;border-bottom:solid 1px #ddd;clear:both;}
h3 { font-size: 1.2em; line-height: 1.25; margin-bottom: 1.25em; text-align:left; background-color:#eeeeee; border-bottom:1px solid #cccccc; border-top:1px solid #cccccc; padding:0.5em 0 0.5em 0.5em;}
ul{list-style-type: none;text-align:left;}
.genre {font-style:italic; text-align:center;color:#ddd;margin-top:0;padding-top:0;border:0;border-bottom:solid 1px #ddd;}
.profil{text-align:left;margin-bottom:1em; width:400px;background:url(/Images/glade.png);}
.profil td {min-width: 200px;}
.ingredients{text-align:left; margin-bottom:2em;}
.ingredients td {min-width: 200px;}

.footer { width:700px;
margin:auto; 
margin-top:4em;
margin-bottom:4em;
padding:0.5em;
background-color:#eeeeee;
border-bottom :1px solid #cccccc;
border-top :1px solid #cccccc;
text-align : center;}
</style>
</head>
<body>
<h1>%s</h1>
<h2 class="genre">%s</h2>''' % (recipe.name, recipe.name, recipe.style)

#         self.recetteHtmlInfo = self.trUtf8('''
# Recette prévue pour un brassin de ''') + str(volume) + self.trUtf8(''' litres <br/>''')

        grains_texte=self.trUtf8('<h3>Grains et sucres</h3> ') + '<table class="ingredients">'
        for f in recipe.listeFermentables:
            if f.useAfterBoil == True:
                use = self.trUtf8('Ajout après ébullition')
            else :
                use = ''
            grains_texte = grains_texte + '<tr><td>%sg</td><td>%s</td><td>%s</td></tr>' % ( str("%.0f" %f.amount), f.name, use )
        grains_texte=grains_texte + '</table>'
          
        houblons_texte=self.trUtf8('<h3>Houblons</h3>') + '<table class="ingredients">'
        for h in recipe.listeHops:
            hUI = HopView(h)
            houblons_texte = houblons_texte + '<tr><td>%sg</td><td>%s (α%s%%, %s)</td><td>%smin (%s)</td></tr>' % (str("%.0f" %(h.amount)), h.name, str(h.alpha), hUI.hopFormDisplay(), str("%.0f" %(h.time)), hUI.hopUseDisplay() )
        houblons_texte = houblons_texte + '</table>'
        
        divers_texte = self.trUtf8('<h3>Ingrédients divers</h3>')  + '<table class="ingredients">'
        for m in recipe.listeMiscs:
            mUI = MiscView(m)
            divers_texte = divers_texte +  '<tr><td>%sg</td><td>%s (%s)</td><td>%smin (%s)</td></tr>' % (str("%.0f" %(m.amount)), m.name, m.type, str("%.0f" %(m.time)), mUI.miscUseDisplay() )
        divers_texte = divers_texte + '</table>'
        
        levures_texte = self.trUtf8('<h3>Levures</h3>')
        for y in recipe.listeYeasts:
            yUI = YeastView(y)
            levures_texte = levures_texte + yUI.yeastDetailDisplay() + '<br/>'
        
        self.recetteHtmlIng = self.trUtf8('<h2>Ingrédients pour un brassin de ') + str(recipe.volume) + self.trUtf8(' litres') + grains_texte + houblons_texte + divers_texte + levures_texte
        
        self.recetteHtmlProfil = '<table class="profil">%s<td>%s%% </td></tr>%s<td>%.3f</td></tr>%s<td>%s</td></tr>%s<td>%.0f EBC </td></tr>%s<td>%.0f IBU </td></tr>%s<td>%.1f</td></tr>%s<td>%.1f%% </td></tr></table>' % \
            (self.trUtf8('<tr><td>Rendement</td> '), str(recipe.efficiency), self.trUtf8('<tr><td>Densité initiale</td>'), recipe.compute_OG(),
            self.trUtf8('<tr><td>Densité finale</td>'), str("%.3f" %(recipe.compute_FG())), self.trUtf8('<tr><td>Teinte</td>'), recipe.compute_EBC(),
            self.trUtf8('<tr><td>Amertume</td>'), recipe.compute_IBU(), self.trUtf8('<tr><td>Ratio BU/GU</td>'), recipe.compute_ratioBUGU(),
            self.trUtf8('<tr><td>Alcool (vol)</td>'), recipe.compute_ABV())

        self.recetteHtmlMashProfile = self.trUtf8(' <h2>Brassage</h2>') + '<p>' + recipe.mash.name + '<br/> pH : ' + str(recipe.mash.ph) + '</p><p><b>' + self.trUtf8(''' Étapes : ''') + '</b> </p> '
        for step in recipe.mash.listeSteps:
            mashStepUI = MashStepView(step)
            self.recetteHtmlMashProfile = self.recetteHtmlMashProfile + step.name + ' : ' + self.trUtf8(''' palier de type ''')+ mashStepUI.mashTypeDisplay() + self.trUtf8(''' à ''') + step.temp +'''°C'''+ self.trUtf8(''' pendant ''')+ step.time + self.trUtf8(''' minutes ''')+ '''<br/> '''
        self.recetteHtmlMashProfile = self.recetteHtmlMashProfile + '<p><b>' + self.trUtf8(''' Rinçage : ''') + '</b></p>' + recipe.mash.spargeTemp + ' °C'

        if recipe.recipeNotes != None :
            self.recipeNotes = self.trUtf8(' <h2>Notes</h2>') + '<p>' + str(recipe.recipeNotes) + '</p>'
        else:
            self.recipeNotes = self.trUtf8(' <h2>Notes</h2>') + '<p></p>'

        self.recetteHtmlFooter =self.trUtf8('''
# <footer class="footer">Une recette générée par JolieBulle, logiciel de brassage libre.</footer>
</body>
</html>''')
                                        
    def generateHtml(self) :
        self.generatedHtml = self.recetteHtmlHeader + self.recetteHtmlProfil + self.recetteHtmlIng + self.recetteHtmlMashProfile + self.recipeNotes
                                        
                                        
    def enregistrerHtml(self,fileHtml) : 
        if  fileHtml.open(QtCore.QIODevice.WriteOnly) :
            self.stream = QtCore.QTextStream(fileHtml)
            self.generateHtml()
            self.stream << self.generatedHtml
                                     
        else :
            fileHtml.close()
                        
