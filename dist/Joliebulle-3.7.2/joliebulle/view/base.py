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


from PyQt5 import QtGui
from base import ImportBase
from view.yeastview import *

def getFermentablesQtModel():
	model = QtGui.QStandardItemModel()
	for f in ImportBase().listeFermentables:
		item = QtGui.QStandardItem(f.name)
		item.setData(f, view.constants.MODEL_DATA_ROLE)
		model.appendRow(item)
	return model

def getHopsQtModel():
	model = QtGui.QStandardItemModel()
	for h in ImportBase().listeHops :
		item = QtGui.QStandardItem(h.name)
		item.setData(h, view.constants.MODEL_DATA_ROLE)
		model.appendRow(item)
	return model

def getMiscsQtModel():
	model = QtGui.QStandardItemModel()
	for m in ImportBase().listeMiscs:
		item = QtGui.QStandardItem(m.name)
		item.setData(m, view.constants.MODEL_DATA_ROLE)
		model.appendRow(item)
	return model

def getYeastsQtModel():
	model = QtGui.QStandardItemModel()
	for y in ImportBase().listeYeasts:
		item = QtGui.QStandardItem(YeastView(y).yeastDetailDisplay())
		item.setData(y, view.constants.MODEL_DATA_ROLE)
		model.appendRow(item)
	return model