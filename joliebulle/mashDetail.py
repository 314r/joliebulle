 #!/usr/bin/python3
#­*­coding: utf­8 -­*­

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


import PyQt5
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from base import *

from mashDetail_ui import *

class DialogMashDetail(QtWidgets.QDialog):
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.ui = Ui_DialogMashDetail()
        self.ui.setupUi(self)

    def setFields (self,currentMash) :
    	self.ui.labelMashName.setText('''<p align="center"><b>''' + currentMash.name + '''</b></p>''')
    	self.ui.labelPhValue.setText(str(currentMash.ph))
    	self.ui.labelSpargeValue.setText(str(currentMash.spargeTemp))

        #la liste des paliers
    	for step in currentMash.listeSteps:
    		stepName = step.name
    		stepNameLabelValue = QtGui.QLabel('<b>'+ stepName + '</b> :')
    		stepDetail = QtGui.QLabel(step.type + ", " + str(step.temp) + self.tr("°C, ") + str(step.time) + self.tr(" min"))
    		self.ui.formSteps.addRow(stepNameLabelValue, stepDetail)
