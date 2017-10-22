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
from PyQt5 import QtCore
from PyQt5 import QtGui
import model.constants
import view.constants
import re

logger = logging.getLogger(__name__)

class HopViewLabels(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.formLabels = {
            model.constants.HOP_FORM_PELLET : self.tr('Pellet'),
            model.constants.HOP_FORM_LEAF   : self.tr('Feuille'),
            model.constants.HOP_FORM_PLUG   : self.tr('Cône')
        }
        self.useLabels = {
            model.constants.HOP_USE_BOIL    : self.tr('Ébullition'),
            model.constants.HOP_USE_DRY_HOP : self.tr('Dry Hop'),
            model.constants.HOP_USE_MASH    : self.tr('Empâtage'),
            model.constants.HOP_USE_FIRST_WORT  : self.tr('Premier Moût'),
            model.constants.HOP_USE_AROMA   : self.tr('Arôme')
        }

class HopView(QtCore.QObject):
    def __init__(self, hop):
        QtCore.QObject.__init__(self)
        self.model = hop
        self.hopLabels = HopViewLabels()

    def hopFormDisplay(self):
        """Return a translated string which can bu used in UI for displaying hop form"""
        try:
            return self.hopLabels.formLabels[self.model.form]
        except KeyError :
            return '?hopFormDisplay?'

    def hopUseDisplay(self):
        """Return a translated string which can bu used in UI for displaying hop use"""
        try:
            return self.hopLabels.useLabels[self.model.use]
        except KeyError :
            return '?hopUseDisplay?'

    def QStandardItem_for_name(self):
        '''Return a QStandardItem for displaying Hop name attribute.
        A reference to the model object is stored in MODEL_DATA_ROLE user Role
        '''
        item = QtGui.QStandardItem(self.model.name)
        item.setData(self.model, view.constants.MODEL_DATA_ROLE)
        return item
    def QStandardItem_for_amount(self):
        '''Return a QStandardItem for displaying Hop amount attribute.
        A reference to the model object is stored in MODEL_DATA_ROLE user Role
        '''
        item = QtGui.QStandardItem( "%.0f" %(self.model.amount) )
        item.setData(self.model, view.constants.MODEL_DATA_ROLE)
        return item
    def QStandardItem_for_time(self):
        '''Return a QStandardItem for displaying Hop time attribute.
        A reference to the model object is stored in MODEL_DATA_ROLE user Role
        '''
        item = QtGui.QStandardItem( HopView.time_to_display(self.model.time) )
        item.setData(self.model, view.constants.MODEL_DATA_ROLE)
        return item
    def QStandardItem_for_alpha(self):
        '''Return a QStandardItem for displaying Hop alpha attribute.
        A reference to the model object is stored in MODEL_DATA_ROLE user Role
        '''
        item = QtGui.QStandardItem(HopView.alpha_to_display(self.model.alpha) )
        item.setData(self.model, view.constants.MODEL_DATA_ROLE)
        return item
    def QStandardItem_for_form(self):
        '''Return a QStandardItem for displaying Hop form attribute.
        A reference to the model object is stored in MODEL_DATA_ROLE user Role
        '''
        item = QtGui.QStandardItem(self.hopFormDisplay())
        item.setData(self.model, view.constants.MODEL_DATA_ROLE)
        return item
    def QStandardItem_for_use(self):
        '''Return a QStandardItem for displaying Hop use attribute.
        A reference to the model object is stored in MODEL_DATA_ROLE user Role
        '''
        item = QtGui.QStandardItem(self.hopUseDisplay())
        item.setData(self.model, view.constants.MODEL_DATA_ROLE)
        return item

    @staticmethod
    def alpha_to_display(value):
        '''Returns a displayable value for a alpha value'''
        return "%.2f %%" %(value)

    @staticmethod
    def display_to_alpha(display):
        '''Return a translated display value suitable for using in Hop model instance'''
        return float(display.replace(" %", ""))

    @staticmethod
    def time_to_display(value):
        '''Returns a displayable value for a time value'''
        return "%.0f min" %(value)

    @staticmethod
    def display_to_time(display):
        '''Return a translated display value suitable for using in Hop model instance'''
        return int(display.replace(" min", ""))

    @staticmethod
    def amount_to_display(value):
        '''Returns a displayable value for a amount value'''
        return "%.0f g" %(value)

    @staticmethod
    def display_to_amount(display):
        '''Return a translated display value suitable for using in Hop amount instance'''
        m = re.search('([\d\.]+)\ *([a-zA-Z]*)',display)
        data = m.group(1)
        unit = m.group(2)
        value = None
        if unit == "g" :
            value =  int(data)
        if unit == "kg" :
            value =  int(float(data)*1000)
        elif unit == "oz" : 
            value = int(float(data) * 28.349)
        elif unit == "lb" : 
            value = int(float(data) * 453.59237)
        else:
            value = int(data)
        return value
