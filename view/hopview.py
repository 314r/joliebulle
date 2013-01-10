from PyQt4 import QtCore
from PyQt4 import QtGui
import model.constants
import view.constants

class HopViewLabels(QtCore.QObject):
	def __init__(self):
		QtCore.QObject.__init__(self)
		self.formLabels = {
			model.constants.HOP_FORM_PELLET	: self.trUtf8('Pellet'),
			model.constants.HOP_FORM_LEAF	: self.trUtf8('Feuille'),
			model.constants.HOP_FORM_PLUG	: self.trUtf8('Cône')
		}
		self.useLabels = {
			model.constants.HOP_USE_BOIL	: self.trUtf8('Ébullition'),
			model.constants.HOP_USE_DRY_HOP	: self.trUtf8('Dry Hop'),
			model.constants.HOP_USE_MASH	: self.trUtf8('Empâtage'),
			model.constants.HOP_USE_FIRST_WORT	: self.trUtf8('Premier Moût'),
			model.constants.HOP_USE_AROMA	: self.trUtf8('Arôme')
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
		item = QtGui.QStandardItem( "%.0f" %(self.model.time) )
		item.setData(self.model, view.constants.MODEL_DATA_ROLE)
		return item
	def QStandardItem_for_alpha(self):
		'''Return a QStandardItem for displaying Hop alpha attribute.
		A reference to the model object is stored in MODEL_DATA_ROLE user Role
		'''
		item = QtGui.QStandardItem( "%.1f" %(self.model.alpha) )
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