# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reader.ui'
#
# Created: Sat Jan  1 17:39:36 2011
#      by: PyQt4 UI code generator 4.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1143, 583)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/bulle.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelRecette = QtGui.QLabel(self.centralwidget)
        self.labelRecette.setObjectName(_fromUtf8("labelRecette"))
        self.horizontalLayout.addWidget(self.labelRecette)
        self.labelRecetteV = QtGui.QLabel(self.centralwidget)
        self.labelRecetteV.setText(_fromUtf8(""))
        self.labelRecetteV.setObjectName(_fromUtf8("labelRecetteV"))
        self.horizontalLayout.addWidget(self.labelRecetteV)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelGenre = QtGui.QLabel(self.centralwidget)
        self.labelGenre.setObjectName(_fromUtf8("labelGenre"))
        self.horizontalLayout_2.addWidget(self.labelGenre)
        self.labelGenreV = QtGui.QLabel(self.centralwidget)
        self.labelGenreV.setText(_fromUtf8(""))
        self.labelGenreV.setObjectName(_fromUtf8("labelGenreV"))
        self.horizontalLayout_2.addWidget(self.labelGenreV)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_2Volume = QtGui.QLabel(self.centralwidget)
        self.label_2Volume.setObjectName(_fromUtf8("label_2Volume"))
        self.horizontalLayout_4.addWidget(self.label_2Volume)
        self.doubleSpinBox_2Volume = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox_2Volume.setObjectName(_fromUtf8("doubleSpinBox_2Volume"))
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_2Volume)
        self.labelBoil = QtGui.QLabel(self.centralwidget)
        self.labelBoil.setObjectName(_fromUtf8("labelBoil"))
        self.horizontalLayout_4.addWidget(self.labelBoil)
        self.spinBoxBoil = QtGui.QSpinBox(self.centralwidget)
        self.spinBoxBoil.setObjectName(_fromUtf8("spinBoxBoil"))
        self.horizontalLayout_4.addWidget(self.spinBoxBoil)
        self.labelRendement = QtGui.QLabel(self.centralwidget)
        self.labelRendement.setObjectName(_fromUtf8("labelRendement"))
        self.horizontalLayout_4.addWidget(self.labelRendement)
        self.doubleSpinBoxRendemt = QtGui.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBoxRendemt.setObjectName(_fromUtf8("doubleSpinBoxRendemt"))
        self.horizontalLayout_4.addWidget(self.doubleSpinBoxRendemt)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelOG = QtGui.QLabel(self.centralwidget)
        self.labelOG.setObjectName(_fromUtf8("labelOG"))
        self.horizontalLayout_3.addWidget(self.labelOG)
        self.labelOGV = QtGui.QLabel(self.centralwidget)
        self.labelOGV.setText(_fromUtf8(""))
        self.labelOGV.setObjectName(_fromUtf8("labelOGV"))
        self.horizontalLayout_3.addWidget(self.labelOGV)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout_3.addWidget(self.line)
        self.labelFG = QtGui.QLabel(self.centralwidget)
        self.labelFG.setObjectName(_fromUtf8("labelFG"))
        self.horizontalLayout_3.addWidget(self.labelFG)
        self.labelFGV = QtGui.QLabel(self.centralwidget)
        self.labelFGV.setText(_fromUtf8(""))
        self.labelFGV.setObjectName(_fromUtf8("labelFGV"))
        self.horizontalLayout_3.addWidget(self.labelFGV)
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_3.addWidget(self.line_2)
        self.labelEBC = QtGui.QLabel(self.centralwidget)
        self.labelEBC.setObjectName(_fromUtf8("labelEBC"))
        self.horizontalLayout_3.addWidget(self.labelEBC)
        self.labelEBCV = QtGui.QLabel(self.centralwidget)
        self.labelEBCV.setText(_fromUtf8(""))
        self.labelEBCV.setObjectName(_fromUtf8("labelEBCV"))
        self.horizontalLayout_3.addWidget(self.labelEBCV)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout_3.addWidget(self.line_3)
        self.labelIBU = QtGui.QLabel(self.centralwidget)
        self.labelIBU.setObjectName(_fromUtf8("labelIBU"))
        self.horizontalLayout_3.addWidget(self.labelIBU)
        self.labelIBUV = QtGui.QLabel(self.centralwidget)
        self.labelIBUV.setText(_fromUtf8(""))
        self.labelIBUV.setObjectName(_fromUtf8("labelIBUV"))
        self.horizontalLayout_3.addWidget(self.labelIBUV)
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.horizontalLayout_3.addWidget(self.line_4)
        self.labelAlc = QtGui.QLabel(self.centralwidget)
        self.labelAlc.setObjectName(_fromUtf8("labelAlc"))
        self.horizontalLayout_3.addWidget(self.labelAlc)
        self.labelAlcv = QtGui.QLabel(self.centralwidget)
        self.labelAlcv.setText(_fromUtf8(""))
        self.labelAlcv.setObjectName(_fromUtf8("labelAlcv"))
        self.horizontalLayout_3.addWidget(self.labelAlcv)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.labelFermentables = QtGui.QLabel(self.centralwidget)
        self.labelFermentables.setObjectName(_fromUtf8("labelFermentables"))
        self.gridLayout.addWidget(self.labelFermentables, 4, 0, 1, 1)
        self.tableViewF = QtGui.QTableView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableViewF.sizePolicy().hasHeightForWidth())
        self.tableViewF.setSizePolicy(sizePolicy)
        self.tableViewF.setEditTriggers(QtGui.QAbstractItemView.AllEditTriggers)
        self.tableViewF.setAlternatingRowColors(True)
        self.tableViewF.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableViewF.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableViewF.setShowGrid(False)
        self.tableViewF.setGridStyle(QtCore.Qt.NoPen)
        self.tableViewF.setObjectName(_fromUtf8("tableViewF"))
        self.tableViewF.horizontalHeader().setCascadingSectionResizes(True)
        self.tableViewF.horizontalHeader().setDefaultSectionSize(175)
        self.tableViewF.horizontalHeader().setStretchLastSection(True)
        self.tableViewF.verticalHeader().setVisible(False)
        self.tableViewF.verticalHeader().setDefaultSectionSize(22)
        self.tableViewF.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableViewF, 5, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_5.addWidget(self.pushButton)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.pushButtonEssai = QtGui.QPushButton(self.centralwidget)
        self.pushButtonEssai.setObjectName(_fromUtf8("pushButtonEssai"))
        self.horizontalLayout_5.addWidget(self.pushButtonEssai)
        self.gridLayout.addLayout(self.horizontalLayout_5, 8, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionOuvrir = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOuvrir.setIcon(icon1)
        self.actionOuvrir.setObjectName(_fromUtf8("actionOuvrir"))
        self.actionQuitter = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Images/application-exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuitter.setIcon(icon2)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Images/help-about.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon3)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.toolBar.addAction(self.actionOuvrir)
        self.toolBar.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "JolieBulle", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRecette.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Nom de la recette :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelGenre.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Genre :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2Volume.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Volume</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelBoil.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Ebullition</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelRendement.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Rendement</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelOG.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">OG :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFG.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">FG :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelEBC.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">EBC :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelIBU.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">IBU :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelAlc.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Alc :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFermentables.setText(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Ingredients : </span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonEssai.setText(QtGui.QApplication.translate("MainWindow", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOuvrir.setText(QtGui.QApplication.translate("MainWindow", "Ouvrir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuitter.setText(QtGui.QApplication.translate("MainWindow", "Quitter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "A propos", None, QtGui.QApplication.UnicodeUTF8))

import toolbar_rc
