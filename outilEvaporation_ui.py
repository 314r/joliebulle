# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'outilEvaporation.ui'
#
# Created: Thu Apr 21 19:05:01 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogEvaporation(object):
    def setupUi(self, DialogEvaporation):
        DialogEvaporation.setObjectName(_fromUtf8("DialogEvaporation"))
        DialogEvaporation.resize(424, 312)
        self.gridLayout = QtGui.QGridLayout(DialogEvaporation)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(DialogEvaporation)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.doubleSpinBoxPreVol = QtGui.QDoubleSpinBox(DialogEvaporation)
        self.doubleSpinBoxPreVol.setObjectName(_fromUtf8("doubleSpinBoxPreVol"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxPreVol)
        self.label_11 = QtGui.QLabel(DialogEvaporation)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_11)
        self.doubleSpinBoxPreSg = QtGui.QDoubleSpinBox(DialogEvaporation)
        self.doubleSpinBoxPreSg.setDecimals(3)
        self.doubleSpinBoxPreSg.setMinimum(1.0)
        self.doubleSpinBoxPreSg.setMaximum(1.9)
        self.doubleSpinBoxPreSg.setSingleStep(0.001)
        self.doubleSpinBoxPreSg.setProperty(_fromUtf8("value"), 1.06)
        self.doubleSpinBoxPreSg.setObjectName(_fromUtf8("doubleSpinBoxPreSg"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxPreSg)
        self.label_2 = QtGui.QLabel(DialogEvaporation)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.doubleSpinBoxTauxEvap = QtGui.QDoubleSpinBox(DialogEvaporation)
        self.doubleSpinBoxTauxEvap.setProperty(_fromUtf8("value"), 10.0)
        self.doubleSpinBoxTauxEvap.setObjectName(_fromUtf8("doubleSpinBoxTauxEvap"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxTauxEvap)
        self.label_3 = QtGui.QLabel(DialogEvaporation)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spinBoxEbu = QtGui.QSpinBox(DialogEvaporation)
        self.spinBoxEbu.setProperty(_fromUtf8("value"), 60)
        self.spinBoxEbu.setObjectName(_fromUtf8("spinBoxEbu"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.spinBoxEbu)
        self.label_4 = QtGui.QLabel(DialogEvaporation)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.doubleSpinBoxTauxRefroi = QtGui.QDoubleSpinBox(DialogEvaporation)
        self.doubleSpinBoxTauxRefroi.setProperty(_fromUtf8("value"), 5.0)
        self.doubleSpinBoxTauxRefroi.setObjectName(_fromUtf8("doubleSpinBoxTauxRefroi"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxTauxRefroi)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtGui.QFormLayout.LabelRole, spacerItem)
        self.label_5 = QtGui.QLabel(DialogEvaporation)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_5)
        self.labelEvapEbu = QtGui.QLabel(DialogEvaporation)
        self.labelEvapEbu.setObjectName(_fromUtf8("labelEvapEbu"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.labelEvapEbu)
        self.label_7 = QtGui.QLabel(DialogEvaporation)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_7)
        self.labelEvapRefroi = QtGui.QLabel(DialogEvaporation)
        self.labelEvapRefroi.setObjectName(_fromUtf8("labelEvapRefroi"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.labelEvapRefroi)
        self.label_9 = QtGui.QLabel(DialogEvaporation)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_9)
        self.labelVolF = QtGui.QLabel(DialogEvaporation)
        self.labelVolF.setObjectName(_fromUtf8("labelVolF"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.labelVolF)
        self.label_12 = QtGui.QLabel(DialogEvaporation)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_12)
        self.labelSg = QtGui.QLabel(DialogEvaporation)
        self.labelSg.setObjectName(_fromUtf8("labelSg"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.labelSg)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DialogEvaporation)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(DialogEvaporation)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogEvaporation.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogEvaporation.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogEvaporation)

    def retranslateUi(self, DialogEvaporation):
        DialogEvaporation.setWindowTitle(QtGui.QApplication.translate("DialogEvaporation", "Evaporation", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogEvaporation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Volume pré-ébullition (L)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("DialogEvaporation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Densité spécifique pré-ébullition</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogEvaporation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Taux d\'évaporation (%/heure)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogEvaporation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Durée d\'ébullition (min)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogEvaporation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Pertes par refroidissement (%)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogEvaporation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Volume évaporé (ébullition) (L) : </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelEvapEbu.setText(QtGui.QApplication.translate("DialogEvaporation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DialogEvaporation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Volume évaporé (refroidissement) (L) : </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelEvapRefroi.setText(QtGui.QApplication.translate("DialogEvaporation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("DialogEvaporation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Volume final (L) : </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelVolF.setText(QtGui.QApplication.translate("DialogEvaporation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">0</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("DialogEvaporation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Densité spécifique : </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSg.setText(QtGui.QApplication.translate("DialogEvaporation", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">1.060</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

