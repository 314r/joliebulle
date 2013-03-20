#!/usr/bin/python3
#­*­coding: utf­8 -­*­



#JolieBulle 2.8
#Copyright (C) 2010-2013 Pierre Tavares

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
from sys import platform
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from preferences import *
from globals import *
from model.mash import *
import xml.etree.ElementTree as ET

#Singleton class, should be in some common module
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class ImportMash(object,metaclass=Singleton): 

    def __init__(self):
        logger.debug("Import %s", mash_file)
        arbre = ET.parse(mash_file)

        mash = arbre.findall('.//MASH')
        self.listeMashes = list()

        for element in mash:
            self.listeMashes.append( Mash.parse(element) )
        logger.debug( "%s mash in database, using %s bytes in memory", len(self.listeMashes), sys.getsizeof(self.listeMashes) )

        logger.debug("Import %s terminé", mash_file)
