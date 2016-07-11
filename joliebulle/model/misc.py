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

import logging
import model.constants
from model.fermentable import *
from model.hop import *

logger = logging.getLogger(__name__)


class Misc(Element):
    """A class for storing Misc attributes"""
    def __init__(self):
        self.amount = 0.0
        self.type = ''
        self.time = 0.0
        self.use = model.constants.MISC_USE_BOIL
    
    def __repr__(self):
        return 'misc[name="%s", amount=%s, type="%s", time=%s, use="%s"]' % (self.name, self.amount, self.type, self.time, self.use)

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