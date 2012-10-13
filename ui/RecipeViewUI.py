# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecipeView.ui'
#
# Created: Sat Oct 13 22:38:50 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RecipeView(object):
    def setupUi(self, RecipeView):
        RecipeView.setObjectName(_fromUtf8("RecipeView"))
        RecipeView.resize(741, 496)
        self.horizontalLayout = QtGui.QHBoxLayout(RecipeView)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(RecipeView)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.webView = QtWebKit.QWebView(self.splitter)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.listView = QtGui.QListView(self.splitter)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(RecipeView)
        QtCore.QMetaObject.connectSlotsByName(RecipeView)

    def retranslateUi(self, RecipeView):
        RecipeView.setWindowTitle(QtGui.QApplication.translate("RecipeView", "Form", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
