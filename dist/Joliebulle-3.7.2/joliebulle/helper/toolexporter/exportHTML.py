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

def exportHTML():
    resultHtml = '''
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="angular/angular.min.js"></script>
<script src="jquery/jquery.js"></script>
<script src="bootstrap/js/bootstrap.min.js"></script>
<script src="controllers/tools/main.js"></script>
<script src="controllers/tools/gravity.js"></script>
<script src="controllers/tools/steps.js"></script>
<script src="controllers/tools/alcool.js"></script>
<script src="controllers/tools/dilution.js"></script>
<script src="controllers/tools/boiloff.js"></script>
<script src="controllers/tools/decoction.js"></script>
<script src="controllers/tools/refractoalc.js"></script>
<script src="controllers/tools/sgplato.js"></script>
<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">
<link rel="stylesheet" href="css/sidebar.css">
<style>
    .header{width:100%%;min-height:55px;position:fixed;left:50px;z-index: 1000;background-color: #fff;padding-left:10px;border-bottom: 1px solid #eee;}
    .main{padding-top:0px; margin-left:75px;}
    .menu{text-align: right; color: #fff; font-size: 24px;float:right;margin: auto; margin-top:90px;margin-right: 75px; padding:0em 0.3em 0em 0.3em; background-color:#3498db;}
    .menu i:hover{color:;}
    .menu ul{text-align: left;}
    .tools-header {margin-left:120px;margin-top:45px;}
    .tools-header h1 {font-size:1.75em; color:#444;padding-bottom:0px;margin-top:0;padding-left:10px;}
    .tool-block {margin-top:3em; margin-bottom:1em; margin-right: 60px; background-color: white; border: 1px solid #ddd; padding: 50px;padding-top: 0;}
    .tool-block label {font-weight:bold; color:#666;}
    h3{margin-bottom: 2em;}
    .tool-result{margin-top:4em;}
    .last{margin-bottom: 3em;}
    .row-tools{padding-left: 15px; padding-right: 15px;}
.tool-result{margin-top:4em;}
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;}
</style>
</head>'''

    resultHtml +=''' <body ng-app="tools">

    <div class="container-fluid">

    	<div class="sidebar">
<!--
            <div class="nav-header"></div>
-->
            <ul class="nav nav-sidebar">
              <li onClick="main.showLib()"><a href="#"><i class="fa fa-flask"></i> </a></li>
              <li onClick="main.showJournal()"><a href="#"><i class="fa fa-calendar-o"></i> </a></li>
              <li class="active" onClick="main.showTools()"><a href="#"><i class="fa fa-cog"></i> </a></li>
            </ul>
        </div>

        <div class="header">

        </div>
        <div class="row">

            <div class="menu btn-group col-sm-offset-7">
                <i class="fa fa-bars" data-toggle="dropdown"></i>
                <ul class="dropdown-menu pull-right" role="menu">
                                <li><a href="#gravity">{1}</a></li>
                                <li><a href="#step">{2}</a></li>
                                <li><a href="#alc">{3}</a></li>
                                <li><a href="#dilution">{4}</a></li>
                                <li><a href="#boiloff">{5}</a></li>
                                <li><a href="#decoc">{6}</a></li>
                                <li><a href="#sg">{7}</a></li>
                                <li><a href="#refractoalc">{8}</a></li>
                              </ul>

            </div>
        </div>''' .format(QCoreApplication.translate("Export","Outils"), QCoreApplication.translate("Export","Correction du densimètre"), QCoreApplication.translate("Export","Assistant paliers"), QCoreApplication.translate("Export","Taux d'alcool"), QCoreApplication.translate("Export","Dilution"), QCoreApplication.translate("Export","Evaporation"), QCoreApplication.translate("Export","Décoction"), QCoreApplication.translate("Export","Densité - Plato"),QCoreApplication.translate("Export","Densité finale - Plato (avec alcool)"))



    resultHtml+='''
    <div class="main">
    <div class="row row-tools" id="gravity">
            <div ng-controller="GravityToolCtrl" class="tool-block">
                <h3>{0}</h3>
                <form class="form-horizontal" role="form">
                <div class="form-group">
                    <label class="col-sm-3 control-label">{1}</label>
                    <div class="col-sm-2">
                        <input type="number" min="1.000" max="1.999" step="0.001" ng-model="measuredGravity" class="form-control">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{2}</label>
                    <div class="col-sm-2">
                        <input type="number" min="0" max="100" step="1" ng-model="calibTemp" class="form-control">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{3}</label>
                    <div class="col-sm-2">
                        <input type="number" min="0" max="110" step="1" ng-model="sampleTemp" class="form-control">
                    </div>
                </div>
                <div class="form-group tool-result">
                    <label class="col-sm-3 control-label">{4}</label>
                    <div class="col-sm-2">
                        <label class="control-label">{5}</label>
                    </div>
                </div>
                </form>
            </div>
        </div>''' .format(QCoreApplication.translate("Export","Correction du densimètre"),QCoreApplication.translate("Export","Densité mesurée"),QCoreApplication.translate("Export","Température de calibration (°C)"), QCoreApplication.translate("Export","Température mesurée (°C)"),QCoreApplication.translate("Export","Densité corrigée"), "{{calcGravity()}}")


    resultHtml+='''<div class="row row-tools" id="step">
            <div ng-controller="StepAssistantCtrl" class="tool-block">
                <h3>{0}</h3>
                <form class="form-horizontal" role="form">
                    <div class="form-group">
                        <label class="col-sm-3 control-label">Mode</label>
                        <div class="col-sm-3">
                            <select ng-model="stepType" ng-options="type for type in stepTypes " class="form-control"></select>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-3 control-label">{1}</label>
                        <div class="col-sm-3">
                            <input type="number" min="1.000" max="100" step="1" ng-model="targetTemp" class="form-control">
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-3 control-label">{2}</label>
                        <div class="col-sm-3">
                            <input type="number" min="0" max="10000" step="1" ng-model="addedVolume" class="form-control">
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-3 control-label">{3}</label>
                        <div class="col-sm-3">
                            <input type="number" min="0" max="10000" step="1" ng-model="grainWeight" class="form-control">
                        </div>
                    </div>
                    <div class="form-group" ng-hide="stepType=='Palier'">
                        <label class="col-sm-3 control-label">{4}</label>
                        <div class="col-sm-3">
                            <input type="number" min="0.1" max="100" step="1" ng-model="grainTemp" class="form-control">
                        </div>
                    </div>
                    <div class="form-group" ng-hide="stepType=='Empâtage'">
                        <label class="col-sm-3 control-label">{5}</label>
                        <div class="col-sm-3">
                            <input type="number" min="0.1" max="100" step="1" ng-model="mashTemp" class="form-control">
                        </div>
                    </div>
                    <div class="form-group" ng-hide="stepType=='Empâtage'">
                        <label class="col-sm-3 control-label">{6}</label>
                        <div class="col-sm-3">
                            <input type="number" min="0" max="10000" step="1" ng-model="waterVolumeMash" class="form-control">
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-3 control-label">{7}</label>
                        <div class="col-sm-3">
                            <input type="number" min="0" max="100" step="1" ng-model="factor" class="form-control">
                        </div>
                    </div>
                    <div class="form-group tool-result">
                    <label class="col-sm-3 control-label">{8}</label>
                    <div class="col-sm-3">
                        <label class="control-label">{9}</label>
                    </div>
                    </div>
                    <div class="form-group">
                    <label class="col-sm-3 control-label">{10}</label>
                    <div class="col-sm-3">
                        <label class="control-label">{11}</label>
                    </div>
                    </div>
                </form>
            </div>
        </div>''' .format(QCoreApplication.translate("Export","Assistant paliers"), QCoreApplication.translate("Export","Température cible (°C)"), QCoreApplication.translate("Export","Volume ajouté (L)"), QCoreApplication.translate("Export","Poids du grain (Kg)"),QCoreApplication.translate("Export","Température du grain (°C)"),QCoreApplication.translate("Export","Température de la maîche (°C)"),QCoreApplication.translate("Export","Volume d'eau dans la maîche (L)"),QCoreApplication.translate("Export","Facteur de correction"),QCoreApplication.translate("Export","Température de l'eau (°C)"),"{{waterTemp().temp}}",QCoreApplication.translate("Export","Ratio (L/Kg)"),"{{waterTemp().ratio}}")



    resultHtml+='''<div class="row row-tools" id="alc">
            <div ng-controller="AlcToolCtrl" class="tool-block">
                <h3>{0}</h3>
                <form class="form-horizontal" role="form">
                <div class="form-group">
                    <label class="col-sm-3 control-label">{1}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0.001" max="100" step="0.001" ng-model="originalGravity">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{2}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0.001" max="100" step="0.001" ng-model="finalGravity">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{3}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="100000" step="1" ng-model="addedSugar">
                    </div>
                </div>
                <div class="form-group tool-result">
                    <label class="col-sm-3 control-label">{4}</label>
                    <div class="col-sm-2">
                        <label class="control-label">{5}</label>
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{6}</label>
                    <div class="col-sm-2">
                        <label class="control-label">{7}</label>
                    </div>
                </div>
                </form>
            </div>
        </div>'''.format(QCoreApplication.translate("Export","Taux d'alcool"),QCoreApplication.translate("Export","Densité initiale"),QCoreApplication.translate("Export","Densité finale"), QCoreApplication.translate("Export","Sucre ajouté (g/L)"),QCoreApplication.translate("Export","Alcool par volume (%)"),"{{calcAlcoolVol()}}",QCoreApplication.translate("Export","Atténuation apparente"), "{{calcAppAttenuation()}}")



    resultHtml+='''<div class="row row-tools" id="dilution">
            <div ng-controller="DilutionToolCtrl" class="tool-block">
                <h3>{0}</h3>
                <form class="form-horizontal" role="form">
                <div class="form-group">
                    <label class="col-sm-3 control-label">{1}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10000000" step="1" ng-model="initialVol">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label" >{2}</label>
                    <div class="col-sm-2">
                        <input type="number"  class="form-control" min="0.001" max="100" step="0.001" ng-model="initialGravity">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{3}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10000000" step="1" ng-model="addedVolume">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{4}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0.001" max="100" step="0.001" ng-model="addedGravity">
                    </div>
                    <p class="help-block col-sm-3">{5}</p>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{6}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10000000" step="1" ng-change="finalVolChanged()" ng-model="finalVol">
                    </div>
                </div>
                <div class="form-group tool-result">
                    <label class="col-sm-3 control-label">{7}</label>
                    <div class="col-sm-2">
                        <label class="control-label">{8}</label>
                    </div>
                </div>
                </form>
            </div>
        </div>'''.format(QCoreApplication.translate("Export","Dilution"),QCoreApplication.translate("Export","Volume initial (L)"),QCoreApplication.translate("Export","Densité spécifique initiale"),QCoreApplication.translate("Export","Volume ajouté (L)"),QCoreApplication.translate("Export","Densité de l'ajout"),QCoreApplication.translate("Export","1 si ajout d'eau"),QCoreApplication.translate("Export","Volume final (L)"),QCoreApplication.translate("Export","Densité spécifique finale"),"{{calcDilution()}}")


    resultHtml+='''<div class="row row-tools" id="boiloff">
            <div ng-controller="BoiloffToolCtrl" class="tool-block">
                <h3>{0}</h3>
                <form class="form-horizontal" role="form">
                <div class="form-group">
                    <label class="col-sm-3 control-label">{1}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10000000" step="1" ng-model="preboilVol">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label" >{2}</label>
                    <div class="col-sm-2">
                        <input type="number"  class="form-control" min="0.001" max="100" step="0.001" ng-model="preboilGravity">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{3}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10000000" step="1" ng-model="boilOffRate">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{4}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="1" max="100000" step="10" ng-model="boilTime">
                    </div>

                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{5}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10000000" step="1" ng-change="" ng-model="coolingLoss">
                    </div>
                </div>
                <div class="form-group tool-result">
                    <label class="col-sm-3 control-label">{6}</label>
                    <div class="col-sm-2">
                        <label class="control-label">{7}</label>
                    </div>
                </div>
                <div class="form-group ">
                    <label class="col-sm-3 control-label">{8}</label>
                    <div class="col-sm-2">
                        <label class="control-label">{9}</label>
                    </div>
                </div>
                <div class="form-group ">
                    <label class="col-sm-3 control-label">{10}</label>
                    <div class="col-sm-2">
                        <label class="control-label">{11}</label>
                    </div>
                </div>
                <div class="form-group ">
                    <label class="col-sm-3 control-label">{12}</label>
                    <div class="col-sm-2">
                        <label class="control-label">{13}</label>
                    </div>
                </div>
                </form>
            </div>
        </div>''' .format(QCoreApplication.translate("Export","Evaporation"),
            QCoreApplication.translate("Export","Volume pré-ébullition (L)"),
            QCoreApplication.translate("Export","Densité spécifique pré-ébullition"),
            QCoreApplication.translate("Export","Taux d'évaporation (%/heure)"),
            QCoreApplication.translate("Export","Durée d'ébullition (min)"),
            QCoreApplication.translate("Export","Pertes par refroidissement (%)"),
            QCoreApplication.translate("Export","Volume évaporé (ébullition) (L)"),
            "{{calcBoilOff().boilOffVol}}",
            QCoreApplication.translate("Export","Volume évaporé (refroidissement) (L)"),
            "{{calcBoilOff().coolingLoss}}",
            QCoreApplication.translate("Export","Volume final (L)"),
            "{{calcBoilOff().finalVol}}",
            QCoreApplication.translate("Export","Densité spécifique"),
            "{{calcBoilOff().finalSg}}")


    resultHtml+='''<div class="row row-tools" id="decoc">
            <div ng-controller="DecocToolCtrl" class="tool-block">
                <h3>{0}</h3>
                <form class="form-horizontal" role="form">
                <div class="form-group">
                    <label class="col-sm-3 control-label">{1}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="100000" step="1" ng-model="mashVol">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{2}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="100" step="1" ng-model="targetTemp">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{3}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="100000" step="1" ng-model="startTemp">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{4}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="1000" step="1" ng-model="boilTemp">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{5}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="1000" step="1" ng-model="correction">
                    </div>
                </div>
                <div class="form-group tool-result">
                    <label class="col-sm-3 control-label">{6}</label>
                    <div class="col-sm-2">
                        <label class="control-label">{7}</label>
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{8}</label>
                    <div class="col-sm-2">
                        <label class="control-label">{9}</label>
                    </div>
                </div>
                </form>
            </div>
        </div>'''.format(QCoreApplication.translate("Export","Décoction"),
            QCoreApplication.translate("Export","Volume de moût (L)"),
            QCoreApplication.translate("Export","Température cible (°C)"),
            QCoreApplication.translate("Export","Température de départ (°C)"),
            QCoreApplication.translate("Export","Température d'ébullition (°C)"),
            QCoreApplication.translate("Export","Facteur de correction (%)"),
            QCoreApplication.translate("Export","Volume de décoction (L)"),
            "{{calcDecoction().decocVol}}",
            QCoreApplication.translate("Export","Fraction du moût (%)"),
            "{{calcDecoction().fraction}}"
            )


    resultHtml+='''<div class="row row-tools last" id="sg">
            <div ng-controller="SgPlatoToolCtrl" class="tool-block">
                <h3>{0}</h3>
                <form class="form-horizontal" role="form">
                <div class="form-group">
                    <label class="col-sm-3 control-label">{1}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10" step="0.001" ng-model="specificGravity" ng-change="sgChanged()">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{2}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10" step="0.01" ng-model="wortFactor" ng-change="wortFactorChanged()">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{3}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="100" step="1" ng-model="plato" ng-change="platoChanged()">
                    </div>
                </div>
                </form>
            </div>
        </div>''' .format(QCoreApplication.translate("Export","Densité spécifique - Plato"),
            QCoreApplication.translate("Export","Densité spécifique"), QCoreApplication.translate("Export","Facteur de correction"), QCoreApplication.translate("Export","Plato"))

    resultHtml+='''<div class="row row-tools last" id="refractoalc">
            <div ng-controller="RefractoAlcToolCtrl" class="tool-block">
                <h3>{0}</h3>
                <form class="form-horizontal" role="form">
                <div class="form-group">
                    <label class="col-sm-3 control-label">{1}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="100" step="0.1" ng-model="originalRi" >
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{2}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="100" step="0.1" ng-model="finalRi" >
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{3}</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10" step="0.01" ng-model="wortFactor" >
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">{4}</label>
                    <div class="col-sm-2">
                        <label class="control-label">{5}</label>
                    </div>
                </div>
                </form>
            </div>
        </div>'''.format(QCoreApplication.translate("Export","Densité spécifique - Plato (avec alcool)"), QCoreApplication.translate("Export","Plato (original)"), QCoreApplication.translate("Export","Plato (final)"), QCoreApplication.translate("Export","Facteur de correction"), QCoreApplication.translate("Export","Densité finale"), "{{calcFgRefracto()}}")


    resultHtml+='''
    <!-- Fin container -->
    </div>

{0}
</body>
</html>''' .format(
'''            <script type="text/javascript">
                                $(function () {
                                $("[data-toggle='dropdown']").dropdown();
                                });
            </script> '''
            )

    return resultHtml
