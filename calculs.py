#!/usr/bin/python
#­*­coding: utf­8 -­*­
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from main import*

class Calculs :

	def __init__(self, parent = None):
		self.calculs_recette()

	def calculs_recette (self) :
			#Calculs sur les ingredients fermentescibles
			#GU = 383.89*equivSucre/volFinal *rendement
			#si RECOMMAND_MASH = False ne pas tenir compte du rendement du brassage
			#OG = 1 + (GU/1000)
			self.liste_equivSucre = list()
			self.liste_equivSucreMashed = list()
			self.liste_equivSucreNonMashed = list()
		
			o = 0
			while o < AppWindow.nbreFer :
				o = o+1
				self.equivSucre = (self.liste_fAmount[o-1]/1000)*(self.liste_fYield[o-1]/100)
				#division par 1000 et 100 pour passer des g aux kg et parce que le rendement est un pourcentage
				self.liste_equivSucre.append(self.equivSucre)
				#for type in self.liste_fType [o-1] :
				if self.liste_fType [o-1] == 'Extract' :
					self.liste_equivSucreNonMashed.append(self.equivSucre)
				else :
					self.liste_equivSucreMashed.append(self.equivSucre)
		
			self.GU= (383.89*sum(self.liste_equivSucreMashed)/float(self.volume))*((self.rendement)/100) + (383.89*sum(self.liste_equivSucreNonMashed)/float(self.volume))
			self.OG = 1+ (self.GU/1000)		
			


		
			#calcul de la FG. Si il y a plusieurs levures, on recupere l'attenuation la plus elevee.
			self.levureAttenDec = sorted (self.liste_levureAtten, reverse = True)
			if not self.levureAttenDec : 
				self.atten = 0.75
			if self.levureAttenDec :
				self.atten = self.levureAttenDec[0]/100
		
			self.GUF = self.GU*(1-self.atten)
			self.FG = 1 + self.GUF/1000

		
		
			#calcul de l'amertume : methode de Tinseth
			#IBUs = decimal alpha acid utilization * mg/l of added alpha acids
		
			#mg/l of added alpha acids = decimal AA rating * grams hops * 1000 / liters of wort
			#Decimal Alpha Acid Utilization = Bigness Factor * Boil Time Factor
			#Bigness factor = 1.65 * 0.000125^(wort gravity - 1)
			#Boil Time factor = 1 - e^(-0.04 * time in mins) / 4.15
			self.liste_btFactor = list()
			self.liste_ibuPart = list()
		
			for time in self.liste_hTime :
				self.btFactor = (1 - 2.71828182845904523536**(-0.04 * time)) / 4.15
				self.liste_btFactor.append(self.btFactor)
			
			self.bignessFactor = 1.65 * (0.000125**(self.OG - 1))
			i = 0
			while i < len(self.liste_btFactor) :
				i = i+1
				self.aaUtil = self.liste_btFactor[i-1]*self.bignessFactor
				self.mgAA = (self.liste_hAlpha[i-1]/100)*self.liste_hAmount[i-1]*1000 / float(self.volume)
				if self.liste_hForm[i-1] == 'Pellet' :
					self.ibuPart = (self.mgAA * self.aaUtil) + 0.1*(self.mgAA * self.aaUtil)
				else :
					self.ibuPart = self.mgAA * self.aaUtil 
				self.liste_ibuPart.append(self.ibuPart)
			

			self.ibuTot = sum(self.liste_ibuPart)

		
		
			#calcul de la couleur
			#calcul du MCU pour chaque grain :
			#MCU=4.23*EBC(grain)*Poids grain(Kg)/Volume(L)
			#puis addition de tous les MCU
			#puis calcul EBC total :
			#EBC=2.939*MCU^0.6859
			self.liste_mcuPart = list()
			i = 0
			while i < AppWindow.nbreFer :
				i = i + 1
				self.mcuPart  = 4.23*self.liste_color[i-1]*(self.liste_fAmount[i-1]/1000)/float(self.volume)
				self.liste_mcuPart.append(self.mcuPart)
			self.mcuTot = sum(self.liste_mcuPart) 
			self.EBC = 2.939*(self.mcuTot**0.6859)

		
			#calcul ABV
			#ABV = 0.130((OG-1)-(FG-1))*1000
		
			self.ABV = 0.130*((self.OG-1) -(self.FG-1))*1000

			
		
		
		
			self.labelOGV.setText(str("%.3f" %(self.OG)))
			self.labelFGV.setText(str("%.3f" %(self.FG)))
			self.labelEBCV.setText(str("%.0f" %(self.EBC)))
			self.labelIBUV.setText(str("%.0f" %(self.ibuTot)))
			self.labelAlcv.setText(str("%.1f" %(self.ABV)) + '%')
						


