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

def exportHTML(recipesSummary):
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
<script src="controllers/recipes-lib/main.js"></script>
<script src="controllers/recipes-lib/recipes-lib.js"></script>
<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">
<link rel="stylesheet" href="css/sidebar.css">
<style>
    .main{padding-top:0px; margin-left:75px;}
    .bar {margin-top:100px;padding:0;}
    .bar .input-group-addon {color:#6f6f6f;}
    .recipe-list{
        position :fixed;
        top: 55px;
        left: 50px;
        bottom: 0;
        width:300px;
        z-index: 1000;
        display: block;
        background-color: white;
        padding-left:30px;
        overflow-y: auto;        
    }
    .recipe-list-header{
        height:55px;
        /*position :fixed;
        display:block;
        top:0;
        z-index: 1000;
        background-color: white;*/
        background-color: #fff;
        border-bottom: 1px solid #eee;
        display:block;
        position:fixed;
        width:330px;
        padding-left :60px;
        margin-left:-25px;

    }

    .recipe-list-header i{font-size : 1.2em;}
    .recipe-list-header input{border:none; height:55px; margin:auto; background-color: #fff; border-bottom: 1px solid #eee;}
    .sortButton{color:#363636;}
    .sortButton:hover{text-decoration:none;}
    .newRecipeButton{color:#363636;margin-left:15px;}
    .newRecipeButton:hover{text-decoration:none;}
    .dropdown-menu {z-index:10000;}
    #menuSort{margin-left:100px; font-size:1em;}
    #menuSort i{padding-left:15px;font-size:1em;} 
    .selected{border-right: 3px solid #f1c40f;}
    .deleteButton{color:#fff; float:right; display:none;}
    .selected .deleteButton{color:#c3c3c3; display:inline;}
    .recipe-item{border-bottom: 1px solid #eee; padding-top:0.5em; padding-left:30px;}
    .brewer-name{padding:0.2em 0.5em 0.2em 0em;color:#c3c3c3; margin-bottom:1em; font-size:90%%;}
    .recipe-style{padding:0.2em 0.5em 0.2em 0em;color:#c3c3c3; margin-bottom:0.5em; font-size:90%%; }
    .recipe-name a{color:#6f6f6f; font-weight: bold;}
    .recipe-info{padding-bottom:30px;}
    
    .recipeView {margin:auto;margin-left:315px;background-color: #fff;}
    .recipe-view-header {width:100%%;min-height:55px;position:fixed;left:379px;z-index: 1000;background-color: #fff;padding-left:10px;border-bottom: 1px solid #eee;}
    
    
    .recipe-header{padding-top:70px;}
    .recipe-header h1 { font-size:1.75em; color:#444;padding-bottom:0px;margin-top:0;padding-left:0px;}
    .author{color:#c3c3c3;padding-left:0px;padding-bottom: 15px;}
    .recipeProfile{background-color:#f7f7f7;margin-left:30px;max-width:768px; margin-right:30px;}
    .recipe-vol {padding-left:30px;padding-top:30px;}
    .vol-label {color: #bbb;}
    .vol-value {padding:0.2em 0.5em 0.2em 0.5em;margin-right:20px;background:#f7f7f7;color:#6f6f6f;font-weight: 800;}
    .effi-label {color: #bbb;}
    .effi-value {padding:0.2em 0.5em 0.2em 0.5em;margin-right:20px;background:#f7f7f7;color:#6f6f6f;font-weight: 800;}
    
    .recipe-infos{border-bottom:solid 1px #eee;padding-bottom:0px;padding-left: 10px;}
    .profile-sidebar h5 {padding-left: 20px;margin-top:25px; padding-top:9px;padding-bottom:9px;background:#fff;color:#6f6f6f;font-weight: 800;}
    .recipe-infos-list li{list-style-type: none;color:#6f6f6f;padding-top:14px;}
    ul.recipe-infos-list{padding-left:20px; padding-top:0;}
    
    .recipe-buttons{margin-left:10px;margin-bottom:15px;padding-top: 0px;padding-left:5px;}
    i.journalMenu-description{padding-left:15px;}
    .edit-button{/*color:#f55050;*/ color: #3498db; background-color:#fff;margin-right: 20px;padding-bottom:2px;}
    .edit-button:hover {color: #3498db; background-color:#fff;}
    .tools-recipe{color:#222;float:right;font-size:18px;}
    .ibu {color:#7ca3fa;}
    .ebc {color:#7ca3fa;}
    .gravity {color:#7ca3fa;}
    .alc {color:#7ca3fa;}
    .ing{padding-bottom:1.2em;}
    .ingredients{padding-left:;}
    .ingredients h3 {padding-bottom:18px; color:#bbb ; padding-top:40px; padding-left:15px;}
    .use {color:#bbb;}
    .ing-name{font-weight:400; }
    
    .calculated{color:#999; font-weight: bold; padding-top: 1.1em;padding-bottom: 1.1em; max-width:100px; min-width:75px; }
    
    .hops {padding-left:30px;}
    .hops h3 {padding-bottom:18px; padding-top:30px;color:#bbb}
    .profile h3 {padding-bottom:10px;padding-top:0px;margin-top:0;color:#bbb}
    .profile-header {padding-top:30px; padding-bottom:10px;}
    .brewday-button {padding-top:0px;}
    .brew-details {padding-left:15px;}
    #donutchart{padding:0;margin:0;margin-top:-3.5em;}
    #hopbar{margin-left:-20px;}
    .profile p{margin-bottom: 1.5em;}
    .profile-name{font-weight: bold;display:block;}
    .label-step{background-color:#f7f7f7;padding:0.2em 0.5em 0.2em 0.5em;color:#6f6f6f;font-weight: bold;}
    .label-sparge{background-color:#a1b5bf;padding:0.2em 0.5em 0.2em 0.5em;color:#6f6f6f;font-weight: bold;}
    .profile-ph{display:inline-block;margin-top:1em;margin-bottom:1.5em;padding:0.2em 0.5em 0.2em 0.5em;background:#f7f7f7;color:#6f6f6f;font-weight: 800;}
    #profile-graph{margin-top:2em;}

    .notes{margin-bottom:90px;padding-left:30px;}
    .notes pre {min-height:100px;}
    .recipe-list::-webkit-scrollbar { 
    display: none; 
}
</style>
</head>'''


    resultHtml+='''<body ng-app="recipes-lib">

      <div class="container-fluid" ng-controller="RecipeslibCtrl" ng-init='init({0})'>
                                                                  
        
          <div class="sidebar">
<!--
              <div class="nav-header"></div>
-->
            <ul class="nav nav-sidebar">
              <li class="active" onClick="main.showLib()"><a href="#"><i class="icon-beaker"></i> </a></li>
              <li onClick="main.showJournal()"><a href="#"><i class="icon-calendar-empty"></i> </a></li>
              <li onClick="main.showTools()"><a href="#"><i class="icon-cog"></i> </a></li>
            </ul>
          </div>'''.format(str(recipesSummary))
        
            
        
        
    resultHtml+='''<div class="main">

                <div class="recipe-list-header row">
                 
                <span class=""><i class="icon-search"></i></span>
                <input type="text" class="" ng-model="searchText" placeholder="{0}" />
                <button  class="btn-link btn-xs sortButton" type="button" data-toggle="dropdown"><i class="icon-sort-by-alphabet"></i></button>
                <ul id="menuSort" class="dropdown-menu" role="menu">
                                <i class="journalMenu-description">{1} :</i>
                                <li><a href="#" ng-click="sortByBrewer()" >{2}</a></li>
                                <li><a href="#" ng-click="sortByName()" >{3}</a></li>
                </ul>
                <button class="btn-link btn-xs newRecipeButton" type="button" onClick="main.newRecipeFromLibrary()"><i class="icon-plus"></i></button>
                </div>'''.format( QCoreApplication.translate("Export","Rechercher...", None, QCoreApplication.UnicodeUTF8),  QCoreApplication.translate("Export","Trier par", None, QCoreApplication.UnicodeUTF8),  QCoreApplication.translate("Export","Brasseur", None, QCoreApplication.UnicodeUTF8),  QCoreApplication.translate("Export","Nom", None, QCoreApplication.UnicodeUTF8))


    resultHtml+='''<div class="recipe-list">
                <div class="recipe-item" ng-class="{0}" ng-repeat="recipe in recipes | filter:searchText.toLowerCase()" ng-click="recipeSelected(recipe)">
                    <span class="brewer-name">{1}</span> <button class="btn-link btn-xs deleteButton" ng-click="deleteLib(recipe)"><i class="icon-remove"></i></button>
                    <div class="recipe-name"><a href="toto" >{2}</a>
                        <div class="recipe-style">{3}</div> 
                        
                    </div>
                </div>                        
            </div>'''.format(str("{'selected' : activeClass == recipe.path}"),"{{recipe.brewer}}", "{{recipe.name}}", "{{recipe.style}}")



    resultHtml+='''<div class="recipe-view-header">

              
            
            </div>
            <div class="recipeView" ng-show="active">
                
                
                <div class="recipe-header col-md-12 row">
                    <div class="col-md-6">
                        <h1>{0}</h1>
                        <div class="author">{1} {3} {2}</div>
                    </div> ''' .format("{{currentRecipe.name}}","{{currentRecipe.style}}","{{currentRecipe.brewer}}", QCoreApplication.translate("Export","par", None, QCoreApplication.UnicodeUTF8))


    resultHtml +='''               
                    <div class="recipe-buttons col-md-5">
                        <button id="menuJournal" class="btn-link  edit-button" type="button" data-toggle="dropdown" ><i class="icon-flag"></i> {0} <span class="icon-caret-down"></span></button>
                        <ul class="dropdown-menu" role="menu">
                                <i class="journalMenu-description">{1} :</i>
                                <li><a onClick="main.addToJournal('brewed')" href="#">{2}</a></li>
                                <li><a onClick="main.addToJournal('ferment')" href="#">{3}</a></li>
                                <li><a onClick="main.addToJournal('bottled')" href="#">{4}</a></li>
                                <li class="divider"></li>
                                <li><a onClick="main.showJournal()" href="#">{5}</a></li>
                        </ul>
                        <button class="btn-link  edit-button" type="button" onClick="main.editCurrentRecipe()"><i class="icon-wrench"></i> {6}</button>
                    </div>
                </div>'''.format( QCoreApplication.translate("Export","Journal", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Marquer comme", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Brassée", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Mise en fermentation", None, QCoreApplication.UnicodeUTF8),  QCoreApplication.translate("Export","Embouteillée", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Voir le journal", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Editer", None, QCoreApplication.UnicodeUTF8))

    resultHtml +='''             
                    <div class="recipeProfile row">
                        <div class="calculated col-xs-1 col-sm-1 col-md-2" ng-show="active">{0}&nbsp;IBU</div>
                        <div class="calculated col-xs-1 col-sm-1 col-md-2" ng-show="active">{1}&nbsp;EBC</div>
                        <div class="calculated col-xs-1 col-sm-1 col-md-2" ng-show="active">DI&nbsp;{2}  </div>
                        <div class="calculated col-xs-1 col-sm-1 col-md-2" ng-show="active">DF&nbsp;{3} </div>
                        <div class="calculated col-xs-1 col-sm-1 col-md-2" ng-show="active">BU/GU&nbsp;{4}</div>
                        <div class="calculated col-xs-1 col-sm-1 col-md-2" ng-show="active">Alc&nbsp;{5}</div>
                    </div>'''.format("{{currentRecipe.ibu}}", "{{currentRecipe.ebc}}","{{currentRecipe.og}}","{{currentRecipe.fg}}","{{currentRecipe.bugu}}","{{currentRecipe.alc}}")

    resultHtml +='''           
                <div class="recipe-vol row col-md-12">
                    <span class="vol-label">{0}</span> <span class="vol-value">{1}L</span>
                    <span class="effi-label">{2}</span> <span class="effi-value">{3}%</span>
                    <span class="effi-label">{4}</span> <span class="effi-value">{5} min</span>
                </div>'''.format(QCoreApplication.translate("Export","Vol", None, QCoreApplication.UnicodeUTF8), "{{currentRecipe.volume}}" ,QCoreApplication.translate("Export","Rendement", None, QCoreApplication.UnicodeUTF8), "{{currentRecipe.efficiency}}" ,QCoreApplication.translate("Export","Ebullition", None, QCoreApplication.UnicodeUTF8), "{{currentRecipe.boilTime}}")
    
    resultHtml +='''            
                <div class="ingredients col-md-12 row">
                    <h3>{0}</h3>
                    <div class="">
                        <div class="col-sm-12 col-md-12" ng-repeat="fermentable in currentRecipe.fermentables">
                            <div class="ing row">
                                <div class="col-sm-4 col-md-4"><span class="ing-name" data-toggle="popover" data-trigger="hover" data-html="true" data-placement="bottom" data-content="EBC : {1} <br/> Rendement : {2}% <br/> Type : {3} ">{4}</span><div class="use">{5}</div></div>
                                <div class="col-md-3 ing-amount">{6} g</div>
                                
                            </div>
                        </div>'''.format(QCoreApplication.translate("Export","Ingrédients", None, QCoreApplication.UnicodeUTF8), "{{fermentable.color}}","{{fermentable.yield}}", "{{fermentable.type}}", "{{fermentable.name}}", "{{fermentable.afterBoilView}}", "{{fermentable.amount}}")


    resultHtml +='''                    <div class="col-sm-12 col-md-12" ng-repeat="hop in currentRecipe.hops">
                            <div class="ing row">
                                <div class="col-sm-4 col-md-4"><span class="ing-name">{0}</span> <div class="use">{1} - {2} min</div></div>
                                <div class="col-md-3 ing-amount">{3} g</div>

                            </div>
                        </div>'''.format("{{hop.name}}", "{{hop.use}}", "{{hop.time}}","{{hop.amount}}")

    resultHtml +='''                     <div class="col-sm-12 col-md-12" ng-repeat="misc in currentRecipe.miscs">
                            <div class="ing row">
                                <div class="col-sm-4 col-md-4"><span class="ing-name">{0}</span> <div class="use">{1} - {2} min</div></div>
                                
                                <div class="col-md-3 ing-amount">{3} g</div>

                            </div>
                        </div>'''.format("{{misc.name}}","{{misc.use}}","{{misc.time}}","{{misc.amount}}")

    resultHtml +='''                    <div class="col-sm-12 col-md-12" ng-repeat="yeast in currentRecipe.yeasts">
                            <div class="ing row">
                                <div class="col-md-6 ing-name">{0} {1} {2}</div>
                            </div>
                        </div>
                    </div>
                </div>'''.format("{{yeast.name}}", "{{yeast.labo}}", "{{yeast.product_id}}")

    resultHtml +='''        <div class="profile col-md-12">
                <div class="row profile-header">
                    <h3 class="col-md-6">{0}</h3>
                    <div class="brewday-button col-md-5">    
                        <button class="btn-link edit-button" type="button" onClick="main.showBrewdayMode()" ><i class="icon-wrench"></i> {1}</button>
                    </div>
                </div>    
                <div class="brew-details">
                <span class="profile-name">{2}</span>
                <span class="profile-ph">pH {3}</span>
                <div ng-repeat="step in currentRecipe.mashProfile.steps">
                    <p><span class="label-step">{4}</span> {5} {6} {7} {8} °C {9} {10} {11}</p>

                </div>
                <p><span class="label-step">{12}</span> {13} °C</p>
                </div>

            </div>'''.format(QCoreApplication.translate("Export","Brassage", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Mode brassage", None, QCoreApplication.UnicodeUTF8),"{{currentRecipe.mashProfile.name}}","{{currentRecipe.mashProfile.ph}}", "{{step.name}}",QCoreApplication.translate("Export","palier de type", None, QCoreApplication.UnicodeUTF8), "{{step.type}}", QCoreApplication.translate("Export","à", None, QCoreApplication.UnicodeUTF8),"{{step.temp}}", QCoreApplication.translate("Export","pendant", None, QCoreApplication.UnicodeUTF8),"{{step.time}}", QCoreApplication.translate("Export","minutes", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Rinçage", None, QCoreApplication.UnicodeUTF8), "{{currentRecipe.mashProfile.sparge}}")            

    resultHtml +='''        <div class="yeasts notes col-md-10">
                <h3>{0}</h3>
                    <pre>{1}</pre>            
            </div> '''.format(QCoreApplication.translate("Export","Notes", None, QCoreApplication.UnicodeUTF8), "{{currentRecipe.notes}}") 
            
            
            
            
            
    resultHtml +='''        </div>
        </div>

       
    <!-- Fin container     -->
    </div>


  
</body>
</html>''' 

    return resultHtml


