#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­



#JolieBulle 2.6
#Copyright (C) 2010-2012 Pierre Tavares

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




import PyQt4
import sys
import logging
from PyQt4 import QtCore
import xml.etree.ElementTree as ET
from globals import *
from model.fermentable import *
from model.hop import *
from model.yeast import *
from model.misc import *

logger = logging.getLogger(__name__)


#Singleton class, should be in some common module
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ImportBase(object,metaclass=Singleton) :

    def __init__(self):
        logger.debug("Import %s", database_file)
        fichierBeerXML = database_file
        arbre = ET.parse(fichierBeerXML)

        presentation=arbre.find('.//RECIPE')
        fermentables=arbre.findall('.//FERMENTABLE')
        hops = arbre.findall('.//HOP')
        levures = arbre.findall('.//YEAST')
        misc = arbre.findall('.//MISC')
 
        
        self.listeFermentables = list()
        self.listeHops = list()
        self.listeYeasts = list()
        self.listeMiscs = list()

        #Ingredient fermentescibles
        for element in fermentables:
            self.listeFermentables.append( Fermentable.parse(element) )
        logger.debug( "%s fermentables in database, using %s bytes in memory", len(self.listeFermentables), sys.getsizeof(self.listeFermentables) )

        #Houblons
        for element in hops:
            self.listeHops.append( Hop.parse(element) )
        logger.debug( "%s hops in database, using %s bytes in memory", len(self.listeHops), sys.getsizeof(self.listeHops) )

        #Levures
        for element in levures:
            self.listeYeasts.append( Yeast.parse(element) )
        logger.debug( "%s yeasts in database, using %s bytes in memory", len(self.listeYeasts), sys.getsizeof(self.listeYeasts) )

        #Ingredients divers
        for element in misc:
            self.listeMiscs.append( Misc.parse(element) )
        logger.debug( "%s miscs in database, using %s bytes in memory", len(self.listeMiscs), sys.getsizeof(self.listeMiscs) )

        logger.debug("Import %s terminé", database_file)
