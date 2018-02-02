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


from PyQt5 import QtCore
from PyQt5 import QtGui
import model.constants
import view.constants
import re

class MiscViewLabels(QtCore.QObject):
	def __init__(self):
		QtCore.QObject.__init__(self)
		self.useLabels = {
			model.constants.MISC_USE_BOIL	: self.tr('Ébullition'),
			model.constants.MISC_USE_MASH	: self.tr('Empâtage'),
			model.constants.MISC_USE_PRIMARY	: self.tr('Primaire'),
			model.constants.MISC_USE_SECONDARY	: self.tr('Secondaire'),
			model.constants.MISC_USE_BOTTLING	: self.tr('Embouteillage')
		}

		self.typeLabels = {
			model.constants.MISC_TYPE_SPICE : self.tr('Épice'),
			model.constants.MISC_TYPE_FLAVOR : self.tr('Arôme'),
			model.constants.MISC_TYPE_WATER : self.tr('Traitement Eau'),
			model.constants.MISC_TYPE_HERB : self.tr('Herbe'),
			model.constants.MISC_TYPE_FINING : self.tr('Clarifiant'),
			model.constants.MISC_TYPE_OTHER : self.tr('Autre')
		}

class MiscView(QtCore.QObject):
	def __init__(self, misc):
		QtCore.QObject.__init__(self)
		self.model = misc
		self.miscLabels = MiscViewLabels()

	def miscUseDisplay(self):
		"Return a translated string which can be used in UI for displaying misc ingredient use"
		try:
			return self.miscLabels.useLabels[self.model.use]
		except KeyError :
			return '?miscUseDisplay?'
	def miscTypeDisplay(self):
		try:
			return self.miscLabels.typeLabels[self.model.type]
		except KeyError :
			return '?miscTypeDisplay?'


	def QStandardItem_for_name_type(self):
		'''Return a QStandardItem for displaying Misc name attribute.
		A reference to the model object is stored in MODEL_DATA_ROLE user Role
		'''
		item = QtGui.QStandardItem(self.model.name + ' [' + self.model.type + ']')
		item.setData(self.model, view.constants.MODEL_DATA_ROLE)
		return item
	def QStandardItem_for_amount(self):
		'''Return a QStandardItem for displaying Misc amount attribute.
		A reference to the model object is stored in MODEL_DATA_ROLE user Role
		'''
		item = QtGui.QStandardItem( "%.0f" %(self.model.amount) )
		item.setData(self.model, view.constants.MODEL_DATA_ROLE)
		return item
	def QStandardItem_for_time(self):
		'''Return a QStandardItem for displaying Misc time attribute.
		A reference to the model object is stored in MODEL_DATA_ROLE user Role
		'''
		item = QtGui.QStandardItem( MiscView.time_to_display(self.model.time) )
		item.setData(self.model, view.constants.MODEL_DATA_ROLE)
		return item
	def QStandardItem_for_use(self):
		'''Return a QStandardItem for displaying Misc use attribute.
		A reference to the model object is stored in MODEL_DATA_ROLE user Role
		'''
		item = QtGui.QStandardItem(self.miscUseDisplay())
		item.setData(self.model, view.constants.MODEL_DATA_ROLE)
		return item

	@staticmethod
	def time_to_display(value):
		'''Returns a displayable value for a time value'''
		return "%.0f min" %(value)

	@staticmethod
	def display_to_time(display):
		'''Return a translated display value suitable for using in Misc model instance'''
		return int(display.replace(" min", ""))

	@staticmethod
	def amount_to_display(value):
		'''Returns a displayable value for a amount value'''
		return "%.0f g" %(value)

	@staticmethod
	def display_to_amount(display):
		'''Return a translated display value suitable for using in Misc amount instance'''
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
