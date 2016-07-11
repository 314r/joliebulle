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
import xml.etree.ElementTree as ET
from model.element import Element

logger = logging.getLogger(__name__)

class Fermentable(Element):
    """"A class for storing Fermentable attributes"""

    def __init__(self):
        self.amount = 0.0
        self.type = ''
        self.fyield = 0.0
        self.recommendMash = ''
        self.color = 0.0
        self.useAfterBoil = False

    def __repr__(self):
        return ('fermentable[name="%s", amount=%s, type=%s, yield=%s, recommendMash=%s, color=%s, useAfterBoil=%s]' % 
            (self.name, self.amount, self.type, self.fyield, self.recommendMash, self.color, self.useAfterBoil) )

    def equivSucre(self):
        #division par 1000 et 100 pour passer des g aux kg et parce que le rendement est un pourcentage
        return (self.amount/1000)*(self.fyield/100)

    def copy(self):
        copy = Fermentable()
        copy.name = self.name
        copy.amount = self.amount
        copy.type = self.type
        copy.fyield = self.fyield
        copy.recommendMash = self.recommendMash
        copy.color = self.color
        copy.useAfterBoil = self.useAfterBoil
        return copy

    def toXml(self):
        fermentable = ET.Element('FERMENTABLE')
        fNom = ET.SubElement(fermentable,'NAME')
        fNom.text = self.name
        fVersion = ET.SubElement(fermentable, 'VERSION')
        fVersion.text = '1'            
        fAmount = ET.SubElement(fermentable, 'AMOUNT')
        fAmount.text = str(self.amount/1000)
        fType = ET.SubElement(fermentable, 'TYPE')
        fType.text = self.type
        fYield = ET.SubElement(fermentable,'YIELD')
        fYield.text = str(self.fyield)
        fMashed = ET.SubElement(fermentable,'RECOMMEND_MASH')
        fMashed.text = self.recommendMash
        fUse = ET.SubElement(fermentable,'ADD_AFTER_BOIL')
        if self.useAfterBoil == False:
            fUse.text = 'FALSE'
        else :
            fUse.text = 'TRUE'
        color = ET.SubElement(fermentable, 'COLOR')
        color.text = str(self.color/1.97)
        return fermentable
