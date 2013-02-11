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
from operator import attrgetter

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
        self.arbre = ET.parse(fichierBeerXML)

        presentation=self.arbre.find('.//RECIPE')
        fermentables=self.arbre.findall('.//FERMENTABLE')
        hops = self.arbre.findall('.//HOP')
        levures = self.arbre.findall('.//YEAST')
        misc = self.arbre.findall('.//MISC')
 
        
        self.listeFermentables = list()
        self.listeHops = list()
        self.listeYeasts = list()
        self.listeMiscs = list()

        #Ingredient fermentescibles
        for element in fermentables:
            self.listeFermentables.append( Fermentable.parse(element) )
        self.listeFermentables = sorted(self.listeFermentables, key=attrgetter('name'))
        logger.debug( "%s fermentables in database, using %s bytes in memory", len(self.listeFermentables), sys.getsizeof(self.listeFermentables) )

        #Houblons
        for element in hops:
            self.listeHops.append( Hop.parse(element) )
        self.listeHops = sorted(self.listeHops, key=attrgetter('name'))
        logger.debug( "%s hops in database, using %s bytes in memory", len(self.listeHops), sys.getsizeof(self.listeHops) )

        #Levures
        for element in levures:
            self.listeYeasts.append( Yeast.parse(element) )
        logger.debug( "%s yeasts in database, using %s bytes in memory", len(self.listeYeasts), sys.getsizeof(self.listeYeasts) )

        #Ingredients divers
        for element in misc:
            self.listeMiscs.append( Misc.parse(element) )
        self.listeMiscs = sorted(self.listeMiscs, key=attrgetter('name'))
        logger.debug( "%s miscs in database, using %s bytes in memory", len(self.listeMiscs), sys.getsizeof(self.listeMiscs) )

        logger.debug("Import %s terminé", database_file)

    @staticmethod
    def addFermentable(f):
        ImportBase().listeFermentables.append(f)
        ImportBase().listeFermentables = sorted(ImportBase().listeFermentables, key=attrgetter('name'))

        root = ImportBase().arbre.getroot()
        root.append(f.toXml())
        databaseXML = open(database_file, 'wb')
        ImportBase().arbre._setroot(root)
        ImportBase().arbre.write(databaseXML, encoding="utf-8")
        databaseXML.close()

    @staticmethod
    def delFermentable(f):
        i = ImportBase().listeFermentables.index(f)
        ImportBase().listeFermentables.remove(f)
        root = ImportBase().arbre.getroot()
        iterator = root.iter("FERMENTABLE")
        item = None
        for elem in iterator :
            tempF = Fermentable.parse(elem)
            if f.name == tempF.name :
                item = elem
        if item is not None:
            root.remove(item)
            databaseXML = open(database_file, 'wb')
            ImportBase().arbre._setroot(root)
            ImportBase().arbre.write(databaseXML, encoding="utf-8")
            databaseXML.close() 

    @staticmethod
    def addHop(h):
        ImportBase().listeHops.append(h)
        ImportBase().listeHops = sorted(ImportBase().listeHops, key=attrgetter('name'))

        root = ImportBase().arbre.getroot()
        root.append(h.toXml())
        databaseXML = open(database_file, 'wb')
        ImportBase().arbre._setroot(root)
        ImportBase().arbre.write(databaseXML, encoding="utf-8")
        databaseXML.close()

    @staticmethod
    def delHop(h):
        i = ImportBase().listeHops.index(h)
        ImportBase().listeHops.remove(h)
        root = ImportBase().arbre.getroot()
        iterator = root.iter("HOP")
        item = None
        for elem in iterator :
            tempHop = Hop.parse(elem)
            if h.name == tempHop.name :
                item = elem
        if item is not None:
            root.remove(item)
            databaseXML = open(database_file, 'wb')
            ImportBase().arbre._setroot(root)
            ImportBase().arbre.write(databaseXML, encoding="utf-8")
            databaseXML.close() 

    @staticmethod
    def addMisc(m):
        ImportBase().listeMiscs.append(m)
        ImportBase().listeMiscs = sorted(ImportBase().listeMiscs, key=attrgetter('name'))

        root = ImportBase().arbre.getroot()
        root.append(m.toXml())
        databaseXML = open(database_file, 'wb')
        ImportBase().arbre._setroot(root)
        ImportBase().arbre.write(databaseXML, encoding="utf-8")
        databaseXML.close()

    @staticmethod
    def delMisc(m):
        i = ImportBase().listeMiscs.index(m)
        ImportBase().listeMiscs.remove(m)
        root = ImportBase().arbre.getroot()
        iterator = root.iter("MISC")
        item = None
        for elem in iterator :
            tempMisc = Misc.parse(elem)
            if m.name == tempMisc.name :
                item = elem
        if item is not None:
            root.remove(item)
            databaseXML = open(database_file, 'wb')
            ImportBase().arbre._setroot(root)
            ImportBase().arbre.write(databaseXML, encoding="utf-8")
            databaseXML.close() 
