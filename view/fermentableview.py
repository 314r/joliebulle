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
		return self.trUtf8('Brassage')

	def QStandardItem_for_name(self):
		return QtGui.QStandardItem(self.model.name)
	def QStandardItem_for_amount(self):
		return QtGui.QStandardItem("%.0f" %(self.model.amount))
	def QStandardItem_for_type(self):
		return QtGui.QStandardItem(self.fermentableTypeDisplay())
	def QStandardItem_for_use(self):
		return QtGui.QStandardItem(self.fermentableUseDisplay())