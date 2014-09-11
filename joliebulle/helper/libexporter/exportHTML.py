#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.2
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
    .dropdown-menu {z-index:10000;}
    #menuSort{margin-left:50px; font-size:1em;}
    #menuSort i{padding-left:15px;font-size:1em;} 
    .selected{border-right: 3px solid #f1c40f;}
    .deleteButton{color:#fff; float:right;}
    .selected .deleteButton{color:#c3c3c3; }
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
    
    .edit-button{/*color:#f55050;*/ background-color: #3498db; color:#fff;margin-right: 20px;padding-bottom:2px;}
    .edit-button:hover {background-color: #3498db; color:#fff;}
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
          </div>
        
            
        
        
        <div class="main">


        
        
                <div class="recipe-list-header row">
                 
                <span class=""><i class="icon-search"></i></span>
                <input type="text" class="" ng-model="searchText" placeholder="Rechercher..." />
                <button  class="btn-link btn-xs sortButton" type="button" data-toggle="dropdown"><i class="icon-sort-by-alphabet"></i></button>
                <ul id="menuSort" class="dropdown-menu" role="menu">
                                <i class="journalMenu-description">Trier par :</i>
                                <li><a href="#" ng-click="sortByBrewer()" >Brasseur</a></li>
                                <li><a href="#" ng-click="sortByName()" >Nom</a></li>
                        </ul>
                
                </div>
            <div class="recipe-list">
                <div class="recipe-item" ng-class="{13}" ng-repeat="recipe in recipes | filter:searchText.toLowerCase()" ng-click="recipeSelected(recipe)">
                    <span class="brewer-name">{1}</span> <button class="btn-link btn-xs deleteButton" ng-click="deleteLib(recipe)"><i class="icon-remove"></i></button>
                    <div class="recipe-name"><a href="toto" >{2}</a>
                        <div class="recipe-style">{3}</div> 
                        
                    </div>
                </div>                        
            </div>
          <div class="recipe-view-header">

              
            
            </div>
            <div class="recipeView" ng-show="active">
                
                
                <div class="recipe-header col-md-12 row">
                    <div class="col-md-6">
                        <h1>{10}</h1>
                        <div class="author">{11} par {12}</div>
                    </div> ''' .format(str(recipesSummary),  "{{recipe.brewer}}", "{{recipe.name}}", "{{recipe.style}}", "{{currentRecipe.ibu}}","{{currentRecipe.ebc}}","{{currentRecipe.og}}","{{currentRecipe.fg}}","{{currentRecipe.fg}}","{{currentRecipe.alc}}","{{currentRecipe.name}}","{{currentRecipe.style}}","{{currentRecipe.brewer}}", str("{'selected' : activeClass == recipe.path}"))


    resultHtml +='''            
                    
                    <div class="recipe-buttons col-md-5">
                        <button id="menuJournal" class="btn-link  edit-button" type="button" data-toggle="dropdown" ><i class="icon-flag"></i> Journal <span class="icon-caret-down"></span></button>
                        <ul class="dropdown-menu" role="menu">
                                <i class="journalMenu-description">Marquer comme :</i>
                                <li><a onClick="main.addToJournal('brewed')" href="#">Brassée</a></li>
                                <li><a onClick="main.addToJournal('ferment')" href="#">Mise en fermentation</a></li>
                                <li><a onClick="main.addToJournal('bottled')" href="#">Embouteillée</a></li>
                                <li class="divider"></li>
                                <li><a onClick="main.showJournal()" href="#">Voir le journal</a></li>
                        </ul>
                        <button class="btn-link  edit-button" type="button" onClick="main.editCurrentRecipe()"><i class="icon-wrench"></i> Editer</button>
                    </div>
                </div>'''

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
                    <span class="vol-label">Vol</span> <span class="vol-value">{{currentRecipe.volume}}L</span>
                    <span class="effi-label">Rendement</span> <span class="effi-value">{{currentRecipe.efficiency}}%</span>
                    <span class="effi-label">Ebullition</span> <span class="effi-value">{{currentRecipe.boilTime}} min</span>
                </div>
                <div class="ingredients col-md-12 row">
                    <h3>Ingrédients</h3>
                    <div class="">
                        <div class="col-sm-12 col-md-12" ng-repeat="fermentable in currentRecipe.fermentables">
                            <div class="ing row">
                                <div class="col-sm-4 col-md-4"><span class="ing-name" data-toggle="popover" data-trigger="hover" data-html="true" data-placement="bottom" data-content="EBC : {{fermentable.color}} <br/> Rendement : {{fermentable.yield}}% <br/> Type : {{fermentable.type}} ">{{fermentable.name}}</span><div class="use">{{fermentable.afterBoilView}}</div></div>
                                <div class="col-md-3 ing-amount">{{fermentable.amount}} g</div>
                                
                            </div>
                        </div>
                        <div class="col-sm-12 col-md-12" ng-repeat="hop in currentRecipe.hops">
                            <div class="ing row">
                                <div class="col-sm-4 col-md-4"><span class="ing-name">{{hop.name}}</span> <div class="use">{{hop.use}} - {{hop.time}} min</div></div>
                                <div class="col-md-3 ing-amount">{{hop.amount}} g</div>
<!--
                                <div class="col-md-3 ing-amount"> {{hop.time}} min</div>
-->
                            </div>
                        </div>
                         <div class="col-sm-12 col-md-12" ng-repeat="misc in currentRecipe.miscs">
                            <div class="ing row">
                                <div class="col-sm-4 col-md-4"><span class="ing-name">{{misc.name}}</span> <div class="use">{{misc.use}} - {{misc.time}} min</div></div>
                                
                                <div class="col-md-3 ing-amount">{{misc.amount}} g</div>
<!--
                                <div class="col-md-3 ing-amount">{{misc.time}} min </div>
-->
                            </div>
                        </div>
                        <div class="col-sm-12 col-md-12" ng-repeat="yeast in currentRecipe.yeasts">
                            <div class="ing row">
                                <div class="col-md-6 ing-name">{{yeast.name}} {{yeast.labo}} {{yeast.product_id}}</div>
                            </div>
                        </div>
                    </div>
                </div>

            <div class="profile col-md-12">
                <div class="row profile-header">
                    <h3 class="col-md-6">Brassage</h3>
                    <div class="brewday-button col-md-5">    
                        <button class="btn-link edit-button" type="button" onClick="main.showBrewdayMode()" ><i class="icon-wrench"></i> Mode brassage</button>
                    </div>
                </div>    
                <div class="brew-details">
                <span class="profile-name">{{currentRecipe.mashProfile.name}}</span>
                <span class="profile-ph">pH {{currentRecipe.mashProfile.ph}}</span>
                <div ng-repeat="step in currentRecipe.mashProfile.steps">
                    <p><span class="label-step">{{step.name}}</span> palier de type {{step.type}} à {{step.temp}} °C pendant {{step.time}} minutes</p>

                </div>
                <p><span class="label-step">Rinçage</span> {{currentRecipe.mashProfile.sparge}} °C</p>
                </div>

            </div>            

            <div class="yeasts notes col-md-10">
                <h3>Notes</h3>
                    <pre>{{currentRecipe.notes}}</pre>            
            </div>  
            
            
            
            
            
            </div>
        </div>

       
    <!-- Fin container     -->
    </div>


  
</body>
</html>''' 

    return resultHtml


