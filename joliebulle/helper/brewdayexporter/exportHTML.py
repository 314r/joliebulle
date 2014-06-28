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
<link rel="stylesheet" href="http://cdn.oesmith.co.uk/morris-0.4.3.min.css">
<script src="http://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
<script src="http://cdn.oesmith.co.uk/morris-0.4.3.min.js"></script>
<style>
    .main {padding-top:90px; padding-left:60px;}
    .step {margin-top : 24px;  }
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
</style>
</head>'''


    resultHtml+='''<body>

Hello world ! You are in the new shiny brewday mode.
  
</body>
</html>''' 

    return resultHtml


