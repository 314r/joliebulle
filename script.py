#!/usr/bin/python
# -*- coding: utf-8 -*-
# Nom de fichier : script.py


import xml.etree.ElementTree as ET

fichierBeerXML = 'qbrew.xml'

arbre = ET.parse(fichierBeerXML)

presentation=arbre.find('.//RECIPE')
style=arbre.find('.//STYLE')
fermentables=arbre.findall('.//FERMENTABLE')


#Presentation de la recette
for nom in presentation :
	if nom.tag == "NAME" : 
    		NomRecette = nom.text
     
for nom in style :
	if nom.tag == "NAME" : 
		StyleRecette = nom.text

for genre in presentation :
	if genre.tag == "TYPE" : 
   		GenreRecette = genre.text

#Partie fermentables
nbreFer = len(fermentables)
i = 0
while i < nbreFer-1 :

	i=i+1
	for nom in fermentables[i] :
		if nom.tag == 'NAME' :
			fNom = nom.text
		if nom.tag =='COLOR' :
			fColor = nom.text

	
	
	print('{0} : {1}°' .format(fNom,fColor))




    
    

        
print (NomRecette)
print (StyleRecette)
print(GenreRecette)
print(nbreFer)


