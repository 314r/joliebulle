#!/usr/bin/python3
#­*­coding: utf­8 -­*­




import PyQt5
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from base import *
from globals import *
import view.base

from editorH_ui import *
import xml.etree.ElementTree as ET
from xml.dom import minidom
import model.constants


class DialogH(QtWidgets.QDialog):
    baseChanged = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        QtWidgets.QDialog.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.base = ImportBase()
        #self.base.importBeerXML()

        self.ui.listViewHoublons.setModel( view.base.getHopsQtModel() )
        self.ui.comboBoxForme.addItem(self.tr('Feuille'))
        self.ui.comboBoxForme.addItem(self.tr('Pellet'))
        self.ui.comboBoxForme.addItem(self.tr('Cône'))

        self.ui.listViewHoublons.selectionModel().currentChanged.connect(self.voir)
        self.ui.pushButtonNouveau.clicked.connect(self.nouveau)
        self.ui.pushButtonEnlever.clicked.connect(self.enlever)
        self.ui.pushButtonAjouter.clicked.connect(self.ajouter)
        self.ui.buttonBox.rejected.connect(self.rejected)

        self.ui.lineEditNom.setEnabled(False)
        self.ui.spinBoxAlpha.setEnabled(False)
        self.ui.comboBoxForme.setEnabled(False)
        self.ui.pushButtonAjouter.setEnabled(False)


    def setModel(self):
        self.ui.listViewHoublons.setModel( view.base.getHopsQtModel() )
        self.ui.listViewHoublons.selectionModel().currentChanged.connect(self.voir)

    def voir(self, current, previous) :

        self.ui.lineEditNom.setEnabled(True)
        self.ui.spinBoxAlpha.setEnabled(True)
        self.ui.comboBoxForme.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)

        h = current.data(view.constants.MODEL_DATA_ROLE)

        self.ui.lineEditNom.setText(h.name)
        self.ui.spinBoxAlpha.setValue(h.alpha)

        if model.constants.HOP_FORM_LEAF == h.form :
            self.ui.comboBoxForme.setCurrentIndex(0)
        elif model.constants.HOP_FORM_PELLET == h.form :
            self.ui.comboBoxForme.setCurrentIndex(1)
        elif model.constants.HOP_FORM_PLUG == h.form  :
            self.ui.comboBoxForme.setCurrentIndex(2)
        else :
            self.ui.comboBoxForme.setCurrentIndex(0)

    def ajouter(self) :
        h = Hop()
        h.name = self.ui.lineEditNom.text()
        h.alpha = self.ui.spinBoxAlpha.value()
        if self.ui.comboBoxForme.currentIndex() is 0 :
            h.form = model.constants.HOP_FORM_LEAF
        elif self.ui.comboBoxForme.currentIndex() is 1 :
            h.form = model.constants.HOP_FORM_PELLET
        elif self.ui.comboBoxForme.currentIndex() is 2 :
            h.form = model.constants.HOP_FORM_PLUG
        else :
            h.form = model.constants.HOP_FORM_LEAF
        ImportBase.addHop(h)
        self.setModel()


    def nouveau(self) :
        self.ui.lineEditNom.setEnabled(True)
        self.ui.spinBoxAlpha.setEnabled(True)
        self.ui.comboBoxForme.setEnabled(True)
        self.ui.pushButtonAjouter.setEnabled(True)

        self.ui.lineEditNom.setText('')
        self.ui.spinBoxAlpha.setValue(0)
        self.ui.comboBoxForme.setCurrentIndex(2)

    def enlever(self) :
        selection = self.ui.listViewHoublons.selectionModel().selectedIndexes()
        for index in selection :
            h = index.data(view.constants.MODEL_DATA_ROLE)
        ImportBase().delHop(h)
        self.setModel()

    def rejected(self) :
        self.baseChanged.emit()
