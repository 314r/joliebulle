# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'outilAlc.ui'
#
# Created: Fri Jan  4 15:56:16 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DialogAlc(object):
    def setupUi(self, DialogAlc):
        DialogAlc.setObjectName(_fromUtf8("DialogAlc"))
        DialogAlc.resize(270, 219)
        self.gridLayout = QtGui.QGridLayout(DialogAlc)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(DialogAlc)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(DialogAlc)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(DialogAlc)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.labelAlc = QtGui.QLabel(DialogAlc)
        self.labelAlc.setObjectName(_fromUtf8("labelAlc"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.labelAlc)
        self.doubleSpinBoxDI = QtGui.QDoubleSpinBox(DialogAlc)
        self.doubleSpinBoxDI.setDecimals(3)
        self.doubleSpinBoxDI.setMinimum(1.0)
        self.doubleSpinBoxDI.setMaximum(1.9)
        self.doubleSpinBoxDI.setSingleStep(0.001)
        self.doubleSpinBoxDI.setObjectName(_fromUtf8("doubleSpinBoxDI"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxDI)
        self.doubleSpinBoxDF = QtGui.QDoubleSpinBox(DialogAlc)
        self.doubleSpinBoxDF.setDecimals(3)
        self.doubleSpinBoxDF.setMinimum(1.0)
        self.doubleSpinBoxDF.setMaximum(1.9)
        self.doubleSpinBoxDF.setSingleStep(0.001)
        self.doubleSpinBoxDF.setObjectName(_fromUtf8("doubleSpinBoxDF"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxDF)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtGui.QFormLayout.LabelRole, spacerItem)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.label_4 = QtGui.QLabel(DialogAlc)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.doubleSpinBoxSucre = QtGui.QDoubleSpinBox(DialogAlc)
        self.doubleSpinBoxSucre.setSingleStep(0.1)
        self.doubleSpinBoxSucre.setProperty("value", 7.0)
        self.doubleSpinBoxSucre.setObjectName(_fromUtf8("doubleSpinBoxSucre"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.doubleSpinBoxSucre)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DialogAlc)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(DialogAlc)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogAlc.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogAlc.reject)
        QtCore.QMetaObject.connectSlotsByName(DialogAlc)

    def retranslateUi(self, DialogAlc):
        DialogAlc.setWindowTitle(_translate("DialogAlc", "Calcul taux alcool", None))
        self.label.setText(_translate("DialogAlc", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Densité initiale</span></p></body></html>", None))
        self.label_2.setText(_translate("DialogAlc", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Densité finale</span></p></body></html>", None))
        self.label_3.setText(_translate("DialogAlc", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Alcool par volume (%) :</span></p></body></html>", None))
        self.labelAlc.setText(_translate("DialogAlc", "0", None))
        self.label_4.setText(_translate("DialogAlc", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Sucre ajouté (g/L)</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DialogAlc = QtGui.QDialog()
    ui = Ui_DialogAlc()
    ui.setupUi(DialogAlc)
    DialogAlc.show()
    sys.exit(app.exec_())

