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


class Yeast(Element):
    """A class for storing Yeast attributes"""
    def __init__(self):
        self.form = ''
        self.labo = ''
        self.productId = ''
        self.attenuation = 0.0
    
    def __repr__(self):
        return ('yeast[name="%s", form=%s, labo=%s, productId=%s, attenuation=%s]' % 
                (self.name, self.form, self.labo, self.productId, self.attenuation))

    def copy(self):
        copy = Yeast()
        copy.name = self.name
        copy.form = self.form
        copy.labo = self.labo
        copy.productId = self.productId
        copy.attenuation = self.attenuation
        return copy

    def toXml(self):
        yeast = ET.Element('YEAST')
        lNom = ET.SubElement(yeast, 'NAME')
        lVersion = ET.SubElement(yeast, 'VERSION')
        lVersion.text = '1'
        lType = ET.SubElement(yeast ,'TYPE')
        lType = 'Ale'
        lNom.text = self.name
        lForm = ET.SubElement(yeast, 'FORM')
        lForm.text = self.form
        lLabo = ET.SubElement(yeast, 'LABORATORY')
        lLabo.text = self.labo
        lProd = ET.SubElement(yeast, 'PRODUCT_ID')
        lProd.text = self.productId
        lAtten = ET.SubElement(yeast, 'ATTENUATION')
        lAtten.text = str(self.attenuation)
        return yeast
