# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecipeView.ui'
#
# Created: Mon Nov 12 22:18:12 2012
#      by: PyQt4 UI code generator 4.9.5
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
        RecipeView.resize(807, 704)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RecipeView.sizePolicy().hasHeightForWidth())
        RecipeView.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(RecipeView)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(RecipeView)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setLineWidth(1)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.recipeListView = QtGui.QListView(self.splitter)
        self.recipeListView.setResizeMode(QtGui.QListView.Fixed)
        self.recipeListView.setModelColumn(0)
        self.recipeListView.setObjectName(_fromUtf8("recipeListView"))
        self.webView = QtWebKit.QWebView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webView.sizePolicy().hasHeightForWidth())
        self.webView.setSizePolicy(sizePolicy)
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(RecipeView)
        QtCore.QMetaObject.connectSlotsByName(RecipeView)

    def retranslateUi(self, RecipeView):
        RecipeView.setWindowTitle(QtGui.QApplication.translate("RecipeView", "Form", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit
