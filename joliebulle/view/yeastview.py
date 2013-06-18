#JolieBulle 2.9
#Copyright (C) 2010-2013 Pierre Tavares
#Copyright (C) 2012-2013 joliebulle's authors
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
		item = QtGui.QStandardItem(self.yeastDetailDisplay())
		item.setData(self.model, view.constants.MODEL_DATA_ROLE)
		return item
