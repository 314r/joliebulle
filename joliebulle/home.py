#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#JolieBulle 2.8
#Copyright (C) 2010-2013 Pierre Tavares

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



import codecs
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class HomePage (QtCore.QObject) :
	def generateHomePage(self) :
		self.homePage = '''
		<!DOCTYPE html>
<html lang="fr">
<head>
<title>HomePage</title>
<meta charset="utf-8" />
<style type="text/css">
html { font-size:100.01%; background-color:white; }
body {width:800px;margin:auto;line-height: 1.5;color: #222; font-size:80%; background-color : white;}
h1,h2,h3,h4,h5,h6 { font-weight: normal; color: #111; }
h1 { font-size: 2em; margin-bottom: 0; text-align:center; margin-top:200px;}
h2 { font-size: 1.5em; line-height: 1; margin-bottom: 2em; margin-top:2em; padding-bottom:0.75em; padding-top:0.75em;border-bottom:solid 1px #ddd;clear:both;}
h3 { font-size: 1.2em; line-height: 1.25; margin-bottom: 1.25em; text-align:center; background-color:#eeeeee; border-bottom:1px solid #cccccc; border-top:1px solid #cccccc; padding:0.5em 0 0.5em 0.5em;}


.footer { width:700px;
margin:auto; 
margin-top:4em;
margin-bottom:4em;
padding:0.5em;
background-color:#eeeeee;
border-bottom :1px solid #cccccc;
border-top :1px solid #cccccc;
text-align : center;}
</style>
</head>
<body>
<h1>JolieBulle</h1>
<h3>Brasser librement</h3>
</body>
</html>
'''



