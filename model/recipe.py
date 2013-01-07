#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­



#JolieBulle 2.6
#Copyright (C) 2010-2012 Pierre Tavares

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
import logging
import model.constants
from model.fermentable import *
from model.hop import *
from model.yeast import *
from model.misc import *
from model.mashstep import *

logger = logging.getLogger(__name__)

class Recipe:
    """A class for storing recipes attributes"""
    def __init__(self):
        self.name = ""
        self.brewer = ""
        self.type = model.constants.RECIPE_TYPE_ALL_GRAIN
        self.volume = 0.0
        self.efficiency = 0.0
        self.boil = 0.0
        self.recipeNotes = ""
        self.style = ""
        self.mashName = ""
        self.mashGrainTemp = ""
        self.mashTunTemp = ""
        self.spargeTemp = ""
        self.mashPh = ""
        self.listeFermentables = list()
        self.listeHops = list()
        self.listeYeasts = list()
        self.listeMiscs = list()
        self.listeMashSteps = list()

    def __repr__(self):
        return ('recipe[name="%s", brewer="%s", type=%s, volume=%s, efficiency=%s, boil=%s, recipeNotes="%s", style="%s"]' %
                (self.name, self.brewer, self.type, self.volume, self.efficiency, self.boil, self.recipeNotes, self.style) )
    
    @staticmethod
    def parse(tree):
        logger.debug("Start parsing recipe")
        recipe = Recipe()
        
        presentation=tree.find('.//RECIPE')
        fermentables=tree.findall('.//FERMENTABLE')
        hops = tree.findall('.//HOP')
        levures = tree.findall('.//YEAST')
        misc = tree.findall('.//MISC')
        style=tree.find('.//STYLE')
        mash = tree.find('.//MASH')
        mashStep = mash.findall('.//MASH_STEP')

        for element in presentation :
            if 'NAME' == element.tag : 
                recipe.name = element.text
                logger.debug(" Recipe name: %s", recipe.name)
            if 'BREWER' == element.tag :
                recipe.brewer = element.text
                logger.debug(" Recipe brewer: %s", recipe.brewer)
            if 'TYPE' == element.tag:
                if "All Grain" == element.text :
                    recipe.type = model.constants.RECIPE_TYPE_ALL_GRAIN
                elif "Partial Mash" == element.text :
                    recipe.type = model.constants.RECIPE_TYPE_PARTIAL_MASH
                elif "Extract" == element.text :
                    recipe.type = model.constants.RECIPE_TYPE_EXTRACT
                logger.debug(" Recipe type: %s", recipe.type)
            if "BATCH_SIZE" == element.tag :
                recipe.volume = float(element.text)
                logger.debug(" Recipe volume: %s", recipe.volume)
            if "EFFICIENCY" == element.tag :
                recipe.efficiency= float(element.text)
                logger.debug(" Recipe efficiency: %s", recipe.efficiency)
            if "BOIL_TIME" == element.tag :
                recipe.boil = float(element.text)
                logger.debug(" Recipe boil time: %s", recipe.boil)
            if "NOTES" == element.tag :
                recipe.recipeNotes = element.text
                logger.debug(" Recipe notes: %s", recipe.recipeNotes)
        
        for element in style :
            if "NAME" == element.tag :
                recipe.style = element.text

        for element in mash:
            if 'NAME' == element.tag :
                recipe.mashName = element.text
            if 'GRAIN_TEMP' == element.tag :
                recipe.mashGrainTemp = element.text
            if 'TUN_TEMP' == element.tag  :
                recipe.mashTunTemp = element.text
            if 'SPARGE_TEMP' == element.tag  :
                recipe.spargeTemp = element.text
            if 'PH' == element.tag :
                recipe.mashPh = element.text

        for element in fermentables:
            recipe.listeFermentables.append( Fermentable.parse(element) )
        for element in hops:
            recipe.listeHops.append(Hop.parse(element))
        for element in levures:
            recipe.listeYeasts.append(Yeast.parse(element))
        for element in misc:
            recipe.listeMiscs.append(Misc.parse(element))
        for element in mashStep:
            recipe.listeMashSteps.append(MashStep.parse(element))

        #logger.debug(repr(recipe))
        logger.debug("End parsing recipe")
        return recipe

    def compute_fermentablesWeight(self):
        grainWeight = 0
        for f in self.listeFermentables:
            grainWeight += f.amount
        return grainWeight

    def compute_equivSugar(self):
        self.equivSugar = 0.0
        self.equivSugarMashed = 0.0
        self.equivSugarNonMashed = 0.0
        self.equivSugarPreBoil = 0.0
        self.equivSugarMashedPreBoil = 0.0
        self.equivSugarNonMashedPreBoil = 0.0

        for f in self.listeFermentables:
            self.equivSugar += f.equivSucre()
            if f.type == model.constants.FERMENTABLE_TYPE_EXTRACT or f.type == model.constants.FERMENTABLE_TYPE_DRY_EXTRACT or f.type == model.constants.FERMENTABLE_TYPE_SUGAR :
                self.equivSugarNonMashed += f.equivSucre()
            else :
                self.equivSugarMashed += f.equivSucre()

            #on refait la même chose pour déterminer la densité pré-ébullition en cas d'addition tardive de sucre, ce qui influence le calcul des IBUs.
            if f.useAfterBoil == False:
                self.equivSugarPreBoil += f.equivSucre()
                if f.type == model.constants.FERMENTABLE_TYPE_EXTRACT or f.type == model.constants.FERMENTABLE_TYPE_DRY_EXTRACT or f.type == model.constants.FERMENTABLE_TYPE_SUGAR :
                    self.equivSugarNonMashedPreBoil += f.equivSucre()
                else :
                    self.equivSugarMashedPreBoil += f.equivSucre()

    def compute_OG(self):
        return 1+ (self.compute_GU()/1000)
    
    def compute_OG_PreBoil(self):
        return 1+ (self.compute_GU_PreBoil()/1000)

    def compute_GU(self):    
        self.compute_equivSugar()
        return (383.89*self.equivSugarMashed/float(self.volume))*(self.efficiency/100) + (383.89*self.equivSugarNonMashed/float(self.volume))

    def compute_GU_PreBoil(self):
        self.compute_equivSugar()
        return (383.89*self.equivSugarMashedPreBoil/float(self.volume))*(self.efficiency/100) + (383.89*self.equivSugarNonMashedPreBoil/float(self.volume))

    def compute_FG(self):
        #calcul de la FG. Si il y a plusieurs levures, on recupere l'attenuation la plus elevee.
        levureAttenDec = sorted (self.listeYeasts, reverse = True, key=lambda levure: levure.attenuation)
        if not levureAttenDec : 
            atten = 0.75
        else :
            atten = levureAttenDec[0].attenuation/100
        
        GUF = self.compute_GU()*(1-atten)
        return 1 + GUF/1000

    def compute_EBC(self):
        #calcul de la couleur
        #calcul du MCU pour chaque grain :
        #MCU=4.23*EBC(grain)*Poids grain(Kg)/Volume(L)
        #puis addition de tous les MCU
        #puis calcul EBC total :
        #EBC=2.939*MCU^0.6859
        mcuTot = 0
        for f in self.listeFermentables:
            mcuTot += 4.23*f.color*(f.amount/1000)/float(self.volume)
        return 2.939*(mcuTot**0.6859)

    def compute_IBUPart(self):
        #calcul de l'amertume : methode de Tinseth
        #IBUs = decimal alpha acid utilization * mg/l of added alpha acids
        
        #mg/l of added alpha acids = decimal AA rating * grams hops * 1000 / liters of wort
        #Decimal Alpha Acid Utilization = Bigness Factor * Boil Time Factor
        #Bigness factor = 1.65 * 0.000125^(wort gravity - 1)
        #Boil Time factor = 1 - e^(-0.04 * time in mins) / 4.15
        bignessFactor = 1.65 * (0.000125**(self.compute_OG_PreBoil() - 1))
        hash_ibu = dict()
        for h in self.listeHops:
            btFactor = (1 - 2.71828182845904523536**(-0.04 * h.time)) / 4.15

            aaUtil = btFactor*bignessFactor
            mgAA = (h.alpha/100)*h.amount*1000 / float(self.volume)
            try :
                if h.use != model.constants.HOP_USE_DRY_HOP and h.use != model.constants.HOP_USE_AROMA :
                    if h.form == model.constants.HOP_FORM_PELLET :
                        ibu = (mgAA * aaUtil) + 0.1*(mgAA * aaUtil)
                    else :
                        ibu = mgAA * aaUtil 
            except:
                if h.form == model.constants.HOP_FORM_PELLET :
                    ibu = (mgAA * aaUtil) + 0.1*(mgAA * aaUtil)
                else :
                    ibu = mgAA * aaUtil
            hash_ibu[h] = ibu
        return hash_ibu

    def compute_IBU(self):
        ibuParts = self.compute_IBUPart()
        return sum(ibuParts.values())

    def compute_ratioBUGU(self):
        #calcul du rapport BU/GU
        try :
            ratioBuGu = self.compute_IBU() / self.compute_GU()
        except :
            ratioBuGu = 0
        return ratioBuGu

    def compute_ABV(self):
        #calcul ABV
        #ABV = 0.130((OG-1)-(FG-1))*1000
        return 0.130*((self.compute_OG()-1) -(self.compute_FG()-1))*1000

    def compute_proportions(self):
        #calcul des proportions pour les grains
        hash_proportion = dict()
        poidsTot = sum([f.amount for f in self.listeFermentables])
        i = 0
        for f in self.listeFermentables:
            i=i+1
            propGrain = (f.amount / poidsTot)*100
            hash_proportion[f] = propGrain
        return hash_proportion

    def calculs_recette (self) :
        
        #Calculs sur les ingredients fermentescibles
        #GU = 383.89*equivSucre/volFinal *rendement
        #si extrait ou sucre ne pas tenir compte du rendement du brassage
        #OG = 1 + (GU/1000)
        
        liste_equivSucre = list()
        liste_equivSucreMashed = list()
        liste_equivSucreNonMashed = list()

        liste_equivSucrePreBoil = list()
        liste_equivSucreMashedPreBoil = list()
        liste_equivSucreNonMashedPreBoil = list()
        
        grainWeight = 0
        for f in self.listeFermentables:
            grainWeight += f.amount
            #division par 1000 et 100 pour passer des g aux kg et parce que le rendement est un pourcentage
            liste_equivSucre.append(f.equivSucre() )
            #for type in self.liste_fType [o-1] :
            if f.type == model.constants.FERMENTABLE_TYPE_EXTRACT or f.type == model.constants.FERMENTABLE_TYPE_DRY_EXTRACT or f.type == model.constants.FERMENTABLE_TYPE_SUGAR :
                liste_equivSucreNonMashed.append(f.equivSucre())
            else :
                liste_equivSucreMashed.append(f.equivSucre())

            #on refait la même chose pour déterminer la densité pré-ébullition en cas d'addition tardive de sucre, ce qui influence le calcul des IBUs.
            if f.useAfterBoil == False:
                liste_equivSucrePreBoil.append(f.equivSucre())
                if f.type == model.constants.FERMENTABLE_TYPE_EXTRACT or f.type == model.constants.FERMENTABLE_TYPE_DRY_EXTRACT or f.type == model.constants.FERMENTABLE_TYPE_SUGAR :
                    liste_equivSucreNonMashedPreBoil.append(f.equivSucre())
                else :
                    liste_equivSucreMashedPreBoil.append(f.equivSucre())

        GU= (383.89*sum(liste_equivSucreMashed)/float(self.volume))*((self.efficiency)/100) + (383.89*sum(liste_equivSucreNonMashed)/float(self.volume))
        OG = 1+ (GU/1000) 

        GUPreBoil = (383.89*sum(liste_equivSucreMashedPreBoil)/float(self.volume))*((self.efficiency)/100) + (383.89*sum(liste_equivSucreNonMashedPreBoil)/float(self.volume))
        OGPreBoil = 1+ (self.GUPreBoil/1000)  

        #calcul de la FG. Si il y a plusieurs levures, on recupere l'attenuation la plus elevee.
        levureAttenDec = sorted (self.listeYeasts, reverse = True, key=lambda levure: levure.attenuation)
        if not levureAttenDec : 
            atten = 0.75
        else :
            atten = levureAttenDec[0].attenuation/100
        
        GUF = GU*(1-atten)
        FG = 1 + GUF/1000
        
        
        #calcul des proportions pour les grains
        liste_fProportion = list()
        poidsTot = sum([f.amount for f in self.listeFermentables])
        i = 0
        for f in self.listeFermentables:
            i=i+1
            propGrain = (f.amount / poidsTot)*100
            liste_fProportion.append(propGrain)
     
        
        #calcul de l'amertume : methode de Tinseth
        #IBUs = decimal alpha acid utilization * mg/l of added alpha acids
        
        #mg/l of added alpha acids = decimal AA rating * grams hops * 1000 / liters of wort
        #Decimal Alpha Acid Utilization = Bigness Factor * Boil Time Factor
        #Bigness factor = 1.65 * 0.000125^(wort gravity - 1)
        #Boil Time factor = 1 - e^(-0.04 * time in mins) / 4.15
        liste_btFactor = list()
        liste_ibuPart = list()
        
        bignessFactor = 1.65 * (0.000125**(OGPreBoil - 1))
        ibuTot = 0
        for h in self.listeHops:
            btFactor = (1 - 2.71828182845904523536**(-0.04 * h.time)) / 4.15

            aaUtil = btFactor*self.bignessFactor
            mgAA = (h.alpha/100)*h.amount*1000 / float(self.volume)
            try :
                if h.use != model.constants.HOP_USE_DRY_HOP and h.use != model.constants.HOP_USE_AROMA :
                    ibuTot += (mgAA * aaUtil) + 0.1*(mgAA * aaUtil)
                else :
                    ibuTot += mgAA * aaUtil 
                liste_ibuPart.append(self.ibuPart)
            except:
                if h.form == model.constants.HOP_FORM_PELLET :
                    ibuTot += (mgAA * aaUtil) + 0.1*(mgAA * aaUtil)
                else :
                    ibuTot += mgAA * aaUtil 
        
        #calcul du rapport BU/GU
        try :
            self.ratioBuGu = ibuTot / GU
        except :
            self.ratioBuGu = 0

        
        #calcul de la couleur
        #calcul du MCU pour chaque grain :
        #MCU=4.23*EBC(grain)*Poids grain(Kg)/Volume(L)
        #puis addition de tous les MCU
        #puis calcul EBC total :
        #EBC=2.939*MCU^0.6859
        mcuTot = 0
        for f in self.listeFermentables:
            mcuTot += 4.23*f.color*(f.amount/1000)/float(self.volume)
        EBC = 2.939*(mcuTot**0.6859)
        
        self.colorPreview()
        
        #calcul ABV
        #ABV = 0.130((OG-1)-(FG-1))*1000
        
        ABV = 0.130*((OG-1) -(FG-1))*1000

        self.displayProfile()
