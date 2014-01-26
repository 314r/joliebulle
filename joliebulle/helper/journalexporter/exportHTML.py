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




def exportHTML(itemsList,newItem):
    resultHtml = '''
<!doctype html>
<html manifest="tools.manifest">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script src="angular/angular.min.js"></script>
<script src="jquery/jquery.js"></script>
<script src="bootstrap/js/bootstrap.min.js"></script>
<script src="underscore/underscore-min.js"></script>
<script src="controllers/journal/main.js"></script>
<script src="controllers/journal/journal.js"></script>
<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">


<style>
    body {background:url(images/furley_bg.png);}
    .journal-header {padding-bottom:1em;margin: auto;float:left;}
    .journal-header h1 {color:#999;font-weight:bold; font-size:24px ;}
    .journal-list{ margin-bottom:1em; background-color: white; border: 1px solid rgba(0, 0, 0, 0.1);box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);padding: 50px;padding-top: 2em;}
    .row-journal{padding-left: 15px; padding-right: 15px;}
    .entry{min-height:3em;}
    .date{background-color:#a1b5bf;padding:0.2em 0.5em 0.2em 0.5em;margin-right:20px;color:white; font-size:85%%; font-weight: bold;}
    .entry button{color:white;}
    .entry:hover button{color:#428bca;}
    .event{padding-right:20px;}
    .newButton{padding-bottom:2em;padding-right:5px;}
    .newButton button {background:none; border:none; color:#999;margin-left:15px;padding:0;padding-right: 3px; float:right;}
    .newButton button:hover{color:#333333;}
    .new-form {margin-bottom:1em; background-color: white; border: 1px solid rgba(0, 0, 0, 0.1);box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);padding: 50px;padding-top: 1em; padding-bottom:1em;}
    .entry .saveButton {color:#428bca;}
</style>



</head>'''


    resultHtml+='''<body ng-app="journal">


    <div class="container">

        <div class="row">
            <div class="journal-header col-sm-3">
                <h1>Journal</h1>
            </div>
        </div>

       
        
        <div ng-controller="JournalCtrl" ng-init='dataJson={0};'>
            
              <div class="new row row-journal" ng-init="newEntry={1}">
                <div class="newButton">
                    <button ng-click="newEntry.editing = !newEntry.editing" ng-hide="newEntry.editing"><i class="icon-plus"> </i>Ajouter une entrée</button>
                </div>
                
                <form class="form-inline new-form" role="form" ng-show="newEntry.editing">
                  <div class="form-group">
                    <input class="form-control datepicker" type="date" ng-model="newEntryDate" ng-show="newEntry.editing" />
                  </div>
                  <div class="form-group">
                    <input class="form-control" type="text" ng-model="newEntryEvent" ng-show="newEntry.editing"/>
                  </div>
                  <div class="form-group">
                    <input class="form-control" type="text" ng-model="newEntryRecipe" ng-show="newEntry.editing"/>
                  </div>
                  <button class="btn-link btn-xs" type="button" ng-click="saveNew(newEntryRecipe, newEntryDate, newEntryEvent); newEntry.editing = !newEntry.editing" ng-show="newEntry.editing">enregistrer</button>
                </form>
              </div>

              <div class="row row-journal">
                <div class="journal-list">
                  <div ng-repeat="entry in entries">
                    <div class = "entry">
                      <div ng-hide="entry.editing"><span class="date">{2}</span> {3} a été marquée comme <span class="event"> {4}</span> 
                      <button class="btn-link btn-xs" type="button" ng-click="edit(entry)" ng-hide="entry.editing">modifier</button>
                      <button class="btn-link btn-xs" type="button" ng-click="delete(entry)" ng-hide="entry.editing">supprimer</button></div>
                      <form class="form-inline" role="form" ng-show="entry.editing">
                        <div class="form-group">
                          <input class="form-control datepicker" type="date" ng-model="entry.date" ng-show="entry.editing"/>
                        </div>
                        <div class="form-group">
                          <input class="form-control" type="text" ng-model="entry.event" ng-show="entry.editing"/>
                        </div>
                        <div class="form-group">
                          <input class="form-control" type="text" ng-model="entry.recipe" ng-show="entry.editing"/>
                        </div>
                       
                        <button class="btn-link btn-xs saveButton" ng-click="save(entry)" ng-show="entry.editing">enregistrer</button>
                        
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
</html>''' .format(str(itemsList) , newItem, "{{entry.date*1000 | date:'d/M/yy'}}", "{{entry.recipe}}", "{{entry.event}}" )

    return resultHtml


