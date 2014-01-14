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




def exportHTML():
    resultHtml = '''
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="angular/angular.min.js"></script>
<script src="controllers/main.js"></script>
<script src="controllers/gravity.js"></script>
<script src="controllers/steps.js"></script>
<script src="controllers/alcool.js"></script>
<script src="controllers/dilution.js"></script>
<script src="controllers/boiloff.js"></script>
<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">


<style>
body {background:url(images/furley_bg.png);}
.tools-header {padding-top:0.5em;padding-bottom:1em;}
.tools-header h1 {color:#999;font-weight:bold;margin:auto;padding-top:0.1em; font-size:24px ;float:left;}
.tool-block {margin-top:3em; margin-bottom:1em; background-color: white; border: 1px solid rgba(0, 0, 0, 0.1);box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);padding: 50px;padding-top: 0;}
h3{margin-bottom: 2em;}
.tool-result{margin-top:4em;}


input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
    /* display: none; <- Crashes Chrome on hover */
    -webkit-appearance: none;
    margin: 0; /* <-- Apparently some margin are still there even though it's hidden */
}

</style>

</head>
'''    
    

    resultHtml +=''' <body ng-app="tools">

    <div class="container">

        <div class="row">
            <div class="tools-header">
                <h1>Outils</h1>
            </div>
        </div>

        <div class="row">
            <div ng-controller="GravityToolCtrl" class="tool-block">
                <h3>Correction du densimètre</h3>
                <form class="form-horizontal" role="form">
                <div class="form-group">
                    <label class="col-sm-3 control-label">Densité mesurée</label>
                    <div class="col-sm-2">
                        <input type="number" min="1.000" max="1.999" step="0.001" ng-model="measuredGravity" class="form-control">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">Température de calibration (°C)</label>
                    <div class="col-sm-2">
                        <input type="number" min="0" max="100" step="1" ng-model="calibTemp" class="form-control">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">Température mesurée (°C)</label>
                    <div class="col-sm-2">
                        <input type="number" min="0" max="110" step="1" ng-model="sampleTemp" class="form-control">
                    </div>
                </div>
                <div class="form-group tool-result">
                    <label class="col-sm-3 control-label">Densité corrigée</label>
                    <div class="col-sm-2">
                        <label class="control-label">{{calcGravity()}}</label>
                    </div>
                </div>
                </form>
            </div>
        </div>



        <div class="row">
            <div ng-controller="StepAssistantCtrl" class="tool-block">
                <h3>Assistant paliers</h3>
                <form class="form-horizontal" role="form">
                    <div class="form-group">
                        <label class="col-sm-3 control-label">Mode</label>
                        <div class="col-sm-3">
                            <select ng-model="stepType" ng-options="type for type in stepTypes " class="form-control"></select>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-3 control-label">Température cible (°C)</label>
                        <div class="col-sm-3">
                            <input type="number" min="1.000" max="100" step="1" ng-model="targetTemp" class="form-control">
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-3 control-label">Volume ajouté (L)</label>
                        <div class="col-sm-3">
                            <input type="number" min="0" max="10000" step="1" ng-model="addedVolume" class="form-control">
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-3 control-label">Poids du grain (Kg)</label>
                        <div class="col-sm-3">
                            <input type="number" min="0" max="10000" step="1" ng-model="grainWeight" class="form-control">
                        </div>
                    </div>
                    <div class="form-group" ng-hide="stepType=='Palier'">
                        <label class="col-sm-3 control-label">Température du grain (°C)</label>
                        <div class="col-sm-3">
                            <input type="number" min="0.1" max="100" step="1" ng-model="grainTemp" class="form-control">
                        </div>
                    </div>
                    <div class="form-group" ng-hide="stepType=='Empâtage'">
                        <label class="col-sm-3 control-label">Température de la maîche (°C)</label>
                        <div class="col-sm-3">
                            <input type="number" min="0.1" max="100" step="1" ng-model="mashTemp" class="form-control">
                        </div>
                    </div>
                    <div class="form-group" ng-hide="stepType=='Empâtage'">
                        <label class="col-sm-3 control-label">Volume d'eau dans la maîche (L)</label>
                        <div class="col-sm-3">
                            <input type="number" min="0" max="10000" step="1" ng-model="waterVolumeMash" class="form-control">
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-sm-3 control-label">Facteur de correction</label>
                        <div class="col-sm-3">
                            <input type="number" min="0" max="100" step="1" ng-model="factor" class="form-control">
                        </div>
                    </div>
                    <div class="form-group tool-result">
                    <label class="col-sm-3 control-label">Température de l'eau (°C)</label>
                    <div class="col-sm-3">
                        <label class="control-label">{{waterTemp().temp}}</label>
                    </div>
                    </div>
                    <div class="form-group">
                    <label class="col-sm-3 control-label">Ratio (L/Kg)</label>
                    <div class="col-sm-3">
                        <label class="control-label">{{waterTemp().ratio}}</label>
                    </div>
                    </div>
                </form>
            </div>
        </div>



        <div class="row">
            <div ng-controller="AlcToolCtrl" class="tool-block">
                <h3>Taux d'alcool</h3>
                <form class="form-horizontal" role="form">
                <div class="form-group">
                    <label class="col-sm-3 control-label">Densité initiale</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0.001" max="100" step="0.001" ng-model="originalGravity">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">Densité finale</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0.001" max="100" step="0.001" ng-model="finalGravity">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">Sucre ajouté (g/L)</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="100000" step="1" ng-model="addedSugar">
                    </div>
                </div>
                <div class="form-group tool-result">
                    <label class="col-sm-3 control-label">Alcool par volume (%)</label>
                    <div class="col-sm-2">
                        <label class="control-label">{{calcAlcoolVol()}}</label>
                    </div>
                </div>
                </form>
            </div>
        </div>



        <div class="row">
            <div ng-controller="DilutionToolCtrl" class="tool-block">
                <h3>Dilution</h3>
                <form class="form-horizontal" role="form">
                <div class="form-group">
                    <label class="col-sm-3 control-label">Volume initial (L)</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10000000" step="1" ng-model="initialVol">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label" >Densité spécifique initiale</label>
                    <div class="col-sm-2">
                        <input type="number"  class="form-control" min="0.001" max="100" step="0.001" ng-model="initialGravity">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">Volume ajouté (L)</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10000000" step="1" ng-model="addedVolume">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">Densité de l'ajout</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0.001" max="100" step="0.001" ng-model="addedGravity">
                    </div>
                    <p class="help-block col-sm-3">1 si ajout d'eau</p>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">Volume final (L)</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10000000" step="1" ng-change="finalVolChanged()" ng-model="finalVol">
                    </div>
                </div>
                <div class="form-group tool-result">
                    <label class="col-sm-3 control-label">Densité spécifique finale</label>
                    <div class="col-sm-2">
                        <label class="control-label">{{calcDilution()}}</label>
                    </div>
                </div>
                </form>
            </div>
        </div>
        
        
        <div class="row">
            <div ng-controller="BoiloffToolCtrl" class="tool-block">
                <h3>Evaporation</h3>
                <form class="form-horizontal" role="form">
                <div class="form-group">
                    <label class="col-sm-3 control-label">Volume pré-ébullition (L)</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10000000" step="1" ng-model="preboilVol">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label" >Densité spécifique pré-ébullition</label>
                    <div class="col-sm-2">
                        <input type="number"  class="form-control" min="0.001" max="100" step="0.001" ng-model="preboilGravity">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">Taux d'évaporation (%/heure)</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10000000" step="1" ng-model="boilOffRate">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">Durée d'ébullition (min)</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="1" max="100" step="10000" ng-model="boilTime">
                    </div>
                    
                </div>
                <div class="form-group">
                    <label class="col-sm-3 control-label">Pertes par refroidissement (%)</label>
                    <div class="col-sm-2">
                        <input type="number" class="form-control" min="0" max="10000000" step="1" ng-change="" ng-model="coolingLoss">
                    </div>
                </div>
                <div class="form-group tool-result">
                    <label class="col-sm-3 control-label">Volume évaporé (ébullition) (L)</label>
                    <div class="col-sm-2">
                        <label class="control-label">{{calcBoilOff().boilOffVol}}</label>
                    </div>
                </div>
                <div class="form-group ">
                    <label class="col-sm-3 control-label">Volume évaporé (refroidissement) (L)</label>
                    <div class="col-sm-2">
                        <label class="control-label">{{calcBoilOff().coolingLoss}}</label>
                    </div>
                </div>
                <div class="form-group ">
                    <label class="col-sm-3 control-label">Volume final (L)</label>
                    <div class="col-sm-2">
                        <label class="control-label">{{calcBoilOff().finalVol}}</label>
                    </div>
                </div>
                <div class="form-group ">
                    <label class="col-sm-3 control-label">Densité spécifique)</label>
                    <div class="col-sm-2">
                        <label class="control-label">{{calcBoilOff().finalSg}}</label>
                    </div>
                </div>
                </form>
            </div>
        </div>



    <!-- Fin container -->
    </div>
</body>
</html>'''


   

    

    return resultHtml


