#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­



import os
import os.path
import PyQt5
import sys
from sys import platform
import logging
from PyQt5 import QtWidgets
from PyQt5 import QtCore
import xml.etree.ElementTree as ET
from globals import *
from model.fermentable import *
from model.hop import *
from model.yeast import *
from model.misc import *
from model.mash import *
from base import *
from operator import attrgetter
import view.base

logger = logging.getLogger(__name__)

class ImportIng (QtWidgets.QDialog) :
    def __init__(self,parent=None):
        QtWidgets.QDialog.__init__(self, parent)

    def parseFile(self, s) :
        fichierBeerXML = s
        try:
            self.arbre = ET.parse(fichierBeerXML)
            presentation=self.arbre.find('.//RECIPE')
            fermentables=self.arbre.findall('.//FERMENTABLE')
            hops = self.arbre.findall('.//HOP')
            levures = self.arbre.findall('.//YEAST')
            misc = self.arbre.findall('.//MISC')

            for element in hops:
                ImportBase.addHop( Hop.parse(element))
            for element in fermentables:
                ImportBase.addFermentable(Fermentable.parse(element))
            for element in misc:
                ImportBase.addMisc(Misc.parse(element))
            for element in levures:
                ImportBase.addYeast(Yeast.parse(element))
        except:
            self.warningFile()

        self.hopsNum = len(hops)
        self.fermNum = len(fermentables)
        self.miscNum = len(misc)
        self.yeastNum = len(levures)

        self.info()

    def info(self):
        info = QtWidgets.QMessageBox.information(self, self.tr("Importation réussie"), self.tr("Importation réussie de %s houblons, %s fermentables, %s ingrédients divers, %s levures." %(self.hopsNum, self.fermNum, self.miscNum, self.yeastNum)))

    def warningFile(self):
        warning = QtWidgets.QMessageBox.warning(self,
                        self.tr("Fichier non compatible"),
                        self.tr("Le fichier n'est pas compatible.")
                        )
