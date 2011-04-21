# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'outilDilution.ui'
#
# Created: Thu Apr 21 19:02:45 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogDilution(object):
    def setupUi(self, DialogDilution):
        DialogDilution.setObjectName(_fromUtf8("DialogDilution"))
        DialogDilution.resize(342, 236)
        self.gridLayout = QtGui.QGridLayout(DialogDilution)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(DialogDilution)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.doubleSpinBoxVolInitial = QtGui.QDoubleSpinBox(DialogDilution)
        self.doubleSpinBoxVolInitial.setObjectName(_fromUtf8("doubleSpinBoxVolInitial"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxVolInitial)
        self.label_2 = QtGui.QLabel(DialogDilution)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.doubleSpinBoxDensInitiale = QtGui.QDoubleSpinBox(DialogDilution)
        self.doubleSpinBoxDensInitiale.setDecimals(3)
        self.doubleSpinBoxDensInitiale.setMinimum(1.0)
        self.doubleSpinBoxDensInitiale.setMaximum(1999.0)
        self.doubleSpinBoxDensInitiale.setSingleStep(0.001)
        self.doubleSpinBoxDensInitiale.setObjectName(_fromUtf8("doubleSpinBoxDensInitiale"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxDensInitiale)
        self.label_3 = QtGui.QLabel(DialogDilution)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_3)
        self.doubleSpinBoxVolAjoute = QtGui.QDoubleSpinBox(DialogDilution)
        self.doubleSpinBoxVolAjoute.setObjectName(_fromUtf8("doubleSpinBoxVolAjoute"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxVolAjoute)
        self.label_4 = QtGui.QLabel(DialogDilution)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtGui.QLabel(DialogDilution)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.doubleSpinBoxDensAjout = QtGui.QDoubleSpinBox(DialogDilution)
        self.doubleSpinBoxDensAjout.setDecimals(3)
        self.doubleSpinBoxDensAjout.setMinimum(1.0)
        self.doubleSpinBoxDensAjout.setMaximum(1999.0)
        self.doubleSpinBoxDensAjout.setSingleStep(0.001)
        self.doubleSpinBoxDensAjout.setProperty(_fromUtf8("value"), 1.0)
        self.doubleSpinBoxDensAjout.setObjectName(_fromUtf8("doubleSpinBoxDensAjout"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxDensAjout)
        self.label_6 = QtGui.QLabel(DialogDilution)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtGui.QLabel(DialogDilution)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_7)
        self.labelVolFinal = QtGui.QLabel(DialogDilution)
        self.labelVolFinal.setObjectName(_fromUtf8("labelVolFinal"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.labelVolFinal)
        self.labelDensFinal = QtGui.QLabel(DialogDilution)
        self.labelDensFinal.setObjectName(_fromUtf8("labelDensFinal"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.labelDensFinal)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(2, QtGui.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtGui.QFormLayout.LabelRole, spacerItem1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtGui.QFormLayout.LabelRole, spacerItem2)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DialogDilution)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(DialogDilution)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogDilution.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogDilution.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogDilution)

    def retranslateUi(self, DialogDilution):
        DialogDilution.setWindowTitle(QtGui.QApplication.translate("DialogDilution", "Dilution", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogDilution", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Volume initial (L)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogDilution", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Densité spécifique initiale</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("DialogDilution", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Volume ajouté (L)</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogDilution", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Densité de l\'ajout</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("DialogDilution", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Volume final (L) : </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("DialogDilution", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Densité spécifique finale : </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelVolFinal.setText(QtGui.QApplication.translate("DialogDilution", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">0 </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelDensFinal.setText(QtGui.QApplication.translate("DialogDilution", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">1.000</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

