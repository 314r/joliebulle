from PyQt4 import QtCore
from PyQt4 import QtGui
import model.constants
import view.constants

class RecipeView(QtCore.QObject):
	def __init__(self, recipe):
		QtCore.QObject.__init__(self)
		self.model = recipe

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
