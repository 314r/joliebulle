#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#JolieBulle 2.8
#Copyright (C) 2010-2013 Pierre Tavares
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


from PyQt4.QtCore import QCoreApplication

from view.hopview import *
from view.miscview import *
from view.yeastview import *
from view.mashstepview import *


def exportHTML(recipe):
    resultHtml = '''
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

    #Profil
    resultHtml += '<table class="profil">'
    resultHtml += '<tr><td>%s</td><td>%.1f %%</td></tr>' % (QCoreApplication.translate("Export", "Rendement : "), recipe.efficiency)
    resultHtml += '<tr><td>%s</td><td>%.3f</td></tr>' % (QCoreApplication.translate("Export", "Densité initiale : "), recipe.compute_OG())
    resultHtml += '<tr><td>%s</td><td>%.3f</td></tr>' % (QCoreApplication.translate("Export", "Densité finale : "), recipe.compute_FG())
    resultHtml += '<tr><td>%s</td><td>%.0f EBC</td></tr>' % (QCoreApplication.translate("Export", "Teinte : "), recipe.compute_EBC())
    resultHtml += '<tr><td>%s</td><td>%.0f IBU</td></tr>' % (QCoreApplication.translate("Export", "Amertume : "), recipe.compute_IBU())
    resultHtml += '<tr><td>%s</td><td>%.1f</td></tr>' % (QCoreApplication.translate("Export", "Ratio BU/GU : "), recipe.compute_ratioBUGU())
    resultHtml += '<tr><td>%s</td><td>%.1f %%</td></tr>' % (QCoreApplication.translate("Export", "Alcool (vol) : "), recipe.compute_ABV())
    resultHtml += '</table>'

    #Ingredients informations
    resultHtml += '<h2>%s %.1f %s</h2>' % (
        QCoreApplication.translate("Export", "Ingrédients prévus pour un brassin de"),
        recipe.volume, QCoreApplication.translate("Export", "litres"))

    #Grains
    resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Grains et sucres")
    resultHtml += '<table class="ingredients">'
    for f in recipe.listeFermentables:
        use = QCoreApplication.translate("Export", "Ajout après ébullition") if f.useAfterBoil else ''
        resultHtml += '<tr><td>%.0fg</td><td>%s</td><td>%s</td></tr>' % (f.amount, f.name, use)
    resultHtml += '</table>'

    #Houblons
    resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Houblons")
    resultHtml += '<table class="ingredients">'
    for h in recipe.listeHops:
        hUI = HopView(h)
        resultHtml += '<tr>'
        resultHtml += '<td>%.0fg</td>' % h.amount
        resultHtml += '<td>%s (α%.1f%%, %s)</td>' % (h.name, h.alpha, hUI.hopFormDisplay())
        resultHtml += '<td>%.0fmin (%s)</td>' % (h.time, hUI.hopUseDisplay())
        resultHtml += '</tr>'
    resultHtml += '</table>'

    #Ingredients divers
    if len(recipe.listeMiscs) > 0:
        resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Ingrédients divers")
        resultHtml += '<table class="ingredients">'
        for m in recipe.listeMiscs:
            mUI = MiscView(m)
            resultHtml += '<tr>'
            resultHtml += '<td>%.0fg</td>' % m.amount
            resultHtml += '<td>%s (%s)</td>' % (m.name, m.type)
            resultHtml += '<td>%.0fmin (%s)</td>' % (m.time, mUI.miscUseDisplay())
            resultHtml += '</tr>'
        resultHtml += '</table>'

    #Levures
    resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Levures")
    resultHtml += '<table class="ingredients">'
    for y in recipe.listeYeasts:
        yUI = YeastView(y)
        resultHtml += '%s<br />' % yUI.yeastDetailDisplay()
    resultHtml += '</table>'

    #Brassage informations
    resultHtml += '<h2>%s</h2>' % QCoreApplication.translate("Export", "Brassage")
    resultHtml += '<p>%s<br />pH : %s</p>' % (recipe.mash.name, recipe.mash.ph)

    #Etapes brassage
    resultHtml += '<p>'
    resultHtml += '<b>%s</b><br />' % QCoreApplication.translate("Export", "Étapes : ")
    for step in recipe.mash.listeSteps:
        mashStepUI = MashStepView(step)
        resultHtml += '%s : %s %s %s %s °C %s %s %s<br />' % (step.name,
                                                           QCoreApplication.translate("Export", "palier de type"),
                                                           mashStepUI.mashTypeDisplay(),
                                                           QCoreApplication.translate("Export", "à"), step.temp,
                                                           QCoreApplication.translate("Export", "pendant"), step.time,
                                                           QCoreApplication.translate("Export", "minutes"))
    resultHtml += '</p>'

    #Rincage
    resultHtml += '<p><b>%s</b>%s °C</p>' % (QCoreApplication.translate("Export", "Rinçage : "), recipe.mash.spargeTemp)

    #Notes
    if recipe.recipeNotes is not None:
        resultHtml += '<h2>%s</h2><p>%s</p>' % (QCoreApplication.translate("Export", "Notes"), recipe.recipeNotes)

    resultHtml += '</body></html>'

    return resultHtml
