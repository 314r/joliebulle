#joliebulle 3.5
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

class YeastViewLabels(QtCore.QObject):
    def __init__(self):
        QtCore.QObject.__init__(self)
        self.formLabels = {
            model.constants.YEAST_FORM_LIQUID : self.tr('Liquide'),
            model.constants.YEAST_FORM_DRY : self.tr('Sèche'),
            model.constants.YEAST_FORM_SLANT : self.tr('Gélose'),
            model.constants.YEAST_FORM_CULTURE : self.tr('Culture')
        }


class YeastView(QtCore.QObject):
    def __init__(self, yeast):
        QtCore.QObject.__init__(self)
        self.model = yeast
        self.yeastLabels = YeastViewLabels()

    def yeastFormDisplay(self) :
        try:
            return self.yeastLabels.formLabels[self.model.form]
        except KeyError :
            return '?yeastFormDisplay?'

    def yeastDetailDisplay(self):
        return "%s %s %s" % (self.model.name, self.model.labo, self.model.productId)
    def QStandardItem_for_detail(self):
        item = QtGui.QStandardItem(self.yeastDetailDisplay())
        item.setData(self.model, view.constants.MODEL_DATA_ROLE)
        return item
