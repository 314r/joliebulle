# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'outilPaliers.ui'
#
# Created: Fri May 13 09:12:54 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogPaliers(object):
    def setupUi(self, DialogPaliers):
        DialogPaliers.setObjectName(_fromUtf8("DialogPaliers"))
        DialogPaliers.resize(400, 316)
        self.gridLayout = QtGui.QGridLayout(DialogPaliers)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(DialogPaliers)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(DialogPaliers)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(DialogPaliers)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(DialogPaliers)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(DialogPaliers)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(DialogPaliers)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(DialogPaliers)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.label_6)
        self.doubleSpinBoxTargetTemp = QtGui.QDoubleSpinBox(DialogPaliers)
        self.doubleSpinBoxTargetTemp.setProperty(_fromUtf8("value"), 68.0)
        self.doubleSpinBoxTargetTemp.setObjectName(_fromUtf8("doubleSpinBoxTargetTemp"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxTargetTemp)
        self.doubleSpinBoxAddedVolume = QtGui.QDoubleSpinBox(DialogPaliers)
        self.doubleSpinBoxAddedVolume.setProperty(_fromUtf8("value"), 10.0)
        self.doubleSpinBoxAddedVolume.setObjectName(_fromUtf8("doubleSpinBoxAddedVolume"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxAddedVolume)
        self.doubleSpinBoxGrainW = QtGui.QDoubleSpinBox(DialogPaliers)
        self.doubleSpinBoxGrainW.setProperty(_fromUtf8("value"), 4.0)
        self.doubleSpinBoxGrainW.setObjectName(_fromUtf8("doubleSpinBoxGrainW"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxGrainW)
        self.doubleSpinBoxGrainT = QtGui.QDoubleSpinBox(DialogPaliers)
        self.doubleSpinBoxGrainT.setProperty(_fromUtf8("value"), 20.0)
        self.doubleSpinBoxGrainT.setObjectName(_fromUtf8("doubleSpinBoxGrainT"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxGrainT)
        self.labelTempWater = QtGui.QLabel(DialogPaliers)
        self.labelTempWater.setObjectName(_fromUtf8("labelTempWater"))
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.labelTempWater)
        self.labelRatio = QtGui.QLabel(DialogPaliers)
        self.labelRatio.setObjectName(_fromUtf8("labelRatio"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.labelRatio)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(9, QtGui.QFormLayout.FieldRole, spacerItem)
        self.label_7 = QtGui.QLabel(DialogPaliers)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_7)
        self.doubleSpinBoxFudgeFactor = QtGui.QDoubleSpinBox(DialogPaliers)
        self.doubleSpinBoxFudgeFactor.setProperty(_fromUtf8("value"), 1.7)
        self.doubleSpinBoxFudgeFactor.setObjectName(_fromUtf8("doubleSpinBoxFudgeFactor"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxFudgeFactor)
        self.label_8 = QtGui.QLabel(DialogPaliers)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_8)
        self.comboBoxPaliers = QtGui.QComboBox(DialogPaliers)
        self.comboBoxPaliers.setObjectName(_fromUtf8("comboBoxPaliers"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBoxPaliers)
        self.doubleSpinBoxMashTemp = QtGui.QDoubleSpinBox(DialogPaliers)
        self.doubleSpinBoxMashTemp.setObjectName(_fromUtf8("doubleSpinBoxMashTemp"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxMashTemp)
        self.label_9 = QtGui.QLabel(DialogPaliers)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_9)
        self.doubleSpinBoxStartWater = QtGui.QDoubleSpinBox(DialogPaliers)
        self.doubleSpinBoxStartWater.setObjectName(_fromUtf8("doubleSpinBoxStartWater"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxStartWater)
        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)

        self.retranslateUi(DialogPaliers)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogPaliers.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogPaliers.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogPaliers)

    def retranslateUi(self, DialogPaliers):
        DialogPaliers.setWindowTitle(QtGui.QApplication.translate("DialogPaliers", "Assistant paliers", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogPaliers", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Température cible (°C)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogPaliers", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Volume ajouté (L)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogPaliers", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Poids du grain (Kg)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("DialogPaliers", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Température initiale du grain (°C)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogPaliers", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Température eau (°C) : </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DialogPaliers", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Ratio eau/grain (L/Kg) : </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTempWater.setText(QtGui.QApplication.translate("DialogPaliers", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRatio.setText(QtGui.QApplication.translate("DialogPaliers", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DialogPaliers", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Facteur de correction </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("DialogPaliers", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Température de la maîche (°C)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("DialogPaliers", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Volume d\'eau dans la maîche (L)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

