from PyQt4 import QtCore
from PyQt4 import QtGui
import model.constants
import view.constants

class YeastView(QtCore.QObject):
	def __init__(self, yeast):
		QtCore.QObject.__init__(self)
		self.model = yeast

	def yeastDetailDisplay(self):
		return "%s %s %s" % (self.model.name, self.model.labo, self.model.productId)
	def QStandardItem_for_detail(self):
		return QtGui.QStandardItem(self.yeastDetailDisplay())