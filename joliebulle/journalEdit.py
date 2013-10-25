#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.0
#Copyright (C) 2010-2013 Pierre Tavares

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

import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from journalEdit_ui import *

class DialogJournalEdit(QtGui.QDialog):
    journalEdited = QtCore.pyqtSignal(int,str,str,int,int)
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.accepted)

    def setFields(self,date,event,recipe) :
        self.ui.lineEditEvent.setText(event)
        self.ui.lineEditRecipe.setText(recipe)
        self.oldDate = date
        date=QtCore.QDateTime.fromTime_t(date)
        self.ui.dateEdit.setDateTime(date)

    def accepted(self) :
        date = QtCore.QDateTime.toTime_t(self.ui.dateEdit.dateTime())
        event=self.ui.lineEditEvent.text()
        recipe=self.ui.lineEditRecipe.text()
        if not self.oldDate :
            self.oldDate = 0
            delItem = 0
        else :
            delItem = 1
        self.journalEdited.emit(date,event,recipe,self.oldDate,delItem)