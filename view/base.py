from PyQt4 import QtGui
from base import ImportBase
from view.yeastview import *

def getFermentablesQtModel():
    return QtGui.QStringListModel( [f.name for f in ImportBase().listeFermentables] )

def getHopsQtModel():
    return QtGui.QStringListModel( [h.name for h in ImportBase().listeHops] )

def getMiscsQtModel():
    return QtGui.QStringListModel( [m.name for m in ImportBase().listeMiscs] )

def getYeastsQtModel():
    return QtGui.QStringListModel( [ YeastView(y).yeastDetailDisplay() for y in ImportBase().listeYeasts] )
