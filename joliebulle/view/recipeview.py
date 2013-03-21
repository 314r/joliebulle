from PyQt4 import QtCore
from PyQt4 import QtGui
import model.constants
import view.constants

class recipeViewLabels(QtCore.QObject):
	def __init__(self):
		QtCore.QObject.__init__(self)
		self.typeLabels = {
			model.constants.RECIPE_TYPE_ALL_GRAIN	: self.trUtf8('Tout grain'),
			model.constants.RECIPE_TYPE_PARTIAL_MASH	: self.trUtf8('Extrait'),
			model.constants.RECIPE_TYPE_EXTRACT	: self.trUtf8('Partial mash'),
		}

class RecipeView(QtCore.QObject):
	def __init__(self, recipe):
		QtCore.QObject.__init__(self)
		self.model = recipe
		self.recipeViewLabels = recipeViewLabels()

	def QStandardItem_for_fermentable_proportion(self, fermentable):
		proportion = self.model.compute_proportions()[fermentable]
		item = QtGui.QStandardItem("%.0f %%" %(proportion))
		item.setData(fermentable, view.constants.MODEL_DATA_ROLE)
		return item

	def QStandardItem_for_hop_ibu(self, hop):
		ibu = self.model.compute_IBUPart()[hop]
		item = QtGui.QStandardItem("%.1f IBU" %(ibu))
		item.setData(hop, view.constants.MODEL_DATA_ROLE)
		return item

	def recipeTypeDisplay(self):
		"""Return a translated string which can be used in UI for displaying recipe type"""
		try:
			return self.recipeViewLabels.typeLabels[self.model.type]
		except KeyError :
			return '?recipeTypeDisplay?'

