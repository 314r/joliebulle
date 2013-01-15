from PyQt4 import QtCore
from PyQt4 import QtGui
import model.constants
import view.constants
import re

class FermentableViewLabels(QtCore.QObject):
	def __init__(self):
		QtCore.QObject.__init__(self)
		self.useLabels = {
			model.constants.FERMENTABLE_USE_BOIL	: self.trUtf8('Brassage'),
			model.constants.FERMENTABLE_USE_AFTER_BOIL	: self.trUtf8('Après ébullition')
		}
		self.typeLabels = {
			model.constants.FERMENTABLE_TYPE_GRAIN	: self.trUtf8('Grain'),
			model.constants.FERMENTABLE_TYPE_SUGAR	: self.trUtf8('Sucre'),
			model.constants.FERMENTABLE_TYPE_EXTRACT	: self.trUtf8('Extrait'),
			model.constants.FERMENTABLE_TYPE_DRY_EXTRACT	: self.trUtf8('Extrait sec'),
			model.constants.FERMENTABLE_TYPE_ADJUNCT	: self.trUtf8('Complément')
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
