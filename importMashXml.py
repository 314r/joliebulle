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


import os
from sys import platform
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from preferences import *
from globals import *
import xml.etree.ElementTree as ET

class ImportMash : 


    def importBeerXML(self) :
    
        self.listMash =[] 
        
        arbre = ET.parse(mash_file)

        mash = arbre.findall('.//MASH')
        
        self.numMash = len(mash)
        
        i = 0
        while i < self.numMash :

            i=i+1
            for nom in mash[i-1] :
                if nom.tag == 'NAME' :
                    self.mashName = nom.text
                    self.listMash.append({'name' : self.mashName})
                    
            for nom in mash[i-1] :
                if nom.tag == 'PH' :
                    self.mashPh = nom.text
                    dic = self.listMash[i-1]
                    dic['ph'] = self.mashPh
            
            for nom in mash[i-1] :
                if nom.tag == 'GRAIN_TEMP' :
                    self.mashGrainTemp = nom.text
                    dic = self.listMash[i-1]
                    dic['grainTemp'] = self.mashGrainTemp
                    
            for nom in mash[i-1] :
                if nom.tag == 'TUN_TEMP' :
                    self.mashTunTemp = nom.text
                    dic = self.listMash[i-1]
                    dic['tunTemp'] = self.mashTunTemp

            for nom in mash[i-1] :
                if nom.tag == 'SPARGE_TEMP' :
                    self.mashSpargeTemp = nom.text
                    dic = self.listMash[i-1]
                    dic['spargeTemp'] = self.mashSpargeTemp            
            
                    
            steps = mash[i-1].findall('.//MASH_STEP')
            self.numSteps = len(steps)
            self.listSteps = []
            dic ['mashSteps'] = self.listSteps
            j=0
            while j < self.numSteps :
                j=j+1
                for nom in steps[j-1] :
                    if nom.tag == 'NAME' :
                        self.stepName = nom.text
                        self.listSteps.append({'name' : self.stepName})
                    
                for nom in steps[j-1] :
                    if nom.tag == 'TYPE' :
                        self.stepType = nom.text
                        dicStep = self.listSteps[j-1]
                        dicStep['type']= self.stepType       
                for nom in steps[j-1] :
                    if nom.tag == 'STEP_TIME' :   
                         self.stepTime = nom.text
                         dicStep = self.listSteps[j-1]
                         dicStep['stepTime']= self.stepTime 
                for nom in steps[j-1] :
                    if nom.tag == 'STEP_TEMP' :
                         self.stepTemp = nom.text
                         dicStep = self.listSteps[j-1]
                         dicStep['stepTemp']= self.stepTemp
                for nom in steps[j-1] :
                    if nom.tag == 'INFUSE_AMOUNT' :
                         self.stepVol = nom.text
                         dicStep = self.listSteps[j-1]
                         dicStep['stepVol']= self.stepVol
                    
        
            
        
        

