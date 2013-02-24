from PyQt4 import QtCore
from PyQt4 import QtGui
import model.constants
import view.constants

class MashStepView(QtCore.QObject):
	def __init__(self, step):
		QtCore.QObject.__init__(self)
		self.model = step

	def mashTypeDisplay(self):
		if self.model.type == model.constants.MASH_STEP_INFUSION:
			return self.trUtf8('''Infusion''')
		if self.model.type == model.constants.MASH_STEP_TEMPERATURE:
			return self.trUtf8('''Température''')
		if self.model.type == model.constants.MASH_STEP_DECOCTION:
			return self.trUtf8('''Décoction''')
		return '?mashTypeDisplay?'

	@staticmethod
	def time_to_display(value):
		'''Returns a displayable value for a time value'''
		return "%s min" %(value)

	@staticmethod
	def temp_to_display(value):
		'''Returns a displayable value for a time value'''
		return "%s °C" %(value)
