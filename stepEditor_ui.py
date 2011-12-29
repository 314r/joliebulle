# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stepEditor.ui'
#
# Created: Wed Dec 21 15:56:55 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(499, 317)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Editeur de paliers", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Nom :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_9)
        self.lineEditStepName = QtGui.QLineEdit(Dialog)
        self.lineEditStepName.setObjectName(_fromUtf8("lineEditStepName"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditStepName)
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Type :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_10)
        self.comboBoxStepType = QtGui.QComboBox(Dialog)
        self.comboBoxStepType.setObjectName(_fromUtf8("comboBoxStepType"))
        self.formLayout_6.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBoxStepType)
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Durée :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_11)
        self.doubleSpinBoxStepTime = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxStepTime.setSuffix(QtGui.QApplication.translate("Dialog", " min", None, QtGui.QApplication.UnicodeUTF8))
        self.doubleSpinBoxStepTime.setObjectName(_fromUtf8("doubleSpinBoxStepTime"))
        self.formLayout_6.setWidget(2, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxStepTime)
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Température :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_6.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_12)
        self.doubleSpinBoxStepTemp = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxStepTemp.setSuffix(QtGui.QApplication.translate("Dialog", " °C", None, QtGui.QApplication.UnicodeUTF8))
        self.doubleSpinBoxStepTemp.setObjectName(_fromUtf8("doubleSpinBoxStepTemp"))
        self.formLayout_6.setWidget(3, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxStepTemp)
        self.label_13 = QtGui.QLabel(Dialog)
        self.label_13.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Volume :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_6.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_13)
        self.doubleSpinBoxStepVol = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBoxStepVol.setSuffix(QtGui.QApplication.translate("Dialog", " L", None, QtGui.QApplication.UnicodeUTF8))
        self.doubleSpinBoxStepVol.setObjectName(_fromUtf8("doubleSpinBoxStepVol"))
        self.formLayout_6.setWidget(4, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxStepVol)
        self.gridLayout.addLayout(self.formLayout_6, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass

