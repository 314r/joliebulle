#!/usr/bin/python3
#­*­coding: utf­8 -­*­



#JolieBulle 2.5
#Copyright (C) 2010-2011 Pierre Tavares

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
from base import *
from globals import *
from preferences_ui import *
from settings import * 
from globals import *


class CalcBrewday :

    def calcPreBoilVolume(self, volF, boilTime) :
    
        coolingLossRate = int(settings.conf.value("CoolingLoss")) / 100
        boilOffRate = int(settings.conf.value("BoilOffRate")) / 100
    
        self.volPreCool = int(volF)/(1-coolingLossRate)
        #ne pas oublier que le temps d'ébu est en minutes et le taux d'évap par heure
        self.volPreBoil = self.volPreCool/(1-(boilOffRate*int(boilTime)/60))
        
    def calcPreBoilSg(self, GU,volF) :
    
        ratio = int(volF)/self.volPreBoil
        GUS = GU * ratio
        self.preBoilSg = 1 + (GUS/1000)
        
