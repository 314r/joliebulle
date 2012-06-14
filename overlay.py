#!/usr/bin/python3
#­*­coding: utf­8 -­*­



#JolieBulle 2.6
#Copyright (C) 2010-2012 Pierre Tavares

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



import os
from sys import platform
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Overlay(QtGui.QWidget):
 
    def __init__(self, parent = None):
 
        QtGui.QWidget.__init__(self, parent)
        palette = QtGui.QPalette(self.palette())
        palette.setColor(palette.Background, QtCore.Qt.transparent)
        self.setPalette(palette)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
 
    def paintEvent(self, event):
 
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.QPen(QtGui.QColor(255, 0, 0)))
        painter.drawLine(self.width()/8, self.height()/8, 7*self.width()/8, 7*self.height()/8)
        painter.drawLine(self.width()/8, 7*self.height()/8, 7*self.width()/8, self.height()/8)
        painter.end()