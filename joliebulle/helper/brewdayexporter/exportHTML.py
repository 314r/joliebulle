#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.3
#Copyright (C) 2010-2014 Pierre Tavares

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

def exportHTML(data):
    resultHtml = '''
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="angular/angular.min.js"></script>
<script src="jquery/jquery.js"></script>
<script src="bootstrap/js/bootstrap.min.js"></script>
<script src="underscore/underscore-min.js"></script>
<script src="controllers/brewday/main.js"></script>
<script src="controllers/brewday/brewday.js"></script>
<script src="beercalc/beercalc.js"></script>
<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">
<link rel="stylesheet" href="css/sidebar.css">

<style>
    .main {padding-top:45px; margin-left:80px; margin-bottom:60px;}
    .header{width:100%%;min-height:55px;position:fixed;left:50px;z-index: 1000;background-color: #fff;padding-left:10px;border-bottom: 1px solid #eee;}
    .buttonBack{margin-left:30px;margin-top:-8px;}
    .mode{margin-top:10px;padding-top:5px;margin-left:30px;display:inline-block;}
    .step {margin-top : 24px;}
    .step + .step {border-top: 1px solid #eee; padding-top : 24px;}
    .infos {margin-top:70px;}
    h2 {padding-top:30px;color:#bbb}
    .stepName {font-weight: 800;}
    .value{background-color:#a1b5bf;padding:0.2em 0.5em 0.2em 0.5em;margin-right:20px;background:#f7f7f7;color:#6f6f6f;font-weight: 800;}
    .stepDescription{color:#b2b2b2; margin-bottom:-0.5em;}
    .formStep{margin-left:-15px;}
    #option2 {margin-left:25px;}
    .form-control {min-width:75px;}
    .input-group {margin-top:1em;}
    .biab {margin-top : 1em;margin-left:-15px;}
    input::-webkit-outer-spin-button,
    input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;}
</style>
</head>'''


    resultHtml+='''<body ng-app="brewday">

    <div class="container-fluid" ng-controller="BrewdayCtrl" ng-init='init({0})'>
    ''' .format(data)

        
    resultHtml+='''
          <div class="sidebar">
            <ul class="nav nav-sidebar">
              <li class="active" onClick="main.showLib()"><a href="#"><i class="icon-beaker"></i> </a></li>
              <li onClick="main.showJournal()"><a href="#"><i class="icon-calendar-empty"></i> </a></li>
              <li onClick="main.showTools()"><a href="#"><i class="icon-cog"></i> </a></li>
            </ul>
          </div>
          <div class="header">
            <button type="button" class="btn btn-default buttonBack" onClick="main.backWebViewBiblio()">Retour recette</button>
            <div class="mode">
            <input ng-model="brewType" value="classic" ng-change="brewTypeChanged()" type="radio" name="options" id="option1"> Brassage classique
            <input ng-model="brewType" value="biab" ng-change="brewTypeChanged()" type="radio" name="options" id="option2"> Brew In A Bag
            </div>
        </div>
        <div class="col-sm-9 col-md-10 main">

            '''
            
    resultHtml+='''<h2>Paliers</h2>
            <div class="row">
                <div ng-show="invalidBiab==true" class="alert alert-warning col-md-4">Le profil de brassage doit comporter un unique palier de type infusion.</div>
            </div>'''
            
    resultHtml+='''<div ng-repeat = "step in steps" class="row step" ng-hide="invalidBiab==true">
                <div class="stepName">{{step.name}}</div>
                <p class="stepDescription">{{step.time}} minutes à {{step.temp}}°C, palier de type {{step.type}}.</p>'''
    resultHtml+='''<form class="form-inline formStep" role="form">
                    <div class="input-group addedWater col-sm-7 col-md-3" ng-hide="step.type=='Temperature' || brewType=='biab'">
                      <span class="input-group-addon">Eau ajoutée</span>
                      <input type="number" class="form-control" ng-model="step.waterVol" ng-change="volChanged($index)">
                        <span class="input-group-addon">L</span>
                    </div>'''
    resultHtml+='''<div class="input-group col-sm-7 col-md-3" ng-hide="step.type=='Temperature' || brewType=='biab'">
                      <span class="input-group-addon">Temp. eau</span>
                      <input type="number" class="form-control" ng-model="step.waterTemp" ng-change="tempChanged($index)" >
                      <span class="input-group-addon">°C</span>
                    </div>'''
    resultHtml+='''<div class="input-group col-sm-7 col-md-3" ng-hide="step.type=='Temperature' || brewType=='biab'">
                      <span class="input-group-addon">Ratio</span>
                      <input type="number" step="0.1" class="form-control" ng-model="step.ratio" ng-change="ratioChanged($index)" >
                    </div>
                </form>'''
                
    resultHtml+='''<div class="col-md-3 col-sm-7 addedWater biab" ng-hide="step.type=='Temperature' || brewType=='classic'">Eau ajoutée : <span class="value">{{step.waterVol.toFixed(1)}} L</span></div>
                <div class="col-md-3 col-sm-7 biab" ng-hide="step.type=='Temperature' || brewType=='classic'">Temp. eau : <span class="value">{{step.waterTemp.toFixed(1)}}°C</span></div>
                <div class="col-md-3 col-sm-7 biab" ng-hide="step.type=='Temperature' || brewType=='classic'">Ratio : <span class="value">{{step.ratio.toFixed(1)}}</span></div>

            </div>'''
            
        
    resultHtml+='''<div class="sparge row">
                <h2>Rinçage</h2>
                <p ng-hide="brewType=='biab'">Volume d'eau de rinçage : {{spargeVol().toFixed(1)}} L</p>
                <p ng-hide="brewType=='biab'">Température de rinçage : {{data.mashProfile.sparge}}°C</p>
                <div ng-hide="brewType=='classic'" class="alert alert-info col-md-4">Pas de rinçage en BIAB.</div>
            </div>'''
    resultHtml+='''<div class="volumes">
                <h2>Volumes</h2>
                <p>Volume de grains : {{grainVolume().toFixed(1)}} L</p>
                <p>Volume de la maische à l'empâtage : {{mashVolumeStrike().toFixed(1)}} L</p>
                <p>Volume de la maische au dernier palier : {{mashVolumeLastStep().toFixed(1)}} L</p>
            </div>'''
    resultHtml+='''<div class="preBoil">
                <h2>Pré-ébullition</h2>
                <p>Volume théorique pré-ébullition : {{preBoilVol().toFixed(1)}} L</p>
                <p>Densité théorique pré-ébullition : {{preBoilSg()}}</p>
                <button class="btn-link  check-button" type="button" ng-click="preBoilCheck()"><i class="icon-wrench"></i> Vérifier et ajuster</button>
            </div>'''
            
            
    resultHtml+='''    </div>

       
    <!-- Fin container     -->
    </div>
  
</body>
</html>''' 

    return resultHtml


