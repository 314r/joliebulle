# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mashDetail.ui'
#
# Created: Thu Dec 13 19:10:26 2012
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogMashDetail(object):
    def setupUi(self, DialogMashDetail):
        DialogMashDetail.setObjectName(_fromUtf8("DialogMashDetail"))
        DialogMashDetail.resize(361, 281)
        self.gridLayout = QtGui.QGridLayout(DialogMashDetail)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.labelMashName = QtGui.QLabel(DialogMashDetail)
        self.labelMashName.setMargin(20)
        self.labelMashName.setObjectName(_fromUtf8("labelMashName"))
        self.verticalLayout.addWidget(self.labelMashName)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.labelPhValue = QtGui.QLabel(DialogMashDetail)
        self.labelPhValue.setObjectName(_fromUtf8("labelPhValue"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.labelPhValue)
        self.labelSparge = QtGui.QLabel(DialogMashDetail)
        self.labelSparge.setObjectName(_fromUtf8("labelSparge"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelSparge)
        self.labelSpargeValue = QtGui.QLabel(DialogMashDetail)
        self.labelSpargeValue.setObjectName(_fromUtf8("labelSpargeValue"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.labelSpargeValue)
        self.labelPh = QtGui.QLabel(DialogMashDetail)
        self.labelPh.setObjectName(_fromUtf8("labelPh"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelPh)
        self.verticalLayout.addLayout(self.formLayout)
        self.label = QtGui.QLabel(DialogMashDetail)
        self.label.setMargin(20)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.formSteps = QtGui.QFormLayout()
        self.formSteps.setObjectName(_fromUtf8("formSteps"))
        self.verticalLayout.addLayout(self.formSteps)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DialogMashDetail)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(DialogMashDetail)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogMashDetail.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogMashDetail.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogMashDetail)

    def retranslateUi(self, DialogMashDetail):
        DialogMashDetail.setWindowTitle(QtGui.QApplication.translate("DialogMashDetail", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMashName.setText(QtGui.QApplication.translate("DialogMashDetail", "<html><head/><body><p align=\"center\">Profil</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPhValue.setText(QtGui.QApplication.translate("DialogMashDetail", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSparge.setText(QtGui.QApplication.translate("DialogMashDetail", "<html><head/><body><p><span style=\" font-weight:600;\">Rinçage :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSpargeValue.setText(QtGui.QApplication.translate("DialogMashDetail", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPh.setText(QtGui.QApplication.translate("DialogMashDetail", "<html><head/><body><p><span style=\" font-weight:600;\">Ph : </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogMashDetail", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Etapes</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

