#!/usr/bin/python
# -*- coding: utf-8 -*-
# Nom de fichier : script.py


import xml.etree.ElementTree as ET

fichierBeerXML = 'qbrew.xml'

arbre = ET.parse(fichierBeerXML)

root = arbre.getroot()


for child in root :
	print (child)


