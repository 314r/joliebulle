#!/usr/bin/python
#­*­coding: utf­8 -­*­
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
import xml.etree.ElementTree as ET
class Recette : 


	def __init__(self, parent = None):
		#self.importBeerXML()
		self.essai()
		
	def essai(self) :
	  
		self.toto=42

	#def importBeerXML(self) :
			#fichierBeerXML = self.s

			

			#arbre = ET.parse(fichierBeerXML)

			#presentation=arbre.find('.//RECIPE')
			#style=arbre.find('.//STYLE')
			#fermentables=arbre.findall('.//FERMENTABLE')
			#hops = arbre.findall('.//HOP')
			#levures = arbre.findall('.//YEAST')
			#misc = arbre.findall('.//MISC')
			#brassin = arbre.find('.//MASH')
			#paliers = arbre.findall('.//MASH_STEP')
			
			
			
			
			##Presentation de la recette
			#for nom in presentation :
				#if nom.tag == "NAME" : 
					#self.nomRecette = nom.text
			    
			#for nom in style :
				#if nom.tag == "NAME" : 
					#self.styleRecette = nom.text
					
			#for batch_size in presentation :
				#if batch_size.tag == "BATCH_SIZE" : 
					#self.volume = batch_size.text
					
			#for efficiency in presentation :
				#if efficiency.tag == "EFFICIENCY" : 
					#self.rendement= float(efficiency.text)	
			
			#for boil in presentation :
				#if boil.tag == 'BOIL_TIME' :
					#self.boil = boil.text


		
			#self.labelRecetteV.setText(self.nomRecette)
			#self.labelGenreV.setText(self.styleRecette)
			#self.doubleSpinBox_2Volume.setValue(float(self.volume))
			#self.doubleSpinBoxRendemt.setValue(self.rendement)
			#try : 
				#self.spinBoxBoil.setValue(float(self.boil))
			#except :
				#self.spinBoxBoil.setValue (0)
		
		
			##Ingredient fermentescibles
			#self.nbreFer = len(fermentables)
			#self.liste_ingr = list()
			#self.liste_fAmount = list()
			#self.liste_fType = list()
			#self.liste_fYield = list()
			#self.liste_fMashed = list()
			#self.liste_color = list()
			
			
			#i = 0
			#while i < self.nbreFer :

				#i=i+1
				#for nom in fermentables[i-1] :
					#if nom.tag == 'NAME' :
						#self.fNom = nom.text
						#self.liste_ingr.append(self.fNom)
						
					#if nom.tag =='AMOUNT' :
						#self.fAmount = 1000*(float(nom.text)) 
						#self.liste_fAmount.append(self.fAmount)
						
					#if nom.tag =='TYPE' :
						#self.fType = nom.text 
						#self.liste_fType.append(self.fType)
						
					#if nom.tag == 'YIELD' :
						#self.fYield = float(nom.text)
						#self.liste_fYield.append(self.fYield)
						
					#if nom.tag == 'RECOMMEND_MASH' :
						#self.fMashed = nom.text
						#self.liste_fMashed.append(self.fMashed)
						
					##ATTENTION ! le format BeerXML utilise des unités SRM ! 
					##srm*1.97 =ebc
					#if nom.tag == 'COLOR' :
						#self.color = float(nom.text)*1.97
						#self.liste_color.append(self.color)
						

			
			
			##Houblons
			
			#self.nbreHops = len(hops)
			#self.liste_houblons = list()
			#self.liste_hAmount = list()
			#self.liste_hForm = list()
			#self.liste_hTime = list()
			#self.liste_hAlpha = list()
			
			
			
			#h = 0
			#while h < self.nbreHops : 
				#h = h+1
				#for nom in hops [h-1] :
					#if nom.tag == 'NAME' :
						#self.hNom = nom.text
						#self.liste_houblons.append(self.hNom)
						
					#if nom.tag =='AMOUNT' :
						#self.hAmount = 1000*(float(nom.text)) 
						#self.liste_hAmount.append(self.hAmount)
						
					#if nom.tag =='FORM' :
						#self.hForm = nom.text 
						#self.liste_hForm.append(self.hForm)
						
					#if nom.tag =='TIME' :
						#self.hTime = float(nom.text)
						#self.liste_hTime.append(self.hTime)
						
					
					#if nom.tag =='ALPHA' :
						#self.hAlpha = float(nom.text)
						#self.liste_hAlpha.append(self.hAlpha)					
						
																

			
			
			##Levure 
			#self.nbreLevures = len(levures)
			#self.liste_levures = list()
			#self.liste_lForm = list()
			#self.liste_lLabo = list()
			#self.liste_lProdid = list()
			#self.liste_levuresDetail = list()
			#self.liste_levureAtten = list ()
			
			
			#l = 0
			#while l < self.nbreLevures : 
				#l = l+1
				#for nom in levures [l-1] :
					#if nom.tag == 'NAME' :
						#self.lNom = str(nom.text)
						#self.liste_levures.append(self.lNom)	
						
					#if nom.tag == 'FORM' :
						#self.lForm = str(nom.text)
						#self.liste_lForm.append(self.lForm)
						
					#if nom.tag == 'LABORATORY' :
						#self.lLabo = str(nom.text)
						#self.liste_lLabo.append(self.lLabo)
						
					#if nom.tag == 'PRODUCT_ID' :
						#self.lProd = str(nom.text)
						#self.liste_lProdid.append(self.lProd)
					
					#if nom.tag == 'ATTENUATION' :
						#self.lAtten = float(nom.text)
						#self.liste_levureAtten.append(self.lAtten)
						
						
						
				#self.liste_levuresDetail.append (self.lLabo +' ' + self.lProd +' ' + self.lNom)
						
						
						
			
			
			
			##Ingredients divers
			#self.nbreDivers = len(misc)
			#self.liste_divers = list ()
			#self.liste_dAmount = list ()
			#self.liste_dType = list ()
			
			
			#m = 0
			#while  m < self.nbreDivers :
				#m = m+1
				#for nom in misc [m-1] : 
					#if nom.tag == 'NAME' :
						#self.dNom = nom.text
						#self.liste_divers.append(self.dNom)
						
					#if nom.tag == 'AMOUNT' :
						#self.dAmount = float(nom.text)*1000
						#self.liste_dAmount.append(self.dAmount)
						
					#if nom.tag == 'TYPE' :
						#self.dType = nom.text
						#self.liste_dType.append(self.dType)

			
			
			##Brassin
			#self.bNom = ''
			#if not brassin : 
				#self.bNom = ''
			#else :
				#for nom in brassin :
					#if nom.tag == 'NAME' :
						#self.bNom = nom.text


			#self.labelBrassageV.setText(self.bNom)

						
			
			
			
			
			##Paliers

			#self.nbrePaliers = len(paliers)
			#self.liste_paliers = list()
			#self.liste_pType = list()
			#self.liste_pTime = list()
			#self.liste_pTemp = list()
			#self.liste_pQte = list()
			
			
			
			
			#p = 0
			#while p < self.nbrePaliers : 
				#p = p+1
				#for nom in paliers [p-1] :
					#if nom.tag == 'NAME' :
						#self.pNom = nom.text
						#self.liste_paliers.append(self.pNom)	
						
					#if nom.tag == 'TYPE' :
						#self.pType = nom.text
						#self.liste_pType.append(self.pType)
						
					#if nom.tag == 'STEP_TIME' :
						#self.pTime = nom.text
						#self.liste_pTime.append(self.pTime)
						
					#if nom.tag == 'STEP_TEMP' :
						#self.pTemp = float(nom.text)
						#self.liste_pTemp.append(self.pTemp)
						
			
					#if nom.tag == 'INFUSE_AMOUNT' :
						#self.pQte = float(nom.text)
						#self.liste_pQte.append(self.pQte)	
						
	#def calculs_recette (self) :
		##Calculs sur les ingredients fermentescibles
		##GU = 383.89*equivSucre/volFinal *rendement
		##si RECOMMAND_MASH = False ne pas tenir compte du rendement du brassage
		##OG = 1 + (GU/1000)
		#self.liste_equivSucre = list()
		#self.liste_equivSucreMashed = list()
		#self.liste_equivSucreNonMashed = list()
		
		#o = 0
		#while o < self.nbreFer :
			#o = o+1
			#self.equivSucre = (self.liste_fAmount[o-1]/1000)*(self.liste_fYield[o-1]/100)
			##division par 1000 et 100 pour passer des g aux kg et parce que le rendement est un pourcentage
			#self.liste_equivSucre.append(self.equivSucre)
			##for type in self.liste_fType [o-1] :
			#if self.liste_fType [o-1] == 'Extract' :
				#self.liste_equivSucreNonMashed.append(self.equivSucre)
			#else :
				#self.liste_equivSucreMashed.append(self.equivSucre)
		
		#self.GU= (383.89*sum(self.liste_equivSucreMashed)/float(self.volume))*((self.rendement)/100) + (383.89*sum(self.liste_equivSucreNonMashed)/float(self.volume))
		#self.OG = 1+ (self.GU/1000)		
			


		
		##calcul de la FG. Si il y a plusieurs levures, on recupere l'attenuation la plus elevee.
		#self.levureAttenDec = sorted (self.liste_levureAtten, reverse = True)
		#if not self.levureAttenDec : 
			#self.atten = 0.75
		#if self.levureAttenDec :
			#self.atten = self.levureAttenDec[0]/100
		
		#self.GUF = self.GU*(1-self.atten)
		#self.FG = 1 + self.GUF/1000

		
		
		##calcul de l'amertume : methode de Tinseth
		##IBUs = decimal alpha acid utilization * mg/l of added alpha acids
		
		##mg/l of added alpha acids = decimal AA rating * grams hops * 1000 / liters of wort
		##Decimal Alpha Acid Utilization = Bigness Factor * Boil Time Factor
		##Bigness factor = 1.65 * 0.000125^(wort gravity - 1)
		##Boil Time factor = 1 - e^(-0.04 * time in mins) / 4.15
		#self.liste_btFactor = list()
		#self.liste_ibuPart = list()
		
		#for time in self.liste_hTime :
			#self.btFactor = (1 - 2.71828182845904523536**(-0.04 * time)) / 4.15
			#self.liste_btFactor.append(self.btFactor)
			
		#self.bignessFactor = 1.65 * (0.000125**(self.OG - 1))
		#i = 0
		#while i < len(self.liste_btFactor) :
			#i = i+1
			#self.aaUtil = self.liste_btFactor[i-1]*self.bignessFactor
			#self.mgAA = (self.liste_hAlpha[i-1]/100)*self.liste_hAmount[i-1]*1000 / float(self.volume)
			#if self.liste_hForm[i-1] == 'Pellet' :
				#self.ibuPart = (self.mgAA * self.aaUtil) + 0.1*(self.mgAA * self.aaUtil)
			#else :
				#self.ibuPart = self.mgAA * self.aaUtil 
			#self.liste_ibuPart.append(self.ibuPart)
			

		#self.ibuTot = sum(self.liste_ibuPart)

		
		
		##calcul de la couleur
		##calcul du MCU pour chaque grain :
		##MCU=4.23*EBC(grain)*Poids grain(Kg)/Volume(L)
		##puis addition de tous les MCU
		##puis calcul EBC total :
		##EBC=2.939*MCU^0.6859
		#self.liste_mcuPart = list()
		#i = 0
		#while i < self.nbreFer :
			#i = i + 1
			#self.mcuPart  = 4.23*self.liste_color[i-1]*(self.liste_fAmount[i-1]/1000)/float(self.volume)
			#self.liste_mcuPart.append(self.mcuPart)
		#self.mcuTot = sum(self.liste_mcuPart) 
		#self.EBC = 2.939*(self.mcuTot**0.6859)

		
		##calcul ABV
		##ABV = 0.130((OG-1)-(FG-1))*1000
		
		#self.ABV = 0.130*((self.OG-1) -(self.FG-1))*1000

			
		
		
		
		#self.labelOGV.setText(str("%.3f" %(self.OG)))
		#self.labelFGV.setText(str("%.3f" %(self.FG)))
		#self.labelEBCV.setText(str("%.0f" %(self.EBC)))
		#self.labelIBUV.setText(str("%.0f" %(self.ibuTot)))
		#self.labelAlcv.setText(str("%.1f" %(self.ABV)) + '%')
						
