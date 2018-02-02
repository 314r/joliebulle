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


class Hop(Element):
    """A class for storing Hops attributes"""
    def __init__(self):
        self.amount = 0.0
        self.form = model.constants.HOP_FORM_LEAF
        self.time = 0.0
        self._alpha = 0.0
        self.use = model.constants.HOP_USE_BOIL

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, value):
        if value > 100:
            self._alpha = 100
        elif value < 0:
            self._alpha = 0
        else:
            self._alpha = value

    def __repr__(self):
        return 'hop[name="%s", amount=%s, form=%s, time=%s, alpha=%s, use=%s]' % (self.name, self.amount, self.form, self.time, self.alpha, self.use)

    def copy(self):
        copy = Hop()
        copy.name = self.name
        copy.amount = self.amount
        copy.form = self.form
        copy.time = self.time
        copy._alpha = self._alpha
        copy.use = self.use
        return copy

    def toXml(self):
        hop = ET.Element('HOP')
        hNom = ET.SubElement(hop, 'NAME')
        hVersion = ET.SubElement(hop, 'VERSION')
        hVersion.text = '1'
        hNom.text = self.name
        hAmount = ET.SubElement(hop, 'AMOUNT')
        hAmount.text = str(self.amount/1000)
        hForm = ET.SubElement(hop, 'FORM')
        if self.form == model.constants.HOP_FORM_LEAF:
            hForm.text = 'Leaf'
        elif self.form == model.constants.HOP_FORM_PELLET:
            hForm.text = 'Pellet'
        elif self.form == model.constants.HOP_FORM_PLUG:
            hForm.text = 'Plug'   
            
        hTime = ET.SubElement(hop, 'TIME')
        hTime.text = str(self.time)
        hAlpha = ET.SubElement(hop, 'ALPHA')
        hAlpha.text = str(self.alpha)
        hUse = ET.SubElement(hop, 'USE')
        if self.use == model.constants.HOP_USE_BOIL :
            hUse.text = 'Boil'
        if self.use == model.constants.HOP_USE_DRY_HOP :
            hUse.text = 'Dry Hop'  
        if self.use == model.constants.HOP_USE_MASH :
            hUse.text = 'Mash'
        if self.use == model.constants.HOP_USE_FIRST_WORT :
            hUse.text = 'First Wort' 
        if self.use == model.constants.HOP_USE_AROMA :
            hUse.text = 'Aroma'  
        else :
            hUse.text = 'Boil'
        return hop