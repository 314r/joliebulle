#!/usr/bin/python3
#­*­coding: utf­8 -­*­



#joliebulle 3.5
#Copyright (C) 2010-2016 Pierre Tavares
#Copyright (C) 2012-2015 joliebulle's authors
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
import PyQt5
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore

class Errors (QtWidgets.QWidget) :
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)


    def errorMashMissing(self) :
        warning = QtWidgets.QMessageBox.warning(self,
                                self.tr("Fichier incompatible"),
                                self.tr("La recette ne possède pas d'information de brassage. \
                                    Le mode brassage fonctionnera mal. \
                                    Vous devriez éditer la recette et définir un profil de brassage.")
                                )

    def warningXml(self) :
        warning = QtWidgets.QMessageBox.warning(self,
                                self.tr("Fichier incompatible"),
                                self.tr("Le fichier que vous essayez d'ouvrir n'est pas une recette ou n'est pas compatible.")
                                )

    def warningExistingPath(self) :
        warning = QtWidgets.QMessageBox.warning(self,
                            self.tr("Recette déjà existante"),
                            self.tr("Ce nom de recette existe déjà. L'enregistrement a été annulé. Vous pouvez choisir un nouveau nom.")
                            )

    def warningExistingFile(self):
        warning = QtWidgets.QMessageBox.warning(self,
                        self.tr("Fichier existant"),
                        self.tr("Un fichier portant le même nom existe déjà dans la bibliothèque. JolieBulle a bloqué l'importation pour éviter son écrasement.")
                        )
