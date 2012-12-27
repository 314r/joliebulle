from PyQt4 import QtCore
import model.constants


class HopUI(QtCore.QObject):
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

class MiscUI(QtCore.QObject):
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

class YeastUI(QtCore.QObject):
	def __init__(self, yeast):
		QtCore.QObject.__init__(self)
		self.model = yeast

	def yeastDetailDisplay(self):
		return "%s %s %s" % (self.model.name, self.model.labo, self.model.productId)

class MashUI(QtCore.QObject):
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