from PyQt4 import QtGui
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