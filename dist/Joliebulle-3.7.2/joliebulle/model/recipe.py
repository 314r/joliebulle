#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­

#joliebulle 3.6
#Copyright (C) 2010-2016 Pierre Tavares
#Copyright (C) 2012-2015 joliebulle's authors
#See AUTHORS file.

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
from encodings.punycode import selective_find

import logging
import model.constants
from model.element import Element
from model.fermentable import *
from model.hop import *
from model.yeast import *
from model.misc import *
from model.mash import *
from helper.recipeExporterRepository import *
from errors import *

logger = logging.getLogger(__name__)

class Recipe(Element):
    """A class for storing recipes attributes"""
    def __init__(self):
        self.path=""
        self.name = ""
        self.brewer = ""
        self.type = model.constants.RECIPE_TYPE_ALL_GRAIN
        self.volume = 0.0
        self.efficiency = 0.0
        self.boil = 0.0
        self.recipeNotes = ""
        self.style = ""
        self.mash = Mash()
        self.listeFermentables = list()
        self.listeHops = list()
        self.listeYeasts = list()
        self.listeMiscs = list()
        self.listeMashSteps = list()
        

    def __repr__(self):
        return ('recipe[name="%s", brewer="%s", type=%s, volume=%s, efficiency=%s, boil=%s, recipeNotes="%s", style="%s"]' %
                (self.name, self.brewer, self.type, self.volume, self.efficiency, self.boil, self.recipeNotes, self.style) )

    def export(self, type):
        return RecipeExporterRepository[type](self)

    def compute_fermentablesWeight(self):
        return sum([f.amount for f in self.listeFermentables])

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
            print (mcuTot)
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
                else :
                    ibu = 0
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

    def compute_grainWeight(self):
        return sum([f.amount for f in self.listeFermentables if f.type != model.constants.FERMENTABLE_TYPE_SUGAR and f.type != model.constants.FERMENTABLE_TYPE_EXTRACT and f.type != model.constants.FERMENTABLE_TYPE_DRY_EXTRACT] )
