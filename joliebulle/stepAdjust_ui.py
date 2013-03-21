# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stepAdjust.ui'
#
# Created: Tue Feb 14 22:00:12 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogStepBrewday(object):
    def setupUi(self, DialogStepBrewday):
        DialogStepBrewday.setObjectName(_fromUtf8("DialogStepBrewday"))
        DialogStepBrewday.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(DialogStepBrewday)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(DialogStepBrewday)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.labelTargetTemp = QtGui.QLabel(DialogStepBrewday)
        self.labelTargetTemp.setObjectName(_fromUtf8("labelTargetTemp"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.labelTargetTemp)
        self.label_2 = QtGui.QLabel(DialogStepBrewday)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(DialogStepBrewday)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(DialogStepBrewday)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.doubleSpinBoxTargetRatio = QtGui.QDoubleSpinBox(DialogStepBrewday)
        self.doubleSpinBoxTargetRatio.setEnabled(False)
        self.doubleSpinBoxTargetRatio.setObjectName(_fromUtf8("doubleSpinBoxTargetRatio"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxTargetRatio)
        self.doubleSpinBoxInfuseAmount = QtGui.QDoubleSpinBox(DialogStepBrewday)
        self.doubleSpinBoxInfuseAmount.setObjectName(_fromUtf8("doubleSpinBoxInfuseAmount"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxInfuseAmount)
        self.doubleSpinBoxWaterTemp = QtGui.QDoubleSpinBox(DialogStepBrewday)
        self.doubleSpinBoxWaterTemp.setObjectName(_fromUtf8("doubleSpinBoxWaterTemp"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxWaterTemp)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DialogStepBrewday)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(DialogStepBrewday)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogStepBrewday.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogStepBrewday.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogStepBrewday)

    def retranslateUi(self, DialogStepBrewday):
        DialogStepBrewday.setWindowTitle(QtGui.QApplication.translate("DialogStepBrewday", "Ajuster le brassage", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogStepBrewday", "Température cible :", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTargetTemp.setText(QtGui.QApplication.translate("DialogStepBrewday", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogStepBrewday", "Ratio cible :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogStepBrewday", "Volume ajouté :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogStepBrewday", "Température de l\'ajout :", None, QtGui.QApplication.UnicodeUTF8))

