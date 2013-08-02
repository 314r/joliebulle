#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#JolieBulle 2.9
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
<link rel="stylesheet" href="bootstrap/css/bootstrap.css">
<style type="text/css">
.container,
.navbar-static-top .container,
.navbar-fixed-top .container,
.navbar-fixed-bottom .container {width: 800px;}
body {padding-top : 60px;color: #222; font-size:80%%; background-color : white;}
h1,h2,h3,h4,h5,h6 { font-weight: normal; color: #111; }
/*h1 { font-size: 2em; margin-bottom: 0; text-align:center;}*/
h2 { font-size: 1.5em; line-height: 1; margin-bottom: 2em; margin-top:2em; padding-bottom:0.75em; padding-top:0.75em;border-bottom:solid 1px #ddd;clear:both;}
h3 { font-size: 1.2em; line-height: 1.25; margin-bottom: 1.25em; text-align:left; background-color:#eeeeee; border-bottom:1px solid #cccccc; border-top:1px solid #cccccc; padding:0.5em 0 0.5em 0.5em;}
ul{list-style-type: none;text-align:left;}
pre {white-space: pre-wrap;font-size:1.25em;}
.genre {font-style:italic; text-align:center;color:#ddd;margin-top:0;padding-top:0;border:0;border-bottom:solid 1px #ddd;}
.profil{text-align:left;margin-bottom:1em; width:400px;background:url(/Images/glade.png);}
.profil td {min-width: 200px;}
.ingredients{text-align:left; margin-bottom:2em;}
.ingredients td {min-width: 200px;}
.profilNav{padding-right: 2.5em;}
.context{padding-right: 2.5em;}
.info{margin-bottom:2.75em; margin-top:1.75em;}
.navbar-inner{background-color: white;background-image: none;}
.profil2{ text-align: center}
.navbar-inner .brand {color:#222;}
#brewChart {padding-top :1.5em;}
</style>
</head>
<body onload="createChart();">
''' % (recipe.name)

    #Profil
    # resultHtml += '<table class="profil">'
    # resultHtml += '<tr><td>%s</td><td>%.1f %%</td></tr>' % (QCoreApplication.translate("Export", "Rendement : ", None, QCoreApplication.UnicodeUTF8), recipe.efficiency)
    # resultHtml += '<tr><td>%s</td><td>%.0f min</td></tr>' % (QCoreApplication.translate("Export", "Ébullition : ", None, QCoreApplication.UnicodeUTF8), recipe.boil)
    # resultHtml += '<tr><td>%s</td><td>%.3f</td></tr>' % (QCoreApplication.translate("Export", "Densité initiale : ", None, QCoreApplication.UnicodeUTF8), recipe.compute_OG())
    # resultHtml += '<tr><td>%s</td><td>%.3f</td></tr>' % (QCoreApplication.translate("Export", "Densité finale : ", None, QCoreApplication.UnicodeUTF8), recipe.compute_FG())
    # resultHtml += '<tr><td>%s</td><td>%.0f EBC</td></tr>' % (QCoreApplication.translate("Export", "Teinte : ", None, QCoreApplication.UnicodeUTF8), recipe.compute_EBC())
    # resultHtml += '<tr><td>%s</td><td>%.0f IBU</td></tr>' % (QCoreApplication.translate("Export", "Amertume : ", None, QCoreApplication.UnicodeUTF8), recipe.compute_IBU())
    # resultHtml += '<tr><td>%s</td><td>%.1f</td></tr>' % (QCoreApplication.translate("Export", "Ratio BU/GU : ", None, QCoreApplication.UnicodeUTF8), recipe.compute_ratioBUGU())
    # resultHtml += '<tr><td>%s</td><td>%.1f %%</td></tr>' % (QCoreApplication.translate("Export", "Alcool (vol) : ", None, QCoreApplication.UnicodeUTF8), recipe.compute_ABV())
    # resultHtml += '</table>'

    #Navbar
    resultHtml += '''<div class="navbar navbar-fixed-top">
                        <div class="navbar-inner">
                            <div class="container">
                                <a class="brand" href="#">%s</a>
                                <div class="profil2 pull-right">                
                                    <span class="navbar-text profilNav" data-toggle="tooltip" data-placement="bottom" title="Amertume">%.0f IBU</span>
                                    <span class="navbar-text profilNav" data-toggle="tooltip" data-placement="bottom" title="Teinte">%.0f EBC</span>
                                    <span class="navbar-text profilNav" data-toggle="tooltip" data-placement="bottom" title="Densité initiale">DI %.3f</span>
                                    <span class="navbar-text profilNav" data-toggle="tooltip" data-placement="bottom" title="Densité finale">DF %.3f</span>
                                    <span class="navbar-text profilNav" data-toggle="tooltip" data-placement="bottom" title="Ratio BU/GU">BU/GU %.1f</span>
                                    <span class="navbar-text" data-toggle="tooltip" data-placement="bottom" title="Taux d'alcool">Alc %.1f%%</span>
                                </div>
                            </div>
                        </div>
                    </div>''' % (recipe.name,recipe.compute_IBU(), recipe.compute_EBC(), recipe.compute_OG(), recipe.compute_FG(),recipe.compute_ratioBUGU(),recipe.compute_ABV())



    #Ingredients informations
    # resultHtml += '<h2>%s %.1f %s</h2>' % (
    #     QCoreApplication.translate("Export", "Ingrédients prévus pour un brassin de", None, QCoreApplication.UnicodeUTF8),
    #     recipe.volume, QCoreApplication.translate("Export", "litres", None, QCoreApplication.UnicodeUTF8))

    #Container
    resultHtml += ''' <div class="container"> '''

    resultHtml += '''<div class="info">
                        <span class="context">Style : <span class="badge">%s</span></span>
                        <span class="context">Rendement : <span class="badge">%.1f%%</span></span>
                        <span class="context">Volume : <span class="badge">%.1fL</span></span>
                        <span class="context">Ebullition : <span class="badge">%.0f min</span></span>
                    </div>''' % (recipe.style, recipe.efficiency, recipe.volume, recipe.boil)

    #Grains
    resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Grains et sucres", None, QCoreApplication.UnicodeUTF8)
    resultHtml += '<table class="ingredients">'
    for f in recipe.listeFermentables:
        use = QCoreApplication.translate("Export", "Ajout après ébullition", None, QCoreApplication.UnicodeUTF8) if f.useAfterBoil else ''
        resultHtml += '<tr><td><span data-toggle="popover" data-trigger="hover" data-html="true" data-content="EBC : %0.f <br/> Rendement : %0.f%% <br/> Type : %s " data-placement="bottom"><a>%s</a></span></td><td>%.0f g</td><td>%s</td></tr>' % (f.color, f.fyield, f.type, f.name, f.amount, use)
    resultHtml += '</table>'

    #Houblons
    resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Houblons", None, QCoreApplication.UnicodeUTF8)
    resultHtml += '<table class="ingredients">'
    for h in recipe.listeHops:
        hUI = HopView(h)
        resultHtml += '<tr>'
        resultHtml += '<td><span data-toggle="popover" data-trigger="hover" data-html="true" data-placement="bottom" data-content="α : %.1f%% <br/> Forme : %s <br/> Etape : %s <br/> Proportion : %.1f IBU"><a>%s</a></span></td>' % (h.alpha,hUI.hopFormDisplay(),hUI.hopUseDisplay(),recipe.compute_IBUPart()[h],h.name)
        resultHtml += '<td>%.0f g</td>' % h.amount
        # resultHtml += '<td>%s (α %.1f %%, %s)</td>' % (h.name, h.alpha, hUI.hopFormDisplay())
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
            resultHtml += '<td><span <span data-toggle="popover" data-trigger="hover" data-html="true" data-placement="bottom" data-content="Type : %s"><a>%s</a></span></td>' % (m.type,m.name)
            resultHtml += '<td>%.0f g</td>' % m.amount
            resultHtml += '<td>%.0f min (%s)</td>' % (m.time, mUI.miscUseDisplay())
            resultHtml += '</tr>'
        resultHtml += '</table>'

    #Levures
    resultHtml += '<h3>%s</h3>' % QCoreApplication.translate("Export", "Levures", None, QCoreApplication.UnicodeUTF8)
    resultHtml += '<table class="ingredients">'
    for y in recipe.listeYeasts:
        yUI = YeastView(y)
        if y.form == "Liquid" :
            form = QCoreApplication.translate("Export", "Liquide", None, QCoreApplication.UnicodeUTF8)
        elif y.form == "Dry" : 
            form = QCoreApplication.translate("Export", "Sèche", None, QCoreApplication.UnicodeUTF8)
        elif y.form == "Culture" : 
            form = QCoreApplication.translate("Export", "Culture", None, QCoreApplication.UnicodeUTF8)
        elif y.form == "Slant" : 
            form = QCoreApplication.translate("Export", "Gélose", None, QCoreApplication.UnicodeUTF8)    
        resultHtml += '<span data-toggle="popover" data-trigger="hover" data-html="true" data-placement="bottom" data-content="Atténuation : %0.f%% <br/> Forme : %s"><a>%s</a></span><br />' % (y.attenuation,form,yUI.yeastDetailDisplay())
    resultHtml += '</table>'

    #Brassage informations
    resultHtml += '<h2>%s</h2>' % QCoreApplication.translate("Export", "Brassage", None, QCoreApplication.UnicodeUTF8)
    resultHtml += '<p><b>%s</b><br />pH : %s <br/></p>' % (recipe.mash.name, recipe.mash.ph)

    #Etapes brassage
    stepsNameString=''
    stepsTempString=''
    for step in recipe.mash.listeSteps:
        mashStepUI = MashStepView(step)
        #la chaine utilisée pour le graphique :
        stepsNameString += '''"%s (%s min)", "",''' %(step.name, step.time)
        stepsTempString += '''%s, %s, ''' %(step.temp,step.temp)
        resultHtml += '<p><span class="label label-info">%s</span> : %s %s %s %s °C %s %s %s</p>' % (step.name,
                                                           QCoreApplication.translate("Export", "palier de type", None, QCoreApplication.UnicodeUTF8),
                                                           mashStepUI.mashTypeDisplay(),
                                                           QCoreApplication.translate("Export", "à", None, QCoreApplication.UnicodeUTF8), step.temp,
                                                           QCoreApplication.translate("Export", "pendant", None, QCoreApplication.UnicodeUTF8), step.time,
                                                           QCoreApplication.translate("Export", "minutes", None, QCoreApplication.UnicodeUTF8))
    

    #Rincage
    resultHtml += '<p><span class="label label-inverse">%s</span> : %s °C</p>' % (QCoreApplication.translate("Export", "Rinçage", None, QCoreApplication.UnicodeUTF8), recipe.mash.spargeTemp)

    #Canvas
    resultHtml += '''<p><canvas id="brewChart" width="400" height="300"></canvas></p>'''

    #Notes
    if recipe.recipeNotes is not None:
        resultHtml += '<h2>%s</h2><pre>%s</pre>' % (QCoreApplication.translate("Export", "Notes", None, QCoreApplication.UnicodeUTF8), recipe.recipeNotes)

    
    #Fin div container
    resultHtml += ''' </div>'''

    #Le javascript
    resultHtml += '''<script src="jquery/jquery.js"></script>
                     <script src="bootstrap/js/bootstrap.js"></script>
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
