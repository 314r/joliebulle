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
import logging
from PyQt4 import QtGui
from PyQt4 import QtCore
from base import *
from globals import *
from preferences_ui import *
from settings import * 
from globals import *

logger = logging.getLogger(__name__)


class CalcBrewday :

    def calcPreBoilVolume(self, volF, boilTime) :
        coolingLossRate = int(settings.conf.value("CoolingLoss")) / 100
        boilOffRate = int(settings.conf.value("BoilOffRate")) / 100   
        self.volPreCool = float(volF)/(1-coolingLossRate)
        #ne pas oublier que le temps d'ébu est en minutes et le taux d'évap par heure
        self.volPreBoil = self.volPreCool/(1-(boilOffRate*int(boilTime)/60))
        
    def calcPreBoilSg(self, GU,volF) :  
        ratio = float(volF)/self.volPreBoil
        GUS = GU * ratio
        self.preBoilSg = 1 + (GUS/1000)
        
    def calcStrikeTemp(self, Ttarget, ratio) :
#        Tstrike = [Ttarget + (0.4 * (Ttarget - Tgrain) / ratio)] + FF  
#        ratio = self.doubleSpinBoxRatio.value()
        fudgeFactor = float(settings.conf.value("FudgeFactor"))
        grainTemp = int(settings.conf.value("GrainTemp"))
        self.strikeTemp = (float(Ttarget) + (0.4 * (float(Ttarget) - int(grainTemp)) / ratio)) + float(fudgeFactor) 
        
    def calcStrikeVol(self, grainWeight, ratio) :
        self.strikeVol = float(grainWeight) * float(ratio) / 1000
        
    def calcMashVolume(self, grainWeight) :
        self.grainVolume = float(grainWeight) * 1.5 / 1000
        #volume d'eau pour saturer le grain
        #1l + 500g de grain = 1.325 l. Au delà le volume d'eau est ajouté en intégralité.
        satGrain = float(grainWeight) * 2 / 1000
        volSat = satGrain * 1.325
        volRestant = self.strikeVol - satGrain
        self.mashVolumeStrike = volSat + volRestant

    def calcMashVolumeBiab(self, grainWeight, strikeVol) :
        self.grainVolume = float(grainWeight) * 1.5 / 1000
        satGrain = float(grainWeight) * 2 / 1000
        volSat = satGrain * 1.325
        volRestant = strikeVol - satGrain
        self.mashVolumeStrike = volSat + volRestant
        
    def calcGrainRetention(self, grainWeight) :
        grainRetentionRate = float(settings.conf.value("GrainRetention"))
        self.grainRetention = grainRetentionRate * grainWeight / 1000
        
    def calcInfusionStep(self, i, grainWeight, listVol, Ttarget, Tmash, Tstrike, stepType) :
        #Vm = Wgrain (0.4 + ratio)
        #Tstrike = (Ttarget*(Vstrike+Vm) - (Vm*Tmash)) / Vstrike

        actualVol = sum(listVol[0:i+1])
        ratio =  actualVol / (float(grainWeight)/ 1000)
        Vm = (float(grainWeight)/1000) * (0.4 + ratio)
        
        
#        Vstrike=((Ttarget*Vm) - (Vm * Tmash)) / (Tstrike - Ttarget)
        
        Tstrike = Tstrike - float(settings.conf.value("FudgeFactor"))
        if stepType == 'Infusion' :
            self.infuseVol = ((float(Ttarget)*Vm) - (Vm * float(Tmash))) / (Tstrike - float(Ttarget))
            self.newRatio = (actualVol + self.infuseVol) / (float(grainWeight)/ 1000)
        elif stepType == 'Temperature' :
            self.infuseVol = 0
            self.newRatio = ratio
        else :
            logger.warn('type non pris en charge')
#        print('actualvol :', actualVol)
#        print('ratio :', ratio)
#        print('vm',Vm)
#        print('strike temp :', Tstrike)
#        print('vol infuse',self.infuseVol)
#        print('listvol :', listVol)
#        print('temp cible :',Ttarget)
        
            
        
    def calcSpargeVol(self, listVol, preBoilVol, grainRetention) :
#        print('listVol :', listVol)
#        print('preBoil :', preBoilVol)
#        print('preBoil :' ,grainRetention)
        if (sum(listVol) - grainRetention) > preBoilVol :
#            print('volume trop élevé')
            self.spargeVol = 0
        else :
            self.spargeVol = preBoilVol - (sum(listVol) - grainRetention)
        
        
        
        
