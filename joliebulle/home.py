#!/usr/bin/python3
#­*­coding: utf­8 -­*­



import codecs
import PyQt5
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


class HomePage (QtCore.QObject) :
	def generateHomePage(self) :
		self.homePage = '''
		<!DOCTYPE html>
<html lang="fr">
<!DOCTYPE html>
<html lang="fr">
<head>
<title>%s</title>
<meta charset="utf-8" />
<link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
<link rel="stylesheet" href="font-awesome/css/font-awesome.min.css">
    <style>
body {background:url(images/furley_bg.png);}
.container{width:800px;margin:auto; margin-top: 16em;background-color: white;border: 1px solid rgba(0, 0, 0, 0.1);box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.08);}
.container h1{text-align:center;}
.container h3{text-align:center;color:#999;}
    </style>
</head>
<body>
	<div class="container">
		<h1>JolieBulle</h1>
		<h3>Brasser librement</h3>
	</div class="container">
</body>
</html>
'''



