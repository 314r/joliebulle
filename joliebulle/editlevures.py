#!/usr/bin/python3
#­*­coding: utf­8 -­*­




import PyQt5
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from base import *
from globals import *
import view.base


from editorY_ui import *
import xml.etree.ElementTree as ET
from xml.dom import minidom


class DialogL(QtWidgets.QDialog):
    baseChanged = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.base = ImportBase()
        #self.base.importBeerXML()

        self.ui.listViewLevures.setModel( view.base.getYeastsQtModel() )
        self.ui.comboBoxForme.addItem(self.tr('Liquide'))
        self.ui.comboBoxForme.addItem(self.tr('Poudre'))
        self.ui.comboBoxForme.addItem(self.tr('Gélose'))
        self.ui.comboBoxForme.addItem(self.tr('Culture'))

        self.ui.listViewLevures.selectionModel().currentChanged.connect(self.voir)
        self.ui.pushButtonNouveau.clicked.connect(self.nouveau)
        self.ui.pushButtonEnlever.clicked.connect(self.enlever)
        self.ui.pushButtonAjouter.clicked.connect(self.ajouter)
        self.ui.buttonBox.rejected.connect(self.rejected)

        self.ui.lineEditNom.setEnabled(False)
        self.ui.comboBoxForme.setEnabled(False)
        self.ui.lineEditLabo.setEnabled(False)
        self.ui.lineEditID.setEnabled(False)
        self.ui.spinBoxAtten.setEnabled(False)
        self.ui.pushButtonAjouter.setEnabled(False)

    def setModel(self) :
        self.ui.listViewLevures.setModel( view.base.getYeastsQtModel() )
        self.ui.listViewLevures.selectionModel().currentChanged.connect(self.voir)

    def voir(self, current, previous) :
        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxForme.setEnabled(True)
        self.ui.lineEditLabo.setEnabled(True)
        self.ui.lineEditID.setEnabled(True)
        self.ui.spinBoxAtten.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)

        y = current.data(view.constants.MODEL_DATA_ROLE)

        self.ui.lineEditNom.setText(y.name)
        self.ui.lineEditLabo.setText(y.labo)
        self.ui.lineEditID.setText(y.productId)
        self.ui.spinBoxAtten.setValue(y.attenuation)

        if y.form == 'Liquid' :
            self.ui.comboBoxForme.setCurrentIndex(0)
        elif y.form == 'Dry' :
            self.ui.comboBoxForme.setCurrentIndex(1)
        elif y.form == 'Slant' :
            self.ui.comboBoxForme.setCurrentIndex(2)
        elif y.form == 'Culture' :
            self.ui.comboBoxForme.setCurrentIndex(3)
        else :
            self.ui.comboBoxForme.setCurrentIndex(0)

    def ajouter(self) :
        y = Yeast()
        y.name = self.ui.lineEditNom.text()
        y.labo = self.ui.lineEditLabo.text()
        y.productId = self.ui.lineEditID.text()
        y.attenuation = self.ui.spinBoxAtten.value()

        if self.ui.comboBoxForme.currentIndex() is 0 :
            y.form =  'Liquid'
        elif self.ui.comboBoxForme.currentIndex() is 1 :
            y.form = 'Dry'
        elif self.ui.comboBoxForme.currentIndex() is 2 :
            y.form = 'Slant'
        elif self.ui.comboBoxForme.currentIndex() is 3 :
            y.form = 'Culture'
        else :
            y.form = 'Dry'

        ImportBase.addYeast(y)
        self.setModel()

    def nouveau(self) :
        self.ui.lineEditNom.setEnabled(True)
        self.ui.comboBoxForme.setEnabled(True)
        self.ui.lineEditLabo.setEnabled(True)
        self.ui.lineEditID.setEnabled(True)
        self.ui.spinBoxAtten.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)

        self.ui.lineEditNom.setText('')
        self.ui.lineEditLabo.setText('')
        self.ui.lineEditID.setText('')
        self.ui.comboBoxForme.setCurrentIndex(0)
        self.ui.spinBoxAtten.setValue(0)

    def enlever(self) :
        selection = self.ui.listViewLevures.selectionModel().selectedIndexes()
        for index in selection :
            y = index.data(view.constants.MODEL_DATA_ROLE)
            ImportBase().delYeast(y)
        self.setModel()

    def rejected(self) :
        self.baseChanged.emit()
