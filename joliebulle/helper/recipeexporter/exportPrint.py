#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.1
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


def exportPrint(recipe):
    resultHtml = '''
<!DOCTYPE html>
<html lang="fr">
<head>
<title>%s</title>
<meta charset="utf-8" />
<style type="text/css">
pre {white-space: pre-wrap;font-size:1.25em;}
</style>
</head>
<body>
<h1>%s</h1>
<h2 class="genre">%s</h2>''' % (recipe.name, recipe.name, recipe.style)

    #Profil
    resultHtml += '<table class="profil">'
    resultHtml += '<tr><td>%s</td><td>%.1f %%</td></tr>' % (QCoreApplication.translate("Export", "Rendement : ", None, QCoreApplication.UnicodeUTF8), recipe.efficiency)
    resultHtml += '<tr><td>%s</td><td>%.0f min</td></tr>' % (QCoreApplication.translate("Export", "Ébullition : ", None, QCoreApplication.UnicodeUTF8), recipe.boil)
    resultHtml += '<tr><td>%s</td><td>%.3f</td></tr>' % (QCoreApplication.translate("Export", "Densité initiale : ", None, QCoreApplication.UnicodeUTF8), recipe.compute_OG())
    resultHtml += '<tr><td>%s</td><td>%.3f</td></tr>' % (QCoreApplication.translate("Export", "Densité finale : ", None, QCoreApplication.UnicodeUTF8), recipe.compute_FG())
    resultHtml += '<tr><td>%s</td><td>%.0f EBC</td></tr>' % (QCoreApplication.translate("Export", "Teinte : ", None, QCoreApplication.UnicodeUTF8), recipe.compute_EBC())
    resultHtml += '<tr><td>%s</td><td>%.0f IBU</td></tr>' % (QCoreApplication.translate("Export", "Amertume : ", None, QCoreApplication.UnicodeUTF8), recipe.compute_IBU())
    resultHtml += '<tr><td>%s</td><td>%.1f</td></tr>' % (QCoreApplication.translate("Export", "Ratio BU/GU : ", None, QCoreApplication.UnicodeUTF8), recipe.compute_ratioBUGU())
    resultHtml += '<tr><td>%s</td><td>%.1f %%</td></tr>' % (QCoreApplication.translate("Export", "Alcool (vol) : ", None, QCoreApplication.UnicodeUTF8), recipe.compute_ABV())
    resultHtml += '</table>'

    #Ingredients informations
    resultHtml += '<h2>%s %.1f %s</h2>' % (
        QCoreApplication.translate("Export", "Ingrédients prévus pour un brassin de", None, QCoreApplication.UnicodeUTF8),
        recipe.volume, QCoreApplication.translate("Export", "litres", None, QCoreApplication.UnicodeUTF8))

    #Grains
    resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Grains et sucres", None, QCoreApplication.UnicodeUTF8)
    resultHtml += '<table class="ingredients">'
    for f in recipe.listeFermentables:
        use = QCoreApplication.translate("Export", "Ajout après ébullition", None, QCoreApplication.UnicodeUTF8) if f.useAfterBoil else ''
        resultHtml += '<tr><td>%.0f g</td><td>%s</td><td>%s</td></tr>' % (f.amount, f.name, use)
    resultHtml += '</table>'

    #Houblons
    resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Houblons", None, QCoreApplication.UnicodeUTF8)
    resultHtml += '<table class="ingredients">'
    for h in recipe.listeHops:
        hUI = HopView(h)
        resultHtml += '<tr>'
        resultHtml += '<td>%.0f g</td>' % h.amount
        resultHtml += '<td>%s (α %.1f %%, %s)</td>' % (h.name, h.alpha, hUI.hopFormDisplay())
        resultHtml += '<td>%.0f min (%s)</td>' % (h.time, hUI.hopUseDisplay())

        resultHtml += '</tr>'
    resultHtml += '</table>'

    #Ingredients divers
    if len(recipe.listeMiscs) > 0:
        resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Ingrédients divers", None, QCoreApplication.UnicodeUTF8)
        resultHtml += '<table class="ingredients">'
        for m in recipe.listeMiscs:
            mUI = MiscView(m)
            resultHtml += '<tr>'
            resultHtml += '<td>%.0f g</td>' % m.amount
            resultHtml += '<td>%s (%s)</td>' % (m.name, m.type)
            resultHtml += '<td>%.0f min (%s)</td>' % (m.time, mUI.miscUseDisplay())
            resultHtml += '</tr>'
        resultHtml += '</table>'

    #Levures
    resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Levures", None, QCoreApplication.UnicodeUTF8)
    resultHtml += '<table class="ingredients">'
    for y in recipe.listeYeasts:
        yUI = YeastView(y)
        resultHtml += '<tr>'   
        resultHtml += '<td>%s</td>' %yUI.yeastDetailDisplay()
        resultHtml += '</tr>'
    resultHtml += '</table>'

    #Brassage informations
    resultHtml += '<h2>%s</h2>' % QCoreApplication.translate("Export", "Brassage", None, QCoreApplication.UnicodeUTF8)
    resultHtml += '<p>%s<br />pH : %s</p>' % (recipe.mash.name, recipe.mash.ph)

    #Etapes brassage
    resultHtml += '<p>'
    resultHtml += '<b>%s</b><br />' % QCoreApplication.translate("Export", "Étapes : ", None, QCoreApplication.UnicodeUTF8)
    for step in recipe.mash.listeSteps:
        mashStepUI = MashStepView(step)
        resultHtml += '%s : %s %s %s %s °C %s %s %s<br />' % (step.name,
                                                           QCoreApplication.translate("Export", "palier de type", None, QCoreApplication.UnicodeUTF8),
                                                           mashStepUI.mashTypeDisplay(),
                                                           QCoreApplication.translate("Export", "à", None, QCoreApplication.UnicodeUTF8), step.temp,
                                                           QCoreApplication.translate("Export", "pendant", None, QCoreApplication.UnicodeUTF8), step.time,
                                                           QCoreApplication.translate("Export", "minutes", None, QCoreApplication.UnicodeUTF8))
    resultHtml += '</p>'

    #Rincage
    resultHtml += '<p><b>%s</b>%s °C</p>' % (QCoreApplication.translate("Export", "Rinçage : ", None, QCoreApplication.UnicodeUTF8), recipe.mash.spargeTemp)

    #Notes
    if recipe.recipeNotes is not None:
        resultHtml += '<h2>%s</h2><pre>%s</pre>' % (QCoreApplication.translate("Export", "Notes", None, QCoreApplication.UnicodeUTF8), recipe.recipeNotes)

    resultHtml += '</body></html>'

    return resultHtml
