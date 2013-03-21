#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#JolieBulle 2.8
#Copyright (C) 2010-2013 Pierre Tavares
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.



import codecs
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from mashEditor_ui import *
from model.mash import *

class DialogMash(QtGui.QDialog):
    mashChanged = QtCore.pyqtSignal(Mash)
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self,parent)
        self.ui = Ui_DialogMash()
        self.ui.setupUi(self)
        self.ui.lineEditName.textChanged.connect(self.valueChanged)
        self.ui.doubleSpinBoxPh.valueChanged.connect(self.valueChanged)
#        self.ui.doubleSpinBoxGrainT.valueChanged.connect(self.valueChanged)
#        self.ui.doubleSpinBoxTunT.valueChanged.connect(self.valueChanged)
        self.ui.doubleSpinBoxSpargeT.valueChanged.connect(self.valueChanged)
        
        self.ui.buttonBox.accepted.connect(self.accepted)
        
    def fields(self,mash) :
        self.ui.lineEditName.setText(mash.name)
        self.ui.doubleSpinBoxPh.setValue(float(mash.ph))
#        self.ui.doubleSpinBoxGrainT.setValue(float(grainT))
#        self.ui.doubleSpinBoxTunT.setValue(float(tunT))
        self.ui.doubleSpinBoxSpargeT.setValue(float(mash.spargeTemp))
        
    def valueChanged(self) :
        self.mash = Mash()
        self.mash.name = self.ui.lineEditName.text()
        self.mash.ph = self.ui.doubleSpinBoxPh.value()
        self.mash.grainTemp = 0
        self.mash.tunTemp = 0
        self.mash.spargeTemp =self.ui.doubleSpinBoxSpargeT.value()
        
    def accepted(self) :
        self.mashChanged.emit(self.mash)
        
        
