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

class FermentableViewLabels(QtCore.QObject):
	def __init__(self):
		QtCore.QObject.__init__(self)
		self.useLabels = {
			model.constants.FERMENTABLE_USE_BOIL	: self.tr('Brassage'),
			model.constants.FERMENTABLE_USE_AFTER_BOIL	: self.tr('Après ébullition')
		}
		self.typeLabels = {
			model.constants.FERMENTABLE_TYPE_GRAIN	: self.tr('Grain'),
			model.constants.FERMENTABLE_TYPE_SUGAR	: self.tr('Sucre'),
			model.constants.FERMENTABLE_TYPE_EXTRACT	: self.tr('Extrait'),
			model.constants.FERMENTABLE_TYPE_DRY_EXTRACT	: self.tr('Extrait sec'),
			model.constants.FERMENTABLE_TYPE_ADJUNCT	: self.tr('Complément')
		}

class FermentableView(QtCore.QObject):
	def __init__(self, fermentable):
		QtCore.QObject.__init__(self)
		self.model = fermentable
		self.fermentableLabels = FermentableViewLabels()

	def fermentableTypeDisplay(self):
		try:
			return self.fermentableLabels.typeLabels[self.model.type]
		except KeyError :
			return '?fermentableTypeDisplay?'

	def fermentableUseDisplay(self):
		if not self.model.useAfterBoil:
			return self.fermentableLabels.useLabels[model.constants.FERMENTABLE_USE_BOIL]
		else:
			return self.fermentableLabels.useLabels[model.constants.FERMENTABLE_USE_AFTER_BOIL]

	def QStandardItem_for_name(self):
		'''Return a QStandardItem for displaying Fermentable name attribute.
		A reference to the model object is stored in MODEL_DATA_ROLE user Role
		'''
		item = QtGui.QStandardItem(self.model.name)
		item.setData(self.model, view.constants.MODEL_DATA_ROLE)
		return item
	def QStandardItem_for_amount(self):
		'''Return a QStandardItem for displaying Fermentable amount attribute.
		A reference to the model object is stored in MODEL_DATA_ROLE user Role
		'''
		item = QtGui.QStandardItem("%.0f" %(self.model.amount))
		item.setData(self.model, view.constants.MODEL_DATA_ROLE)
		return item
	def QStandardItem_for_type(self):
		'''Return a QStandardItem for displaying Fermentable type attribute.
		A reference to the model object is stored in MODEL_DATA_ROLE user Role
		'''
		item = QtGui.QStandardItem(self.fermentableTypeDisplay())
		item.setData(self.model, view.constants.MODEL_DATA_ROLE)
		return item
	def QStandardItem_for_use(self):
		'''Return a QStandardItem for displaying Fermentable use attribute.
		A reference to the model object is stored in MODEL_DATA_ROLE user Role
		'''
		item = QtGui.QStandardItem(self.fermentableUseDisplay())
		item.setData(self.model, view.constants.MODEL_DATA_ROLE)
		return item

	@staticmethod
	def amount_to_display(value):
		'''Returns a displayable value for a amount value'''
		return "%.0f g" %(value)

	@staticmethod
	def display_to_amount(display):
		'''Return a translated display value suitable for using in Fermentable amount instance'''
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
