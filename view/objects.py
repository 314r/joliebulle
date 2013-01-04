from PyQt4 import QtCore
from PyQt4 import QtGui
import model.constants


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
		return QtGui.QStandardItem(self.model.name)
	def QStandardItem_for_amount(self):
		return QtGui.QStandardItem( "%.0f" %(self.model.amount) )
	def QStandardItem_for_time(self):
		return QtGui.QStandardItem( "%.0f" %(self.model.time) )
	def QStandardItem_for_alpha(self):
		return QtGui.QStandardItem( "%.1f" %(self.model.alpha) )
	def QStandardItem_for_form(self):
		return QtGui.QStandardItem(self.hopFormDisplay())
	def QStandardItem_for_use(self):
		return QtGui.QStandardItem(self.hopUseDisplay())

class MiscView(QtCore.QObject):
	def __init__(self, misc):
		QtCore.QObject.__init__(self)
		self.model = misc

	def miscUseDisplay(self):
		"Return a translated string which can be used in UI for displaying misc ingredient use"
		if self.model.use == model.constants.MISC_USE_BOIL :
			return self.trUtf8('Ébullition')
		if self.model.use == model.constants.MISC_USE_MASH :
			return self.trUtf8('Empâtage')
		if self.model.use == model.constants.MISC_USE_PRIMARY :
			return self.trUtf8('Primaire')		
		if self.model.use == model.constants.MISC_USE_SECONDARY :
			return self.trUtf8('Secondaire')
		if self.model.use == model.constants.MISC_USE_BOTTLING :
			return self.trUtf8('Embouteillage')
		return '?miscUseDisplay?'

class YeastView(QtCore.QObject):
	def __init__(self, yeast):
		QtCore.QObject.__init__(self)
		self.model = yeast

	def yeastDetailDisplay(self):
		return "%s %s %s" % (self.model.name, self.model.labo, self.model.productId)

class MashView(QtCore.QObject):
	def __init__(self, yeast):
		QtCore.QObject.__init__(self)
		self.model = yeast

	def mashTypeDisplay(self):
		if self.model.type == model.constants.MASH_STEP_INFUSION:
			return self.trUtf8('''Infusion''')
		if self.model.type == model.constants.MASH_STEP_TEMPERATURE:
			return self.trUtf8('''Température''')
		if self.model.type == model.constants.MASH_STEP_DECOCTION:
			return self.trUtf8('''Décoction''')
		return '?mashTypeDisplay?'

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

class RecipeView(QtCore.QObject):
	def __init__(self, recipe):
		QtCore.QObject.__init__(self)
		self.model = recipe

	def QStandardItem_for_fermentable_propertion(self, fermentable):
		proportion = self.model.compute_proportions()[fermentable]
		return QtGui.QStandardItem("%.0f %%" %(proportion))

	def QStandardItem_for_hop_ibu(self, hop):
		ibu = self.model.compute_IBUPart()[hop]
		return QtGui.QStandardItem("%.1f IBU" %(ibu))
