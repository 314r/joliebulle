 #!/usr/bin/python3
#­*­coding: utf­8 -­*­



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
