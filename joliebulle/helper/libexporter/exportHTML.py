#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.4
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

def exportHTML(ingredients):
    resultHtml = '''
<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="angular/angular.min.js"></script>
<script src="angular/angular-locale_fr-fr.js"></script>
<script src="jquery/jquery.js"></script>
<script src="bootstrap/js/bootstrap.min.js"></script>
<script src="underscore/underscore-min.js"></script>
<script src="controllers/recipes-lib/main.js"></script>
<script src="controllers/recipes-lib/recipes-lib.js"></script>
<script src="beercalc/translate.js"></script>
<script src="beercalc/beercalc.js"></script>
<script src="beercalc/jb2xml.js"></script>
<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">
<link rel="stylesheet" href="css/sidebar.css">
<link rel="stylesheet" type="text/css" href="css/library.css"/>
</head>'''


    resultHtml+='''<body ng-app="recipes-lib">

      <div class="container-fluid" ng-controller="RecipeslibCtrl" ng-init='init({0})'>
                                                                  
        
          <div class="sidebar" ng-hide="showFermentableEditor || showHopEditor || showMiscEditor || showYeastEditor">
<!--
              <div class="nav-header"></div>
-->
            <ul class="nav nav-sidebar">
              <li class="active" onClick="main.showLib()"><a href="#"><i class="fa fa-flask"></i> </a></li>
              <li onClick="main.showJournal()"><a href="#"><i class="fa fa-calendar-o"></i> </a></li>
              <li onClick="main.showTools()"><a href="#"><i class="fa fa-cog"></i> </a></li>
            </ul>
          </div>'''.format(str(ingredients))
        
            
        
        
    resultHtml+='''<div class="main" ng-hide="showFermentableEditor || showHopEditor || showMiscEditor || showYeastEditor">

                <div class="recipe-list-header row">
                 
                <span class="" ><i class="fa fa-search"></i></span>
                <input type="text" class="" ng-model="searchText" placeholder="{0}" />
                <button  class="btn-link btn-xs sortButton" type="button" data-toggle="dropdown" ><i class="fa fa-sort-alpha-asc"></i></button>
                <ul id="menuSort" class="dropdown-menu" role="menu" >
                                <i class="journalMenu-description">{1} :</i>
                                <li><a href="#" ng-click="sortByBrewer()" >{2}</a></li>
                                <li><a href="#" ng-click="sortByName()" >{3}</a></li>
                </ul>
                <button class="btn-link btn-xs newRecipeButton" type="button" onClick="main.newRecipeFromLibrary()" data-toggle="tooltip" data-placement="bottom" title="{4}"><i class="fa fa-plus"></i></button>
                </div>'''.format( QCoreApplication.translate("Export","Rechercher...", None, QCoreApplication.UnicodeUTF8),  QCoreApplication.translate("Export","Trier par", None, QCoreApplication.UnicodeUTF8),  QCoreApplication.translate("Export","Brasseur", None, QCoreApplication.UnicodeUTF8),  QCoreApplication.translate("Export","Nom", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Nouvelle recette", None, QCoreApplication.UnicodeUTF8))


    resultHtml+='''<div class="recipe-list">
                <div class="recipe-item" ng-class="{0}" ng-repeat="recipe in recipes | filter:searchText.toLowerCase()" ng-click="recipeSelected(recipe)">
                    <span class="brewer-name">{1}</span> <button class="btn-link btn-xs deleteButton" ng-click="deleteLib(recipe)"><i class="fa fa-times"></i></button>
                    <div class="recipe-name"><a href="toto" >{2}</a>
                        <div class="recipe-style">{3}</div> 
                        
                    </div>
                </div>                        
            </div>'''.format(str("{'selected' : activeClass == recipe.path}"),"{{recipe.brewer}}", "{{recipe.name}}", "{{recipe.style}}")



    resultHtml+='''<div class="recipe-view-header">
                <button class="btn-link  editRecipe" type="button" ng-click="save(currentRecipe)" ng-show="editMode">Enregistrer</button>
                <button class="btn-link  editRecipe" type="button" ng-click="cancel()" ng-show="editMode">Annuler</button>
                <button class="btn-link  editRecipe" type="button" ng-click="editRecipe()" ng-hide="editMode">Editer</button>
            </div>
            <div class="recipeView" ng-show="active">
                
                
                <div class="recipe-header col-md-12 row">
                    <div class="col-md-6" ng-hide="editMode">
                        <h1>{0}</h1>
                        <div class="author">{1} {3} {2}</div>
                    </div> ''' .format("{{currentRecipe.name}}","{{currentRecipe.style}}","{{currentRecipe.brewer}}", QCoreApplication.translate("Export","par", None, QCoreApplication.UnicodeUTF8))


    resultHtml +='''               
                    <div class="recipe-buttons col-md-5" ng-hide="editMode">
                        <button id="menuJournal" class="btn-link  edit-button" type="button" data-toggle="dropdown" ><i class="fa fa-flag"></i> {0} <span class="fa fa-caret-down"></span></button>
                        <ul class="dropdown-menu" role="menu">
                                <i class="journalMenu-description">{1} :</i>
                                <li><a onClick="main.addToJournal('brewed')" href="#">{2}</a></li>
                                <li><a onClick="main.addToJournal('ferment')" href="#">{3}</a></li>
                                <li><a onClick="main.addToJournal('bottled')" href="#">{4}</a></li>
                                <li class="divider"></li>
                                <li><a onClick="main.showJournal()" href="#">{5}</a></li>
                        </ul>
                        <button class="btn-link  edit-button" type="button" onClick="main.editCurrentRecipe()"><i class="fa fa-wrench"></i> {6}</button>
                    </div>
                </div>'''.format( QCoreApplication.translate("Export","Journal", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Marquer comme", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Brassée", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Mise en fermentation", None, QCoreApplication.UnicodeUTF8),  QCoreApplication.translate("Export","Embouteillée", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Voir le journal", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Editer", None, QCoreApplication.UnicodeUTF8))

    resultHtml +='''             
                    <div class="recipeProfile row" >
                        <div class="calculated col-xs-1 col-sm-1 col-md-2" ng-show="active" data-toggle="tooltip" data-placement="bottom" title="{0}">{1}&nbsp;IBU</div>
                        <div class="calculated col-xs-1 col-sm-1 col-md-2" ng-show="active" data-toggle="tooltip" data-placement="bottom" title="{2}">{3}&nbsp;EBC</div>
                        <div class="calculated col-xs-1 col-sm-1 col-md-2" ng-show="active" data-toggle="tooltip" data-placement="bottom" title="{4}">DI&nbsp;{5}  </div>
                        <div class="calculated col-xs-1 col-sm-1 col-md-2" ng-show="active" data-toggle="tooltip" data-placement="bottom" title="{6}">DF&nbsp;{7} </div>
                        <div class="calculated col-xs-1 col-sm-1 col-md-2" ng-show="active" data-toggle="tooltip" data-placement="bottom" title="{8}">BU/GU&nbsp;{9}</div>
                        <div class="calculated col-xs-1 col-sm-1 col-md-2" ng-show="active" data-toggle="tooltip" data-placement="bottom" title="{10}">Alc&nbsp;{11} %</div>
                    </div>'''.format(QCoreApplication.translate("Export","Amertume", None, QCoreApplication.UnicodeUTF8), "{{currentRecipe.ibu}}",QCoreApplication.translate("Teinte","Teinte", None, QCoreApplication.UnicodeUTF8), "{{currentRecipe.ebc}}", QCoreApplication.translate("Export","Densité Initiale", None, QCoreApplication.UnicodeUTF8),"{{currentRecipe.og}}",QCoreApplication.translate("Export","Densité Finale", None, QCoreApplication.UnicodeUTF8),"{{currentRecipe.fg}}", QCoreApplication.translate("Export","Rapport amertume / densité", None, QCoreApplication.UnicodeUTF8), "{{currentRecipe.bugu}}", QCoreApplication.translate("Export","Alcool", None, QCoreApplication.UnicodeUTF8), "{{currentRecipe.alc}}")

    resultHtml+= ''' 
                    <form class="baseInfos form-inline row col-md-12" role="form" ng-show="editMode">
                    <div class="form-group col-xs-1 col-sm-1 col-md-3">
                        <label for="exampleInputName2">Nom de la recette</label>
                        <input type="text" class="form-control" ng-model="currentRecipe.name">
                    </div>
                    <div class="form-group col-xs-1 col-sm-1 col-md-3">
                        <label for="exampleInputName2">Style</label>
                        <input type="text" class="form-control" ng-model="currentRecipe.style">
                    </div>
                    <div class="form-group col-xs-1 col-sm-1 col-md-3">
                        <label for="exampleInputName2">Auteur</label>
                        <input type="text" class="form-control" ng-model="currentRecipe.brewer">
                    </div>
                    <div class="form-group col-xs-1 col-sm-1 col-md-3">
                        <label for="exampleInputName2">Type</label>
                        <select class="form-control" ng-model="currentRecipe.type">
                            <option>All Grain</option>
                            <option>Extract</option>
                            <option>Partial Mash</option>
                        </select>
                    </div>
                </form>
    ''' 

    resultHtml += ''' 
                    <form class="baseConstants form-inline row col-md-12" role="form" ng-show="editMode">
                        <div class="form-group col-xs-1 col-sm-1 col-md-3">
                            <label for="exampleInputName2">Volume</label>
                            <input type="number" class="form-control" ng-model="currentRecipe.volume" ng-change="calcProfile(currentRecipe)">
                        </div>
                        <div class="form-group col-xs-1 col-sm-1 col-md-3">
                            <label for="exampleInputName2">Rendement</label>
                            <input type="number" class="form-control" ng-model="currentRecipe.efficiency" ng-change="calcProfile(currentRecipe)">
                        </div>
                        <div class="form-group col-xs-1 col-sm-1 col-md-3">
                            <label for="exampleInputName2">Durée d'ébullition</label>
                            <input type="number" class="form-control" ng-model="currentRecipe.boilTime" ng-change="calcProfile(currentRecipe)">
                        </div>
                    </form>
    '''               

    resultHtml +='''           
                <div class="recipe-vol row col-md-12" ng-hide="editMode">
                    <span class="vol-label">{0}</span> <span class="vol-value" data-toggle="tooltip" data-placement="bottom" title="{1}">{2}L</span>
                    <span class="effi-label">{3}</span> <span class="effi-value" data-toggle="tooltip" data-placement="bottom" title="{4}">{5}%</span>
                    <span class="effi-label">{6}</span> <span class="effi-value" data-toggle="tooltip" data-placement="bottom" title="{7}">{8} min</span>
                </div>
                

                '''.format(QCoreApplication.translate("Export","Vol", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Volume du brassin", None, QCoreApplication.UnicodeUTF8), "{{currentRecipe.volume}}" ,QCoreApplication.translate("Export","Rendement", None, QCoreApplication.UnicodeUTF8),QCoreApplication.translate("Export","Rendement du brassage", None, QCoreApplication.UnicodeUTF8), "{{currentRecipe.efficiency}}" ,QCoreApplication.translate("Export","Ebullition", None, QCoreApplication.UnicodeUTF8), QCoreApplication.translate("Export","Durée d'ébullition", None, QCoreApplication.UnicodeUTF8), "{{currentRecipe.boilTime}}")
    
    resultHtml +='''            
                <div class="ingredients col-md-12 row">
                    <h3>{0}</h3>
                    <div class="">
                        <div class="col-sm-12 col-md-12" ng-repeat="fermentable in currentRecipe.fermentables">
                            <div class="ing row">
                                <div class="col-sm-4 col-md-4">
                                    <span class="ing-name">
                                        <ul class="popover-ing">
                                            <li>{1} : {2}</li>
                                            <li>{3} : {4}% </li>
                                            <li>{5} : {6}</li>
                                        </ul>
                                    {7}</span>
                                    <div class="use">{8}</div>
                                </div>
                                <div class="col-md-3 ing-amount">{9} g</div>  
                                <button class="btn-link" type="button" ng-click="editFermentable($index)" ng-show="editMode">Editer</button>
                                <button class="btn-link" type="button" ng-show="editMode" ng-click="removeFermentable($index)">Supprimer</button> 
                            </div>
                        </div>
                        <button class="btn-link" type="button" ng-show="editMode" ng-click="newFermentable()">Ajouter un grain ou un sucre</button> 

                        '''.format(QCoreApplication.translate("Export","Ingrédients", None, QCoreApplication.UnicodeUTF8),QCoreApplication.translate("Export","EBC", None, QCoreApplication.UnicodeUTF8), "{{fermentable.color}}",QCoreApplication.translate("Export","Rendement", None, QCoreApplication.UnicodeUTF8),"{{fermentable.fyield}}", QCoreApplication.translate("Export","Type", None, QCoreApplication.UnicodeUTF8),"{{fermentable.type}}", "{{fermentable.name}}", "{{fermentable.afterBoilView}}", "{{fermentable.amount | number : 0}}")


    resultHtml +='''                    <div class="col-sm-12 col-md-12" ng-repeat="hop in currentRecipe.hops">
                            <div class="ing row">
                                <div class="col-sm-4 col-md-4">
                                    <span class="ing-name">
                                        <ul class="popover-ing"> 
                                            <li>{0} : {1}%</li>
                                            <li>{2} : {3}</li>
                                        </ul>

                                    {4}
                                    </span> 
                                    <div class="use">{5} - {6} min</div></div>
                                <div class="col-md-3 ing-amount">{7} g</div>
                                <button class="btn-link" type="button" ng-click="editHop($index)" ng-show="editMode">Editer</button>
                                <button class="btn-link" type="button" ng-show="editMode" ng-click="removeHop($index)">Supprimer</button> 

                            </div>
                        </div>
                        <button class="btn-link" type="button" ng-show="editMode" ng-click="newHop()">Ajouter un houblon</button> 
                        '''.format(QCoreApplication.translate("Export","Acides Alpha", None, QCoreApplication.UnicodeUTF8), "{{hop.alpha}}", QCoreApplication.translate("Export","IBU", None, QCoreApplication.UnicodeUTF8), "{{hop.ibuPart}}", "{{hop.name}}", "{{hop.use}}", "{{hop.time}}","{{hop.amount | number : 0}}")

    resultHtml +='''                     <div class="col-sm-12 col-md-12" ng-repeat="misc in currentRecipe.miscs">
                            <div class="ing row">
                                <div class="col-sm-4 col-md-4"><span class="ing-name">{0}</span> <div class="use">{1} - {2} min</div></div>
                                
                                <div class="col-md-3 ing-amount">{3} g</div>
                                <button class="btn-link" type="button" ng-click="editMisc($index)" ng-show="editMode">Editer</button>
                                <button class="btn-link" type="button" ng-show="editMode" ng-click="removeMisc($index)">Supprimer</button> 

                            </div>
                        </div>
                        <button class="btn-link" type="button" ng-show="editMode" ng-click="newMisc()">Ajouter un ingrédient divers</button> 
                        '''.format("{{misc.name}}","{{misc.use}}","{{misc.time}}","{{misc.amount | number : 0}}")

    resultHtml +='''                    <div class="col-sm-12 col-md-12" ng-repeat="yeast in currentRecipe.yeasts">
                            <div class="ing row">
                                <div class="col-md-6 ing-name">
                                    <ul class="popover-ing">
                                        <li>{0} : {1}%</li>
                                        <li>{2} : {3}</li>
                                    </ul>

                                {4} {5} {6}</div>
                                <button class="btn-link" type="button" ng-click="editYeast($index)" ng-show="editMode">Editer</button>
                                <button class="btn-link" type="button" ng-show="editMode" ng-click="removeYeast($index)">Supprimer</button> 
                            </div>
                        </div>
                    </div>
                </div>
                <button class="btn-link" type="button" ng-show="editMode" ng-click="newYeast()">Ajouter une levure</button> 
                '''.format(QCoreApplication.translate("Export","Atténuation", None, QCoreApplication.UnicodeUTF8), "{{yeast.attenuation}}", QCoreApplication.translate("Export","Forme", None, QCoreApplication.UnicodeUTF8), "{{yeast.form}}","{{yeast.name}}", "{{yeast.labo}}", "{{yeast.product_id}}")

    resultHtml +='''        <div class="profile col-md-12">
                <div class="row profile-header">
                    <h3 class="col-md-6">{0}</h3>
                    <div class="brewday-button col-md-5" ng-hide="editMode">    
                        <button class="btn-link edit-button" type="button" onClick="main.showBrewdayMode()" ><i class="fa fa-wrench"></i> {1}</button>
                    </div>
                </div>    
                <div class="brew-details">
                <select ng-model="currentRecipe.mashProfile" ng-options="profile.name for profile in mashProfiles" ng-show="editMode">
                <option value="">-- Choisir un profil de brassage --</option>
                </select>
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
                    <pre ng-hide="editMode">{1}</pre>
                    <div class="noteEditor">
                        <textarea ng-model="currentRecipe.notes" class="col-md-10" ng-show="editMode"></textarea>
                    </div>            
            </div> '''.format(QCoreApplication.translate("Export","Notes", None, QCoreApplication.UnicodeUTF8), "{{currentRecipe.notes}}") 
            
            
     
            
            
    resultHtml +='''        </div>
        </div>

        <div class="ingredientEditor" ng-show="showFermentableEditor"> 
            <button ng-click="closeFermentableEditor()">Ok</button>
            <form class="form-inline" role="form" >
                <div class="form-group">
                    <label for="exampleInputName2">Nom</label>
                    <input type="text" class="form-control" ng-model="currentFerm.name">
                </div>
                <div class="form-group">
                    <label for="exampleInputName2">Quantité</label>
                    <input type="number" class="form-control" ng-model="currentFerm.amount" ng-change="calcProfile(currentRecipe)">
                </div>
                <div class="form-group">
                    <label for="exampleInputName2">Rendement</label>
                    <input type="number" class="form-control" ng-model="currentFerm.fyield" ng-change="calcProfile(currentRecipe)">
                </div>
                <div class="form-group">
                    <label for="exampleInputName2">Couleur</label>
                    <input type="number" class="form-control" ng-model="currentFerm.color" ng-change="calcProfile(currentRecipe)">
                </div>
                <select ng-model="currentFerm.typeView" ng-change="calcProfile(currentRecipe)">
                    <option>Grain</option>
                    <option>Extrait</option>
                    <option>Extrait Sec</option>
                    <option>Sucre</option>
                </select>
                <select ng-model="currentFerm.afterBoilView" ng-change="calcProfile(currentRecipe)">
                    <option>Après Ebullition</option>
                    <option>Brassage</option>
                </select>
            </form>
             <div ng-repeat="fermentable in ingredients.fermentables" ng-click="fermentableSelected(fermentable)">
                <span>
                    {0}
                </span>

            </div>

        </div>'''.format("{{fermentable.name}}")

    resultHtml += ''' 

        <div class="ingredientEditor" ng-show="showHopEditor"> 
            <div class="sidebarIng" >
                <div ng-repeat="hop in ingredients.hops" ng-click="hopSelected(hop)">
                    <span>
                        {0}
                    </span>
                </div>
            </div>
            <div class="mainIng">
                <button ng-click="closeHopEditor()">Ok</button>
                <form class="form-inline" role="form" >
                    <div class="form-group">
                        <label for="exampleInputName2">Nom</label>
                        <input type="text" class="form-control" ng-model="currentHop.name">
                    </div>
                    <div class="form-group">
                        <label for="exampleInputName2">Durée</label>
                        <input type="number" class="form-control" ng-model="currentHop.time" ng-change="calcProfile(currentRecipe)">
                    </div>
                    <div class="form-group">
                        <label for="exampleInputName2">Alpha</label>
                        <input type="number" class="form-control" ng-model="currentHop.alpha" ng-change="calcProfile(currentRecipe)">
                    </div>
                    <div class="form-group">
                        <label for="exampleInputName2">Quantité</label>
                        <input type="number" class="form-control" ng-model="currentHop.amount" ng-change="calcProfile(currentRecipe)">
                    </div>
                    <select ng-model="currentHop.useView" ng-change="calcProfile(currentRecipe)">
                        <option>Ebullition</option>
                        <option>Dry Hop</option>
                        <option>Empâtage</option>
                        <option>Premier Moût</option>
                        <option>Aromatique</option>
                    </select>
                    <select ng-model="currentHop.formView" ng-change="calcProfile(currentRecipe)">
                        <option>Pellet</option>
                        <option>Cône</option>
                        <option>Feuille</option>
                    </select>
                </form>
            </div>
             
        </div>

    '''.format("{{hop.name}}")

    resultHtml += '''

        <div class="ingredientEditor" ng-show="showMiscEditor"> 
            <button ng-click="closeMiscEditor()">Ok</button>
            <form class="form-inline" role="form" >
                <div class="form-group">
                    <label for="exampleInputName2">Nom</label>
                    <input type="text" class="form-control" ng-model="currentMisc.name">
                </div>
                <div class="form-group">
                    <label for="exampleInputName2">Quantité</label>
                    <input type="number" class="form-control" ng-model="currentMisc.amount" ng-change="calcProfile(currentRecipe)">
                </div>
                <select ng-model="currentMisc.typeView" ng-change="calcProfile(currentRecipe)">
                    <option>Epice</option>
                    <option>Arôme</option>
                    <option>Traitement Eau</option>
                    <option>Herbe</option>
                    <option>Clarifiant</option>
                    <option>Autre</option>
                </select>
                <select ng-model="currentMisc.useView" ng-change="calcProfile(currentRecipe)">
                    <option>Ebullition</option>
                    <option>Empâtage</option>
                    <option>Primaire</option>
                    <option>Secondaire</option>
                    <option>Embouteillage</option>
                </select>
                <div class="form-group">
                    <label for="exampleInputName2">Durée</label>
                    <input type="number" class="form-control" ng-model="currentMisc.time" ng-change="calcProfile(currentRecipe)">
                </div>
                
            </form>
             <div ng-repeat="misc in ingredients.miscs" ng-click="miscSelected(misc)">
                <span>
                    {0}
                </span>
            </div>
        </div>

    '''.format("{{misc.name}}")

    resultHtml += '''
        <div class="ingredientEditor" ng-show="showYeastEditor"> 
            <button ng-click="closeYeastEditor()">Ok</button>
            <form class="form-inline" role="form" >
                <div class="form-group">
                    <label for="exampleInputName2">Nom</label>
                    <input type="text" class="form-control" ng-model="currentYeast.name">
                </div>
                <div class="form-group">
                    <label for="exampleInputName2">Labo</label>
                    <input type="text" class="form-control" ng-model="currentYeast.labo">
                </div>
                <div class="form-group">
                    <label for="exampleInputName2">ID</label>
                    <input type="text" class="form-control" ng-model="currentYeast.product_id">
                </div>
                <div class="form-group">
                    <label for="exampleInputName2">Rendement</label>
                    <input type="text" class="form-control" ng-model="currentYeast.attenuation">
                </div>
                <select ng-model="currentYeast.formView" ng-change="calcProfile(currentRecipe)">
                    <option>Liquide</option>
                    <option>Poudre</option>
                    <option>Gélose</option>
                    <option>Culture</option>
                </select>
            </form>
             <div ng-repeat="yeast in ingredients.yeasts" ng-click="yeastSelected(yeast)">
                <span>
                    {0}
                </span>
            </div>
        </div>
    '''.format("{{yeast.name}}")

    resultHtml += '''   
       
    <!-- Fin container     -->
    </div>

{0} 

  
</body>
</html>'''.format(''' 
<script type="text/javascript">
$(function () {
$("[data-toggle='tooltip']").tooltip();
});
</script>
    ''')

    return resultHtml

