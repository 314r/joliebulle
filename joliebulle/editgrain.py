#!/usr/bin/python3
#­*­coding: utf­8 -­*­




import codecs
import PyQt5
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from base import *
from globals import *
import view.base
import model.constants

from editorG_ui import *

logger = logging.getLogger(__name__)

class Dialog(QtWidgets.QDialog):
    baseChanged = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.base = ImportBase()
        logger.debug("init Dialog")

        #self.ui.listWidgetGrains.addItems(self.base.listeFermentables)
        self.ui.listViewGrains.setModel(view.base.getFermentablesQtModel())
        self.ui.comboBoxType.addItem(self.tr('Grain'))
        self.ui.comboBoxType.addItem(self.tr('Extrait'))
        self.ui.comboBoxType.addItem(self.tr('Extrait sec'))
        self.ui.comboBoxType.addItem(self.tr('Sucre'))
        self.ui.comboBoxType.addItem(self.tr("Complément"))
        self.ui.comboBoxReco.addItem(self.tr('Oui'))
        self.ui.comboBoxReco.addItem(self.tr('Non'))

        self.ui.spinBoxCouleur.setMaximum(10000)
        self.ui.spinBoxRendmt.setMaximum(1000)

        self.ui.listViewGrains.selectionModel().currentChanged.connect(self.voir)
        self.ui.pushButtonNouveau.clicked.connect(self.nouveau)
        self.ui.pushButtonEnlever.clicked.connect(self.enlever)
        self.ui.pushButtonAjouter.clicked.connect(self.ajouter)
        self.ui.radioButtonEBC.toggled.connect(self.toggleUnits)
        self.ui.buttonBox.rejected.connect(self.rejected)


        self.ui.lineEditNom.setEnabled(False)
        self.ui.comboBoxType.setEnabled(False)
        self.ui.spinBoxRendmt.setEnabled(False)
        self.ui.comboBoxReco.setEnabled(False)
        self.ui.spinBoxCouleur.setEnabled(False)
        self.ui.pushButtonAjouter.setEnabled(False)
        self.ui.pushButtonAjouter.setEnabled(False)
        self.ui.radioButtonSRM.setEnabled(False)
        self.ui.radioButtonEBC.setEnabled(False)

    def setModel(self) :
        self.ui.listViewGrains.setModel(view.base.getFermentablesQtModel())
        self.ui.listViewGrains.selectionModel().currentChanged.connect(self.voir)

    def voir (self, current, previous) :

        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxType.setEnabled(True)
        self.ui.spinBoxRendmt.setEnabled(True)
        self.ui.comboBoxReco.setEnabled(True)
        self.ui.spinBoxCouleur.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)
        self.ui.radioButtonSRM.setEnabled(True)
        self.ui.radioButtonEBC.setEnabled(True)
        self.ui.radioButtonSRM.setChecked(True)

        f = current.data(view.constants.MODEL_DATA_ROLE)
        self.ui.lineEditNom.setText(f.name)
        self.ui.spinBoxRendmt.setValue(f.fyield)
        self.ui.spinBoxCouleur.setValue(f.color/1.97)

        if model.constants.FERMENTABLE_TYPE_GRAIN == f.type :
            self.ui.comboBoxType.setCurrentIndex(0)
        elif model.constants.FERMENTABLE_TYPE_EXTRACT == f.type :
            self.ui.comboBoxType.setCurrentIndex(1)
        elif model.constants.FERMENTABLE_TYPE_DRY_EXTRACT == f.type :
            self.ui.comboBoxType.setCurrentIndex(2)
        elif model.constants.FERMENTABLE_TYPE_SUGAR == f.type :
            self.ui.comboBoxType.setCurrentIndex(3)
        elif model.constants.FERMENTABLE_TYPE_ADJUNCT == f.type :
            self.ui.comboBoxType.setCurrentIndex(4)
        else :
            self.ui.comboBoxType.setCurrentIndex(0)

        if f.useAfterBoil == False :
            self.ui.comboBoxReco.setCurrentIndex(0)
        else :
            self.ui.comboBoxReco.setCurrentIndex(1)

    def toggleUnits (self) :

        if self.ui.radioButtonEBC.isChecked() :
            self.ui.spinBoxCouleur.setValue(round(self.ui.spinBoxCouleur.value()*1.97,1))
        else :
            self.ui.spinBoxCouleur.setValue(round(self.ui.spinBoxCouleur.value()/1.97,1))

    def ajouter (self) :
        #Attention aux unités. Dans la base xml la couleur est en srm, dans la liste de la base la couleur est convertie en EBC
        f = Fermentable()
        f.name = self.ui.lineEditNom.text()
        f.fyield = self.ui.spinBoxRendmt.value()
        self.ui.radioButtonSRM.setChecked(True)
        f.color = self.ui.spinBoxCouleur.value()*1.97

        if self.ui.comboBoxType.currentIndex() is 0 :
            f.type = model.constants.FERMENTABLE_TYPE_GRAIN
        elif self.ui.comboBoxType.currentIndex() is 1 :
            f.type = model.constants.FERMENTABLE_TYPE_EXTRACT
        elif self.ui.comboBoxType.currentIndex() is 2 :
            f.type = model.constants.FERMENTABLE_TYPE_DRY_EXTRACT
        elif self.ui.comboBoxType.currentIndex() is 3 :
            f.type = model.constants.FERMENTABLE_TYPE_SUGAR
        elif self.ui.comboBoxType.currentIndex() is 4 :
            f.type = model.constants.FERMENTABLE_TYPE_ADJUNCT

        if self.ui.comboBoxReco.currentIndex() is 0 :
            f.useAfterBoil = False
        else :
            f.useAfterBoil = True
        ImportBase.addFermentable(f)
        self.setModel()

    def nouveau (self) :
        logger.debug("nouveau")
        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxType.setEnabled(True)
        self.ui.spinBoxRendmt.setEnabled(True)
        self.ui.comboBoxReco.setEnabled(True)
        self.ui.spinBoxCouleur.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)
        self.ui.radioButtonSRM.setEnabled(True)
        self.ui.radioButtonEBC.setEnabled(True)
        self.ui.radioButtonSRM.setChecked(True)

        self.ui.lineEditNom.setText('')
        self.ui.spinBoxCouleur.setValue(0)
        self.ui.spinBoxRendmt.setValue(0)
        self.ui.comboBoxReco.setCurrentIndex(0)
        self.ui.comboBoxType.setCurrentIndex(0)

    def enlever (self) :
        selection = self.ui.listViewGrains.selectionModel().selectedIndexes()
        for index in selection :
            f = index.data(view.constants.MODEL_DATA_ROLE)
        ImportBase().delFermentable(f)
        self.setModel()


    def rejected(self) :
        #self.emit( QtCore.SIGNAL( "baseChanged"))
        self.baseChanged.emit()
