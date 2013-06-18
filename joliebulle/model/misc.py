#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­



#JolieBulle 2.9
#Copyright (C) 2010-2013 Pierre Tavares
#Copyright (C) 2012-2013 joliebulle's authors
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

import logging
import model.constants
from model.fermentable import *
from model.hop import *

logger = logging.getLogger(__name__)

class Misc:
    """A class for storing Misc attributes"""
    def __init__(self):
        self.name = ''
        self.amount = 0.0
        self.type = ''
        self.time = 0.0
        self.use = model.constants.MISC_USE_BOIL
    
    def __repr__(self):
        return 'misc[name="%s", amount=%s, type="%s", time=%s, use="%s"]' % (self.name, self.amount, self.type, self.time, self.use)
        
    @staticmethod
    def parse(element):
        m = Misc()
        for balise in element:
            if 'NAME' == balise.tag :
                m.name = balise.text
            elif 'AMOUNT' == balise.tag :
                m.amount = float(balise.text)*1000
            elif 'TYPE' == balise.tag :
                m.type = balise.text
            elif 'TIME' == balise.tag:
                try :
                    m.time = float(balise.text)
                except : 
                    m.time = 0.0
                    logger.debug("misc time attribute is not numeric:%s", balise.text)
            elif 'USE' == balise.tag:
                if 'Boil' == balise.text:
                    m.use = model.constants.MISC_USE_BOIL
                elif 'Mash' == balise.text:
                    m.use = model.constants.MISC_USE_MASH
                elif 'Primary' == balise.text:
                    m.use = model.constants.MISC_USE_PRIMARY
                elif 'Secondary' == balise.text:
                    m.use = model.constants.MISC_USE_SECONDARY
                elif 'Bottling' == balise.text:
                    m.use = model.constants.MISC_USE_BOTTLING
                else :
                    logger.warn ("Unkown misc use '%s', assuming 'Boil' by default", balise.text)
                    m.use = model.constants.MISC_USE_BOIL

        #logger.debug(repr(m))
        return m

    def copy(self):
        copy = Misc()
        copy.name = self.name
        copy.amount = self.amount
        copy.type = self.type
        copy.time = self.time
        copy.use = self.use
        return copy

    def toXml(self):
        misc = ET.Element('MISC')
        dNom = ET.SubElement(misc, 'NAME')
        dNom.text = self.name
        dVersion = ET.SubElement(misc, 'VERSION')
        dVersion.text = '1'
        dAmount = ET.SubElement(misc, 'AMOUNT')
        dAmount.text = str(self.amount/1000)
        dType = ET.SubElement(misc, 'TYPE')
        dType.text = self.type
        dTime = ET.SubElement(misc, 'TIME')
        dTime.text = str(self.time)
        dUse = ET.SubElement(misc, 'USE')
        if self.use == model.constants.MISC_USE_BOIL :
            dUse.text = 'Boil'
        if self.use == model.constants.MISC_USE_MASH :
            dUse.text = 'Mash'
        if self.use == model.constants.MISC_USE_PRIMARY :
            dUse.text = 'Primary'        
        if self.use == model.constants.MISC_USE_SECONDARY :
            dUse.text = 'Secondary'
        if self.use == model.constants.MISC_USE_BOTTLING :
            dUse.text = 'Bottling'       
        else :
            dUse.text = 'Boil'
        return misc