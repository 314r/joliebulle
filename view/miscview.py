from PyQt4 import QtCore
from PyQt4 import QtGui
import model.constants
import view.constants
import re

class MiscViewLabels(QtCore.QObject):
	def __init__(self):
		QtCore.QObject.__init__(self)
		self.useLabels = {
			model.constants.MISC_USE_BOIL	: self.trUtf8('Ébullition'),
			model.constants.MISC_USE_MASH	: self.trUtf8('Empâtage'),
			model.constants.MISC_USE_PRIMARY	: self.trUtf8('Primaire'),
			model.constants.MISC_USE_SECONDARY	: self.trUtf8('Secondaire'),
			model.constants.MISC_USE_BOTTLING	: self.trUtf8('Embouteillage')
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
