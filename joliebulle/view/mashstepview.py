#joliebulle 3.6
#Copyright (C) 2010-2016 Pierre Tavares
#Copyright (C) 2012-2015 joliebulle's authors
#See AUTHORS file.

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 3
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.


from PyQt5 import QtCore
from PyQt5 import QtGui
import model.constants
import view.constants

class MashStepView(QtCore.QObject):
	def __init__(self, step):
		QtCore.QObject.__init__(self)
		self.model = step

	def mashTypeDisplay(self):
		if self.model.type == model.constants.MASH_STEP_INFUSION:
			return self.tr('''Infusion''')
		if self.model.type == model.constants.MASH_STEP_TEMPERATURE:
			return self.tr('''Température''')
		if self.model.type == model.constants.MASH_STEP_DECOCTION:
			return self.tr('''Décoction''')
		return '?mashTypeDisplay?'

	@staticmethod
	def time_to_display(value):
		'''Returns a displayable value for a time value'''
		return "%s min" %(value)

	@staticmethod
	def temp_to_display(value):
		'''Returns a displayable value for a time value'''
		return "%s °C" %(value)
