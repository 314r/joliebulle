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

def exportHTML(itemsList,newItem):
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
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
<script src="controllers/journal/main.js"></script>
<script src="controllers/journal/journal.js"></script>
<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">
<link rel="stylesheet" href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<link rel="stylesheet" href="css/sidebar.css">
<style>
    .main{padding-top:0px; margin-left:75px;}
    .header{width:100%%;min-height:55px;position:fixed;left:50px;z-index: 1000;background-color: #fff;padding-left:10px;border-bottom: 1px solid #eee;}
    .journal-header {margin-left:120px;margin-top:100px;}
    .journal-header h1 {font-size:1.75em; color:#444;padding-bottom:0px;margin-top:0;padding-left:0px;}
    .journal-list{ margin-bottom:1em; padding: 50px;padding-top: 2em;}
    .row-journal{padding-left: 15px; padding-right: 15px;}
    .entry{min-height:3em;}
    .date{background-color:#a1b5bf;padding:0.2em 0.5em 0.2em 0.5em;margin-right:20px;color:white; font-size:85%%; font-weight: bold;}
    .entry button{color:white;}
    .entry:hover button{color:#428bca;}
    .event{padding-right:20px;}
    .newButton{padding-top:3em;padding-right:10px;}
    .newButton button {background-color: #3498db; color:#fff; border:none; margin-left:50px;}
    .newButton button:hover{}
    .new-form {margin-bottom:1em; padding: 50px;padding-top: 1em; padding-bottom:1em;}
    .entry .saveButton {color:#428bca;}
</style>
</head>'''


    resultHtml+='''<body ng-app="journal">


    <div class="container-fluid">

        <div class="sidebar">
<!--
            <div class="nav-header"></div>
-->
            <ul class="nav nav-sidebar">
              <li onClick="main.showLib()"><a href="#"><i class="fa fa-flask""></i> </a></li>
              <li class="active" onClick="main.showJournal()"><a href="#"><i class="fa fa-calendar-o""></i> </a></li>
              <li onClick="main.showTools()"><a href="#"><i class="fa fa-cog"></i> </a></li>
            </ul>
        </div>

        <div class="header">

        </div>

        <div class="row">
            <div class="journal-header col-md-9">
                <h1>Journal</h1>
            </div>
        </div>



        <div class="main" ng-controller="JournalCtrl" ng-init='dataJson={0};'>

              <div class="new row row-journal" ng-init="newEntry={1}">
                <div class="newButton">
                    <button ng-click="newEntry.editing = !newEntry.editing;newClicked('recette', 'événement')" ng-hide="newEntry.editing"><i class="fa fa-plus"> </i> {2}</button>
                </div>

                <form class="form-inline new-form" role="form" ng-show="newEntry.editing">
                  <div class="form-group">
                    <input class="form-control" type="date" ng-model="newEntryDate" ng-show="newEntry.editing" />
                  </div>
                  <div class="form-group">
                    <input class="form-control" type="text" ng-model="newEntryEvent" ng-show="newEntry.editing"/>
                  </div>
                  <div class="form-group">
                    <input class="form-control" id="new-entry-recipe" type="text" ng-model="newEntryRecipe" ng-show="newEntry.editing"/>
                  </div>
                  <button class="btn-link btn-xs" type="button" ng-click="saveNew(newEntryRecipe, newEntryDate, newEntryEvent); newEntry.editing = !newEntry.editing;" ng-show="newEntry.editing">{3}</button>
                </form>
              </div>''' .format(str(itemsList) , newItem, QCoreApplication.translate("Export","Ajouter une entrée"),QCoreApplication.translate("Export","enregistrer"))

    resultHtml += '''<div class="row row-journal">
                <div class="journal-list">
                  <div ng-repeat="entry in entries">
                    <div class = "entry">
                      <div ng-hide="entry.editing"><span class="date">{0}</span> {1} {2}  <span class="event"> {3}</span>
                      <button class="btn-link btn-xs" type="button" ng-click="edit(entry)" ng-hide="entry.editing">{4}</button>
                      <button class="btn-link btn-xs" type="button" ng-click="delete(entry)" ng-hide="entry.editing">{5}</button></div>
                      <form class="form-inline" role="form" ng-show="entry.editing">
                        <div class="form-group">
                          <input class="form-control" type="date" ng-model="entry.date" ng-show="entry.editing"/>
                        </div>
                        <div class="form-group">
                          <input class="form-control" type="text" ng-model="entry.event" ng-show="entry.editing"/>
                        </div>
                        <div class="form-group">
                          <input class="form-control edit-entry-recipe" type="text" ng-model="entry.recipe" ng-show="entry.editing"/>
                        </div>
                        <button class="btn-link btn-xs saveButton" ng-click="save(entry)" ng-show="entry.editing">{6}</button>
                      </form>
                    </div>
                  </div>
                </div>
            </div>
        </div>
    <!-- Fin container     -->
    </div>

</script>
</body>
</html>''' .format("{{entry.date | date:'dd/MM/yy'}}", "{{entry.recipe}}",QCoreApplication.translate("Export","a été marquée comme"), "{{entry.event}}", QCoreApplication.translate("Export","modifier"), QCoreApplication.translate("Export","supprimer"), QCoreApplication.translate("Export","enregistrer") )

    return resultHtml
