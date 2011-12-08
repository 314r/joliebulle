# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editorG.ui'
#
# Created: Thu Dec  8 21:54:49 2011
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
        Dialog.resize(683, 312)
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Editeur", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Nom</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditNom = QtGui.QLineEdit(self.widget)
        self.lineEditNom.setObjectName(_fromUtf8("lineEditNom"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNom)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Type</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.comboBoxType = QtGui.QComboBox(self.widget)
        self.comboBoxType.setObjectName(_fromUtf8("comboBoxType"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.comboBoxType)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Rendement</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.spinBoxRendmt = QtGui.QSpinBox(self.widget)
        self.spinBoxRendmt.setObjectName(_fromUtf8("spinBoxRendmt"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.spinBoxRendmt)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600;\">Couleur</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.spinBoxCouleur = QtGui.QSpinBox(self.widget)
        self.spinBoxCouleur.setMaximum(9000)
        self.spinBoxCouleur.setObjectName(_fromUtf8("spinBoxCouleur"))
        self.horizontalLayout_2.addWidget(self.spinBoxCouleur)
        self.radioButtonSRM = QtGui.QRadioButton(self.widget)
        self.radioButtonSRM.setText(QtGui.QApplication.translate("Dialog", "SRM", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonSRM.setObjectName(_fromUtf8("radioButtonSRM"))
        self.horizontalLayout_2.addWidget(self.radioButtonSRM)
        self.radioButtonEBC = QtGui.QRadioButton(self.widget)
        self.radioButtonEBC.setText(QtGui.QApplication.translate("Dialog", "EBC", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonEBC.setObjectName(_fromUtf8("radioButtonEBC"))
        self.horizontalLayout_2.addWidget(self.radioButtonEBC)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Empâtage recommandé</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.comboBoxReco = QtGui.QComboBox(self.widget)
        self.comboBoxReco.setObjectName(_fromUtf8("comboBoxReco"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.comboBoxReco)
        self.pushButtonAjouter = QtGui.QPushButton(self.widget)
        self.pushButtonAjouter.setText(QtGui.QApplication.translate("Dialog", "Ajouter", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAjouter.setObjectName(_fromUtf8("pushButtonAjouter"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.pushButtonAjouter)
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)
        self.widget_2 = QtGui.QWidget(Dialog)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.listWidgetGrains = QtGui.QListWidget(self.widget_2)
        self.listWidgetGrains.setObjectName(_fromUtf8("listWidgetGrains"))
        self.gridLayout_2.addWidget(self.listWidgetGrains, 0, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonNouveau = QtGui.QPushButton(self.widget_2)
        self.pushButtonNouveau.setText(QtGui.QApplication.translate("Dialog", "Nouveau", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonNouveau.setObjectName(_fromUtf8("pushButtonNouveau"))
        self.horizontalLayout.addWidget(self.pushButtonNouveau)
        self.pushButtonEnlever = QtGui.QPushButton(self.widget_2)
        self.pushButtonEnlever.setText(QtGui.QApplication.translate("Dialog", "Enlever", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEnlever.setObjectName(_fromUtf8("pushButtonEnlever"))
        self.horizontalLayout.addWidget(self.pushButtonEnlever)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass

