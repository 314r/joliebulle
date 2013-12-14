#!/usr/bin/python3
#­*­coding: utf­8 -­*­



#joliebulle 3.1
#Copyright (C) 2010-2013 Pierre Tavares
#Copyright (C) 2012-2013 joliebulle's authors
#See AUTHORS file.

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 3        
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.


import os
import os.path
import glob
import logging
import logging.config
from sys import platform
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class Errors (QtGui.QWidget) :
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)


    def errorMashMissing(self) :
        warning = QtGui.QMessageBox.warning(self,
                                self.trUtf8("Fichier incompatible"),
                                self.trUtf8("La recette ne possède pas d'information de brassage. \
                                    Le mode brassage fonctionnera mal. \
                                    Vous devriez éditer la recette et définir un profil de brassage.")
                                )

    def warningXml(self) :
        warning = QtGui.QMessageBox.warning(self,
                                self.trUtf8("Fichier incompatible"),
                                self.trUtf8("Le fichier que vous essayez d'ouvrir n'est pas une recette ou n'est pas compatible.")
                                )

    def warningExistingPath(self) :
        warning = QtGui.QMessageBox.warning(self,
                            self.trUtf8("Recette déjà existante"),
                            self.trUtf8("Ce nom de recette existe déjà. L'enregistrement a été annulé. Vous pouvez choisir un nouveau nom.")
                            )

    def warningExistingFile(self):
        warning = QtGui.QMessageBox.warning(self,
                        self.trUtf8("Fichier existant"),
                        self.trUtf8("Un fichier portant le même nom existe déjà dans la bibliothèque. JolieBulle a bloqué l'importation pour éviter son écrasement.")
                        )
