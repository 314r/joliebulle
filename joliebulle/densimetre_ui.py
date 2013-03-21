# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'densimetre.ui'
#
# Created: Sun Feb 27 23:19:25 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogDensimetre(object):
    def setupUi(self, DialogDensimetre):
        DialogDensimetre.setObjectName(_fromUtf8("DialogDensimetre"))
        DialogDensimetre.resize(250, 178)
        self.gridLayout = QtGui.QGridLayout(DialogDensimetre)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(DialogDensimetre)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(DialogDensimetre)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(DialogDensimetre)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.doubleSpinBoxTempCalib = QtGui.QDoubleSpinBox(DialogDensimetre)
        self.doubleSpinBoxTempCalib.setProperty(_fromUtf8("value"), 20.0)
        self.doubleSpinBoxTempCalib.setObjectName(_fromUtf8("doubleSpinBoxTempCalib"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxTempCalib)
        self.doubleSpinBoxTempEchan = QtGui.QDoubleSpinBox(DialogDensimetre)
        self.doubleSpinBoxTempEchan.setEnabled(True)
        self.doubleSpinBoxTempEchan.setProperty(_fromUtf8("value"), 20.0)
        self.doubleSpinBoxTempEchan.setObjectName(_fromUtf8("doubleSpinBoxTempEchan"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxTempEchan)
        self.doubleSpinBoxDens = QtGui.QDoubleSpinBox(DialogDensimetre)
        self.doubleSpinBoxDens.setSuffix(_fromUtf8(""))
        self.doubleSpinBoxDens.setDecimals(3)
        self.doubleSpinBoxDens.setMinimum(1.0)
        self.doubleSpinBoxDens.setMaximum(1.9)
        self.doubleSpinBoxDens.setSingleStep(0.001)
        self.doubleSpinBoxDens.setObjectName(_fromUtf8("doubleSpinBoxDens"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxDens)
        self.label_4 = QtGui.QLabel(DialogDensimetre)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.labelDensCorr = QtGui.QLabel(DialogDensimetre)
        self.labelDensCorr.setObjectName(_fromUtf8("labelDensCorr"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.labelDensCorr)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtGui.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(6, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DialogDensimetre)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(DialogDensimetre)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogDensimetre.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogDensimetre.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogDensimetre)

    def retranslateUi(self, DialogDensimetre):
        DialogDensimetre.setWindowTitle(QtGui.QApplication.translate("DialogDensimetre", "Densimetre", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogDensimetre", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Densité mesurée</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogDensimetre", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Température calibration</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogDensimetre", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Température échantillon</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.doubleSpinBoxTempCalib.setSuffix(QtGui.QApplication.translate("DialogDensimetre", "°C", None, QtGui.QApplication.UnicodeUTF8))
        self.doubleSpinBoxTempEchan.setSuffix(QtGui.QApplication.translate("DialogDensimetre", "°C", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogDensimetre", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Densité corrigée :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDensCorr.setText(QtGui.QApplication.translate("DialogDensimetre", "1.000", None, QtGui.QApplication.UnicodeUTF8))

