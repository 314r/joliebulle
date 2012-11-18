'''
Created on 13 oct. 2012

@author: nico
'''
from PyQt4 import QtGui, QtCore
from ui.RecipeViewUI import Ui_RecipeView

class RecipeView(QtGui.QWidget, Ui_RecipeView):
    def __init__(self, parent=None, flags=0):
        super(RecipeView, self).__init__(parent)
        self.setupUi(self)
        
        self.recipeListView.
