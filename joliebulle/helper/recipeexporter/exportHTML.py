#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.0
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

from view.fermentableview import *
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
<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">
    <style>
body {background:url(images/furley_bg.png);}
.beer-profile{width:800px;margin:auto;padding-top:0.5em;padding-bottom:1em;}
.beer-profile h1{color:#999;font-weight:bold;margin:auto;padding-top:0.1em; font-size:24px ;float:left;}
.beer-profile span{padding-right:20px; color:#999;font-weight:bold;padding-top:0.7em;float:right;}
.beer-profile-last{margin-right: -15px;}
.part-container{margin:auto;margin-top:3em; margin-bottom:3em; background-color: white; width:800px;border: 1px solid rgba(0, 0, 0, 0.1);box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);}
.tools{margin:auto;margin-top:3em;width:800px;margin-bottom:-2.5em;text-align:right;}
.tools button {background:none; border:none; color:#999;margin-left:15px;padding:0;padding-right: 3px;}
.tools button:hover{color:#333333;}
.info{padding-bottom:1.25em; padding-top:1.25em; text-align:center;}
.info-titre{display: block;text-transform: uppercase;color:#777; font-size:0.8em;}
.grains{padding-left: 50px;padding-right: 50px;}
.grains a {color:#333333;}
.grains h3 {margin-bottom:1em;}
.hops{padding-left: 50px;padding-right: 50px;}
.hops a {color:#333333;}
.hops h3 {margin-bottom:1em;}
.miscs{padding-left:50px;padding-right: 50px;}
.miscs a {color:#333333;}
.miscs h3 {margin-bottom:1em;}
.yeasts{padding-left: 50px;padding-right: 50px;}
.yeasts a {color:#333333;}
.yeasts h3 {margin-bottom:1em;}
.profile{padding-left: 50px;padding-right: 50px;}
.profile a {color:#333333;}
.profile h3 {margin-bottom:1em;}
.notes{padding-left: 50px;padding-right: 50px;}
.notes a {color:#333333;}
.notes h3 {margin-bottom:1em;}
.notes pre{border:none;background:none;font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;font-size: 14px;white-space: pre-wrap;}
.ingredients{text-align:left; margin-bottom:2em;}
.ingredients td {min-width: 200px;}
.context{display:inline-block;width:150px;padding: 0.5em 0.5em 0.5em 0.5em;}
.label-step{background-color:#a1b5bf;padding:0.2em 0.5em 0.2em 0.5em;color:white; font-size:85%%; font-weight: bold;}
.label-sparge{background-color:#a1b5bf;padding:0.2em 0.5em 0.2em 0.5em;color:white; font-size:85%%; font-weight: bold;}
#brewChart {margin-top:2.5em; }

    </style>
</head>
<body onload="createChart();">
''' %(recipe.name)    

    #Navbar
    resultHtml += '''<div class="beer-profile">
                        <h1>%s</h1> 
                        <span class="beer-profile-last" data-toggle="tooltip" data-placement="bottom" title="%s">%s %.1f%%</span> 
                        <span data-toggle="tooltip" data-placement="bottom" title="%s">%s %.1f</span>      
                        <span data-toggle="tooltip" data-placement="bottom" title="%s">%s %.3f</span>
                        <span data-toggle="tooltip" data-placement="bottom" title="%s">%s %.3f</span>
                        <span data-toggle="tooltip" data-placement="bottom" title="%s">%.0f %s</span> 
                        <span data-toggle="tooltip" data-placement="bottom" title="%s">%.0f %s</span>

                    </div>''' % (recipe.name,QCoreApplication.translate("Export", "Taux d'alcool", None, QCoreApplication.UnicodeUTF8),QCoreApplication.translate("Export", "Alc", None, QCoreApplication.UnicodeUTF8), recipe.compute_ABV(), QCoreApplication.translate("Export", "Ratio amertume/densité", None, QCoreApplication.UnicodeUTF8),QCoreApplication.translate("Export", "BU/GU", None, QCoreApplication.UnicodeUTF8),recipe.compute_ratioBUGU(), QCoreApplication.translate("Export", "Densité finale", None, QCoreApplication.UnicodeUTF8),QCoreApplication.translate("Export", "DF", None, QCoreApplication.UnicodeUTF8),recipe.compute_FG(), QCoreApplication.translate("Export", "Densité initiale", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export", "DI", None, QCoreApplication.UnicodeUTF8),recipe.compute_OG(), QCoreApplication.translate("Export", "Teinte", None, QCoreApplication.UnicodeUTF8),recipe.compute_EBC(),QCoreApplication.translate("Export", "EBC", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export", "Amertume", None, QCoreApplication.UnicodeUTF8),recipe.compute_IBU(),QCoreApplication.translate("Export", "IBU", None, QCoreApplication.UnicodeUTF8),)



    #Ingredients informations
    # resultHtml += '<h2>%s %.1f %s</h2>' % (
    #     QCoreApplication.translate("Export", "Ingrédients prévus pour un brassin de", None, QCoreApplication.UnicodeUTF8),
    #     recipe.volume, QCoreApplication.translate("Export", "litres", None, QCoreApplication.UnicodeUTF8))

    #Outils
    resultHtml += '''<div class="tools">
                        <button type="button" value="edit" onClick="main.editCurrentRecipe()"><i class="icon-wrench"></i> %s</button> <button type="button" value="brewday" onClick="main.switchToBrewday()"><i class="icon-dashboard"></i> %s</button>
                    </div>'''%(QCoreApplication.translate("Export", "Editer la recette", None, QCoreApplication.UnicodeUTF8),QCoreApplication.translate("Export", "Mode brassage", None, QCoreApplication.UnicodeUTF8))

    # resultHtml += ''' <button type="button" class="btn btn-link">Editer la recette</button> <button type="button" class="btn btn-link">Mode brassage</button>'''

    resultHtml += '''<div class="part-container info">
                        <span class="context"><span class="info-titre">%s</span>%s</span>
                        <span class="context"><span class="info-titre">%s</span>%.1f%%</span>
                        <span class="context"><span class="info-titre">%s</span>%.1fL</span>
                        <span class="context"><span class="info-titre">%s</span>%.0f min</span>
                    </div>''' % (QCoreApplication.translate("Export", "Style", None, QCoreApplication.UnicodeUTF8),recipe.style, QCoreApplication.translate("Export", "Rendement", None, QCoreApplication.UnicodeUTF8),recipe.efficiency, QCoreApplication.translate("Export", "Volume", None, QCoreApplication.UnicodeUTF8),recipe.volume, QCoreApplication.translate("Export", "Ebullition", None, QCoreApplication.UnicodeUTF8), recipe.boil)

    #Grains
    resultHtml += '<div class="part-container grains">'
    resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Grains et sucres", None, QCoreApplication.UnicodeUTF8)
    resultHtml += '<table class="ingredients">'
    for f in recipe.listeFermentables:
        fUI=FermentableView(f)
        use = QCoreApplication.translate("Export", "Ajout après ébullition", None, QCoreApplication.UnicodeUTF8) if f.useAfterBoil else ''
        resultHtml += '<tr><td><span data-toggle="popover" data-trigger="hover" data-html="true" data-content="%s : %0.f <br/> %s : %0.f%% <br/> %s : %s " data-placement="bottom"><a>%s</a></span></td><td>%.0f g</td><td>%s</td></tr>' % (QCoreApplication.translate("Export", "EBC", None, QCoreApplication.UnicodeUTF8),f.color,QCoreApplication.translate("Export", "Rendement", None, QCoreApplication.UnicodeUTF8), f.fyield, QCoreApplication.translate("Export", "Type", None, QCoreApplication.UnicodeUTF8),fUI.fermentableTypeDisplay(), f.name, f.amount, use)
    resultHtml += '</table></div>'


    #Houblons
    resultHtml += '<div class="part-container hops">'
    resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Houblons", None, QCoreApplication.UnicodeUTF8)
    resultHtml += '<table class="ingredients">'
    for h in recipe.listeHops:
        hUI = HopView(h)
        resultHtml += '<tr>'
        resultHtml += '<td><span data-toggle="popover" data-trigger="hover" data-html="true" data-placement="bottom" data-content="α : %.1f%% <br/> %s : %s <br/> %s : %.1f IBU"><a>%s</a></span></td>' % (h.alpha,QCoreApplication.translate("Export", "Forme", None, QCoreApplication.UnicodeUTF8),hUI.hopFormDisplay(),QCoreApplication.translate("Export", "Proportion", None, QCoreApplication.UnicodeUTF8),recipe.compute_IBUPart()[h],h.name)
        resultHtml += '<td>%.0f g</td>' % h.amount
        # resultHtml += '<td>%s (α %.1f %%, %s)</td>' % (h.name, h.alpha, hUI.hopFormDisplay())
        resultHtml += '<td>%.0f min (%s)</td>' % (h.time, hUI.hopUseDisplay())

        resultHtml += '</tr>'
    resultHtml += '</table></div>'

    #Ingredients divers
    if len(recipe.listeMiscs) > 0:
        resultHtml += '<div class="part-container miscs">'
        resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Ingrédients divers", None, QCoreApplication.UnicodeUTF8)
        resultHtml += '<table class="ingredients">'
        for m in recipe.listeMiscs:
            mUI = MiscView(m)
            resultHtml += '<tr>'
            resultHtml += '<td><span <span data-toggle="popover" data-trigger="hover" data-html="true" data-placement="bottom" data-content="%s : %s"><a>%s</a></span></td>' % (QCoreApplication.translate("Export", "Type", None, QCoreApplication.UnicodeUTF8),mUI.miscTypeDisplay(),m.name)
            resultHtml += '<td>%.0f g</td>' % m.amount
            resultHtml += '<td>%.0f min (%s)</td>' % (m.time, mUI.miscUseDisplay())
            resultHtml += '</tr>'
        resultHtml += '</table></div>'

    #Levures
    resultHtml += '<div class="part-container yeasts">'
    resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Levures", None, QCoreApplication.UnicodeUTF8)
    resultHtml += '<table class="ingredients">'
    for y in recipe.listeYeasts:
        yUI = YeastView(y)
        resultHtml += '<tr>'   
        resultHtml += '<td data-toggle="popover" data-trigger="hover" data-html="true" data-placement="bottom" data-content="%s : %0.f%% <br/> %s : %s"><a>%s</a></td>' % (QCoreApplication.translate("Export", "Atténuation", None, QCoreApplication.UnicodeUTF8),y.attenuation,QCoreApplication.translate("Export", "Forme", None, QCoreApplication.UnicodeUTF8),yUI.yeastFormDisplay(),yUI.yeastDetailDisplay())
        resultHtml += '</tr>'
    resultHtml += '</table></div>'

    #Brassage informations
    resultHtml += '<div class="part-container profile">'
    resultHtml += '<h3 class="brassage-title">%s</h3>' % QCoreApplication.translate("Export", "Brassage", None, QCoreApplication.UnicodeUTF8)
    resultHtml += '<p class="brassage-profil"><b>%s</b></p><p>pH : %s</p>' % (recipe.mash.name, recipe.mash.ph)

    #Etapes brassage
    stepsNameString=''
    stepsTempString=''
    for step in recipe.mash.listeSteps:
        mashStepUI = MashStepView(step)
        #la chaine utilisée pour le graphique :
        stepsNameString += '''"%s (%s min)", "",''' %(step.name, step.time)
        stepsTempString += '''%s, %s, ''' %(step.temp,step.temp)
        resultHtml += '<p><span class="label-step">%s</span> %s %s %s %s °C %s %s %s</p>' % (step.name,
                                                           QCoreApplication.translate("Export", "palier de type", None, QCoreApplication.UnicodeUTF8),
                                                           mashStepUI.mashTypeDisplay(),
                                                           QCoreApplication.translate("Export", "à", None, QCoreApplication.UnicodeUTF8), step.temp,
                                                           QCoreApplication.translate("Export", "pendant", None, QCoreApplication.UnicodeUTF8), step.time,
                                                           QCoreApplication.translate("Export", "minutes", None, QCoreApplication.UnicodeUTF8))

    

    #Rincage
    resultHtml += '<p><span class="label-sparge">%s</span> %s °C</p>' % (QCoreApplication.translate("Export", "Rinçage", None, QCoreApplication.UnicodeUTF8), recipe.mash.spargeTemp)

    #Canvas
    resultHtml += '''<p><canvas id="brewChart" width="400" height="300"></canvas></p>'''
    resultHtml += '</div>'

    #Notes
    if recipe.recipeNotes is not None:
        resultHtml += '<div class="part-container notes">'
        resultHtml += '<h3>%s</h3><pre>%s</pre>' % (QCoreApplication.translate("Export", "Notes", None, QCoreApplication.UnicodeUTF8), recipe.recipeNotes)
        resultHtml += '</div>'
    

    #Le javascript
    resultHtml += '''<script src="jquery/jquery.js"></script>
                     <script src="bootstrap/js/bootstrap.min.js"></script>
                     <script src="chartjs/Chart.js"></script>'''

    #Tooltips
    resultHtml += ''' <script type="text/javascript">
                    $(function () {
                    $("[data-toggle='tooltip']").tooltip();
                    });
                    </script>'''
                    
    #Popovers
    resultHtml += ''' <script type="text/javascript">
                    $(function () {
                    $("[data-toggle='popover']").popover();
                    });
                    </script>'''

    #Graphique
    resultHtml += '''     <script type="text/javascript">
function createChart()
        {
            //Get the context of the canvas element we want to select
            var ctx = document.getElementById("brewChart").getContext("2d");
 
            //Create the data object to pass to the chart
            var data = {
                labels : [%s],
                datasets : [
                            {
                                fillColor : "rgba(220,220,220,0.5)",
                                strokeColor : "rgba(220,220,220,1)",
                                pointColor : "rgba(220,220,220,1)",
                                pointStrokeColor : "#fff",
                                data : [%s]
                            },
                        ]
                      };
 
            //The options we are going to pass to the chart
            options = {
                            bezierCurve : false,
                            scaleOverride : true,
                            //Number - The number of steps in a hard coded scale
                            scaleSteps : 12,
                            //Number - The value jump in the hard coded scale
                            scaleStepWidth : 1,
                            //Number - The scale starting value
                            scaleStartValue : 65,
                            
            };
 
            //Create the chart
            new Chart(ctx).Line(data, options);
        }
</script>''' %(stepsNameString,stepsTempString)

                

    resultHtml += '</body></html>'

    return resultHtml
