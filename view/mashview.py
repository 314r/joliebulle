from PyQt4 import QtCore
from PyQt4 import QtGui
import model.constants
import view.constants

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