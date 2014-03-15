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
    .main{padding-top:0px;}
    .bar {margin-top:100px;padding:0;}
    .bar .input-group-addon {color:#6f6f6f;}
    .recipe-list{ margin-bottom:1em; margin-top:40px;background-color: white;}
    

    .brewer-name{background-color:#a1b5bf;padding:0.2em 0.5em 0.2em 0.5em;color:white; margin-bottom:1em; font-size:85%%; font-weight: bold;}
    .recipe-style{background-color:#f7f7f7;padding:0.2em 0.5em 0.2em 0.5em;color:#6f6f6f; margin-bottom:1em; font-size:85%%; font-weight: bold;}
    .recipe-name a{color:#7ca3fa;}

    .recipe-info{padding-bottom:30px;}
</style>
</head>'''


    resultHtml+='''<body ng-app="recipes-lib">

      <div class="container-fluid" ng-controller="RecipeslibCtrl" ng-init='dataJson={0};'>
        
        
          <div class="col-sm-3 col-md-2 sidebar">
            <ul class="nav nav-sidebar">
              <li class="active"><a href="#"><i class="icon-beaker"></i> Recettes</a></li>
              <li><a href="#"><i class="icon-calendar-empty"></i> Journal</a></li>
              <li><a href="#"><i class="icon-cog"></i> Outils</a></li>
            </ul>
          </div>
        
            
        
        
        <div class="col-sm-9 col-sm-offset-3 col-md-10 col-md-offset-2 main">

<!-- ####################################### Le petit menu
       <div class="small-menu row">
            <div class="col-xs-3 small-menu-item"><i class="icon-cog"></i> Menu</div>
        </div> -->
          <div class="row">
            <div class="input-group input-group-sm bar col-md-2">
                <span class="input-group-addon"><i class="icon-search"></i></span>
                <input type="text" class="form-control" ng-model="searchText" placeholder="Rechercher..." />
            </div>
          </div>
        
        
          <div class="row">
            <div class="recipe-list col-md-10 col-xs-12 row">
                    <div class="recipe-item row" ng-repeat="recipe in recipes | filter:searchText.toLowerCase()">
                        <div class="recipe-name col-md-4 col-sm-3 col-xs-6"><a href="{1}">{2}</a></div>
                        <div class="col-md-4 col-sm-5 col-xs-5 recipe-info">
                            <span class="brewer-name">{3}</span> <span class="recipe-style">{4}</span>
                        </div> 
                    </div>                        
            </div>
          </div>
        
        </div>

       
    <!-- Fin container     -->
    </div>

       
</body>
</html>''' .format(str(recipesSummary), "{{recipe.path}}", "{{recipe.name}}", "{{recipe.author}}",  "{{recipe.style}}")

    return resultHtml


