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
    .printButton{color:#909090; font-size:150%; margin-right : 30px;}
    .printButton:hover{text-decoration:none; color:#909090;}
    .check-button {padding-left:0;}
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
            <button type="button" class="btn btn-default buttonBack" onClick="main.backWebViewBiblio()">{0}</button>
            <button class="btn-link btn-xs printButton" type="button" ng-click="printBrewday()"><i class="icon-print"></i></button>
            <div class="mode">
            <input ng-model="brewType" value="classic" ng-change="brewTypeChanged()" type="radio" name="options" id="option1"> {1}
            <input ng-model="brewType" value="biab" ng-change="brewTypeChanged()" type="radio" name="options" id="option2"> {2}
            </div>
        </div>
        <div class="col-sm-9 col-md-10 main">

            '''.format(QCoreApplication.translate("Export","Retour recette", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Brassage classique", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Brew In A Bag", None, QCoreApplication.UnicodeUTF8))
            
    resultHtml+='''<h2>{0}</h2>
            <div class="row">
                <div ng-show="invalidBiab==true" class="alert alert-warning col-md-4">{1}</div>
            </div>'''.format(QCoreApplication.translate("Export","Paliers", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Le profil de brassage doit comporter un unique palier de type infusion.", None, QCoreApplication.UnicodeUTF8))
            
    resultHtml+='''<div ng-repeat = "step in steps" class="row step" ng-hide="invalidBiab==true">
                <div class="stepName">{0}</div>
                <p class="stepDescription">{1} {2} {3}°C, {4} {5}.</p>'''.format("{{step.name}}", "{{step.time}}", QCoreApplication.translate("Export","minutes à", None, QCoreApplication.UnicodeUTF8), "{{step.temp}}", QCoreApplication.translate("Export","palier de type", None, QCoreApplication.UnicodeUTF8), "{{step.type}}")

    resultHtml+='''<form class="form-inline formStep" role="form">
                    <div class="input-group addedWater col-sm-7 col-md-3" ng-hide="step.type=='Temperature' || brewType=='biab'">
                      <span class="input-group-addon">{0}</span>
                      <input type="number" class="form-control" ng-model="step.waterVol" ng-change="volChanged($index)">
                        <span class="input-group-addon">L</span>
                    </div>'''.format(QCoreApplication.translate("Export","Eau ajoutée", None, QCoreApplication.UnicodeUTF8),)

    resultHtml+='''<div class="input-group col-sm-7 col-md-3" ng-hide="step.type=='Temperature' || brewType=='biab'">
                      <span class="input-group-addon">{0}</span>
                      <input type="number" class="form-control" ng-model="step.waterTemp" ng-change="tempChanged($index)" >
                      <span class="input-group-addon">°C</span>
                    </div>'''.format(QCoreApplication.translate("Export","Temp. eau", None, QCoreApplication.UnicodeUTF8),)

    resultHtml+='''<div class="input-group col-sm-7 col-md-3" ng-hide="step.type=='Temperature' || brewType=='biab'">
                      <span class="input-group-addon">{0}</span>
                      <input type="number" step="0.1" class="form-control" ng-model="step.ratio" ng-change="ratioChanged($index)" >
                    </div>
                </form>'''.format(QCoreApplication.translate("Export","Ratio", None, QCoreApplication.UnicodeUTF8),)
                
    resultHtml+='''<div class="col-md-3 col-sm-7 addedWater biab" ng-hide="step.type=='Temperature' || brewType=='classic'">Eau ajoutée : <span class="value">{0} L</span></div>
                <div class="col-md-3 col-sm-7 biab" ng-hide="step.type=='Temperature' || brewType=='classic'">Temp. eau : <span class="value">{1}°C</span></div>
                <div class="col-md-3 col-sm-7 biab" ng-hide="step.type=='Temperature' || brewType=='classic'">Ratio : <span class="value">{2}</span></div>
            </div>'''.format("{{step.waterVol.toFixed(1)}}", "{{step.waterTemp.toFixed(1)}}","{{step.ratio.toFixed(1)}}" )
        
    resultHtml+='''<div class="sparge row">
                <h2>{0}</h2>
                <p ng-hide="brewType=='biab'">{1} : {2} L</p>
                <p ng-hide="brewType=='biab'">{3} : {4}°C</p>
                <div ng-hide="brewType=='classic'" class="alert alert-info col-md-4">{5}</div>
            </div>'''.format(QCoreApplication.translate("Export","Rinçage", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Volume d'eau de rinçage", None, QCoreApplication.UnicodeUTF8), "{{spargeVol().toFixed(1)}}", QCoreApplication.translate("Export","Température de rinçage", None, QCoreApplication.UnicodeUTF8),"{{data.mashProfile.sparge}}", QCoreApplication.translate("Export","Pas de rinçage en BIAB.", None, QCoreApplication.UnicodeUTF8))

    resultHtml+='''<div class="volumes">
                <h2>{0}</h2>
                <p>{1} : {2} L</p>
                <p>{3} : {4} L</p>
                <p>{5} : {6} L</p>
            </div>'''.format(QCoreApplication.translate("Export","Volumes", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Volume de grains", None, QCoreApplication.UnicodeUTF8), "{{grainVolume().toFixed(1)}}", QCoreApplication.translate("Export","Volume de la maische à l'empâtage", None, QCoreApplication.UnicodeUTF8), "{{mashVolumeStrike().toFixed(1)}}", QCoreApplication.translate("Export","Volume de la maische au dernier palier", None, QCoreApplication.UnicodeUTF8), "{{mashVolumeLastStep().toFixed(1)}}")

    resultHtml+='''<div class="preBoil">
                <h2>{0}</h2>
                <p>{1} : {2} L</p>
                <p>{3} : {4}</p>
                <button class="btn-link check-button" type="button" ng-click="preBoilCheck()"><i class="icon-wrench"></i> {5}</button>
            </div>'''.format(QCoreApplication.translate("Export","Pré-ébullition", None, QCoreApplication.UnicodeUTF8),QCoreApplication.translate("Export","Volume théorique pré-ébullition", None, QCoreApplication.UnicodeUTF8),"{{preBoilVol().toFixed(1)}}", QCoreApplication.translate("Export","Densité théorique pré-ébullition", None, QCoreApplication.UnicodeUTF8), "{{preBoilSg()}}", QCoreApplication.translate("Export","Vérifier et ajuster", None, QCoreApplication.UnicodeUTF8))
            
            
    resultHtml+='''</div>

       
    <!-- Fin container     -->
    </div>
  
</body>
</html>''' 

    return resultHtml


