#!/usr/bin/python3
#­*­coding: utf­8 -­*­

import os
from sys import platform
import PyQt5
import sys
from operator import itemgetter
from PyQt5 import QtGui
from PyQt5 import QtCore
from preferences import *
from globals import *
import xml.etree.ElementTree as ET

class ExportMash :

    def export(self,listMash) :
#        print (listMash)
        
        self.database = ET.Element('DATABASE')
        listMash = sorted(listMash, key=attrgetter('name')) 
        for m in listMash:
            mash = ET.SubElement(self.database, 'MASH')
            mashVersion = ET.SubElement(mash, 'VERSION')
            mashVersion.text = '1'
            mashName = ET.SubElement(mash, 'NAME')
            mashName.text = m.name
            grainTemp = ET.SubElement(mash, 'GRAIN_TEMP')
#            grainTemp.text = dicMash['grainTemp']
            grainTemp.text = '20'
            tunTemp = ET.SubElement(mash, 'TUN_TEMP')
#            tunTemp.text = dicMash['tunTemp']
            tunTemp.text = '20'
            ph = ET.SubElement(mash, 'PH')
            ph.text = str(m.ph)
            spargeTemp = ET.SubElement(mash, 'SPARGE_TEMP')
            spargeTemp.text =str(m.spargeTemp)
            steps = ET.SubElement(mash, 'MASH_STEPS')
            
            for s in m.listeSteps:
                step = ET.SubElement(steps, 'MASH_STEP')
                stepVersion = ET.SubElement(step, 'VERSION')
                stepVersion.text = '1'
                stepName = ET.SubElement(step, 'NAME')
                stepName.text = s.name
                stepType = ET.SubElement(step, 'TYPE')
                stepType.text = s.type
                stepTemp = ET.SubElement(step, 'STEP_TEMP')
                stepTemp.text = str(s.temp)
                stepTime = ET.SubElement(step, 'STEP_TIME')
                stepTime.text = str(s.time)
                stepVol = ET.SubElement(step, 'INFUSE_AMOUNT')
#                stepVol.text = dicStep['stepVol']
                stepVol.text = '0'
            
    def enregistrer (self, s) :    
        ET.ElementTree(self.database).write(s,encoding="utf-8")


    def exportJson(self, listMash) :
        listMash = sorted(listMash, key=attrgetter('name')) 
        # print(listMash)

        dic = {}

        mashes=[]
        for m in listMash :
            mash = {}
            mash['name'] = m.name
            mash['ph'] = m.ph
            mash['sparge'] = m.spargeTemp
            steps=[]
            mashes.append(mash)
            for s in m.listeSteps :
                step = {}
                step['name'] = s.name
                step['temp'] = s.temp
                step['time'] = s.time
                step['type'] = s.type
                steps.append(step)
            mash['steps'] = steps
            
        dic['mashes'] = mashes
        dic = json.dumps(dic)

        return dic





            
            
                
                
        
