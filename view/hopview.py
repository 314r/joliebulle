from PyQt4 import QtCore
from PyQt4 import QtGui
import model.constants
import view.constants


class HopView(QtCore.QObject):
	def __init__(self, hop):
		QtCore.QObject.__init__(self)
		self.model = hop

	def hopFormDisplay(self):
		"""Return a translated string which can bu used in UI for displaying hop form"""

		if self.model.form == model.constants.HOP_FORM_PELLET :
			return self.trUtf8('''Pellet''')
		if self.model.form == model.constants.HOP_FORM_LEAF :
			return self.trUtf8('''Feuille''')
		if self.model.form == model.constants.HOP_FORM_PLUG :
			return self.trUtf8('''Cône''')
		return '?hopFormDisplay?'

	def hopUseDisplay(self):
		"""Return a translated string which can bu used in UI for displaying hop use"""
		if self.model.use == model.constants.HOP_USE_BOIL :
			return self.trUtf8('''Ébullition''')
		if self.model.use == model.constants.HOP_USE_DRY_HOP :
			return self.trUtf8('Dry Hop')
		if self.model.use == model.constants.HOP_USE_MASH :
			return self.trUtf8('Empâtage')
		if self.model.use == model.constants.HOP_USE_FIRST_WORT :
			return self.trUtf8('Premier Moût')
		if self.model.use == model.constants.HOP_USE_AROMA :
			return self.trUtf8('Arôme')
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