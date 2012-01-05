# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mashEditor.ui'
#
# Created: Thu Jan  5 18:47:06 2012
#      by: PyQt4 UI code generator 4.9
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogMash(object):
    def setupUi(self, DialogMash):
        DialogMash.setObjectName(_fromUtf8("DialogMash"))
        DialogMash.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(DialogMash)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(DialogMash)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditName = QtGui.QLineEdit(DialogMash)
        self.lineEditName.setObjectName(_fromUtf8("lineEditName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditName)
        self.label_2 = QtGui.QLabel(DialogMash)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(DialogMash)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(DialogMash)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(DialogMash)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.doubleSpinBoxPh = QtGui.QDoubleSpinBox(DialogMash)
        self.doubleSpinBoxPh.setObjectName(_fromUtf8("doubleSpinBoxPh"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxPh)
        self.doubleSpinBoxGrainT = QtGui.QDoubleSpinBox(DialogMash)
        self.doubleSpinBoxGrainT.setObjectName(_fromUtf8("doubleSpinBoxGrainT"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxGrainT)
        self.doubleSpinBoxTunT = QtGui.QDoubleSpinBox(DialogMash)
        self.doubleSpinBoxTunT.setObjectName(_fromUtf8("doubleSpinBoxTunT"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxTunT)
        self.doubleSpinBoxSpargeT = QtGui.QDoubleSpinBox(DialogMash)
        self.doubleSpinBoxSpargeT.setObjectName(_fromUtf8("doubleSpinBoxSpargeT"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxSpargeT)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DialogMash)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(DialogMash)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogMash.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogMash.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogMash)

    def retranslateUi(self, DialogMash):
        DialogMash.setWindowTitle(QtGui.QApplication.translate("DialogMash", "Editeur de profils de brassage", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogMash", "<html><head/><body><p><span style=\" font-weight:600;\">Nom :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogMash", "<html><head/><body><p><span style=\" font-weight:600;\">pH :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogMash", "<html><head/><body><p><span style=\" font-weight:600;\">Température grain :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogMash", "<html><head/><body><p><span style=\" font-weight:600;\">Température cuve : </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogMash", "<html><head/><body><p><span style=\" font-weight:600;\">Température rinçage :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

