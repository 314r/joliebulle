from PyQt4 import QtCore
from PyQt4 import QtGui
import model.constants
import view.constants

class FermentableView(QtCore.QObject):
	def __init__(self, fermentable):
		QtCore.QObject.__init__(self)
		self.model = fermentable

	def fermentableTypeDisplay(self):
		if self.model.type == model.constants.FERMENTABLE_TYPE_GRAIN:
			return self.trUtf8('Grain')
		if self.model.type == model.constants.FERMENTABLE_TYPE_SUGAR:
			return self.trUtf8('Sucre')
		if self.model.type == model.constants.FERMENTABLE_TYPE_EXTRACT:
			return self.trUtf8('Extrait')
		if self.model.type == model.constants.FERMENTABLE_TYPE_DRY_EXTRACT:
			return self.trUtf8('Extrait sec')
		if self.model.type == model.constants.FERMENTABLE_TYPE_ADJUNCT:
			return self.trUtf8('Complément')
		return '?fermentableTypeDisplay?'

	def fermentableUseDisplay(self):
		if not self.model.useAfterBoil:
			return self.trUtf8('Brassage')
		else:
			return self.trUtf8('Après ébullition')

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
