#!/usr/bin/python
#­*­coding: utf­8 -­*­





import PyQt5
import sys
import logging
from PyQt5 import QtCore
import json
import xml.etree.ElementTree as ET
from globals import *
from model.fermentable import *
from model.hop import *
from model.yeast import *
from model.misc import *
from model.mash import *
from model.constants import *
from operator import attrgetter
from singleton import Singleton


logger = logging.getLogger(__name__)

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
        self.listeYeasts = sorted(self.listeYeasts, key=attrgetter('name'))
        logger.debug( "%s yeasts in database, using %s bytes in memory", len(self.listeYeasts), sys.getsizeof(self.listeYeasts) )

        #Ingredients divers
        for element in misc:
            self.listeMiscs.append( Misc.parse(element) )
        self.listeMiscs = sorted(self.listeMiscs, key=attrgetter('name'))
        logger.debug( "%s miscs in database, using %s bytes in memory", len(self.listeMiscs), sys.getsizeof(self.listeMiscs) )

        logger.debug("Import %s terminé", database_file)

        #Import Mash file
        logger.debug("Import %s", mash_file)
        arbre = ET.parse(mash_file)

        mash = arbre.findall('.//MASH')
        self.listeMashes = list()

        for element in mash:
            self.listeMashes.append( Mash.parse(element) )
        logger.debug( "%s mash in database, using %s bytes in memory", len(self.listeMashes), sys.getsizeof(self.listeMashes) )

        logger.debug("Import %s terminé", mash_file)

    @staticmethod
    def __indent(elem, level=0):
        i = "\n" + level*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                ImportBase.__indent(elem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    @staticmethod
    def save(root_node):
        with open(database_file, 'wb') as database_xml:
            ImportBase.__indent(root_node)
            ET.ElementTree(root_node).write(database_xml, encoding="utf-8")

    @staticmethod
    def addFermentable(f):
        ImportBase().listeFermentables.append(f)
        ImportBase().listeFermentables = sorted(ImportBase().listeFermentables, key=attrgetter('name'))

        root = ImportBase().arbre.getroot()
        root.append(f.toXml())
        ImportBase.save(root)

    @staticmethod
    def delFermentable(f):
        ImportBase().listeFermentables.remove(f)
        root = ImportBase().arbre.getroot()
        iterator = root.iter("FERMENTABLE")
        item = None
        for elem in iterator :
            tempF = Fermentable.parse(elem)
            if f.name == tempF.name and f.type == tempF.type and f.color == tempF.color and f.recommendMash == tempF.recommendMash and f.fyield == tempF.fyield :
                item = elem
        if item is not None:
            root.remove(item)
            ImportBase.save(root)

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
        ImportBase().listeHops.remove(h)
        root = ImportBase().arbre.getroot()
        iterator = root.iter("HOP")
        item = None
        for elem in iterator :
            tempHop = Hop.parse(elem)
            if h.name == tempHop.name and h.form == tempHop.form and h.alpha == tempHop.alpha :
                item = elem
        if item is not None:
            root.remove(item)
            ImportBase.save(root)

    @staticmethod
    def addMisc(m):
        ImportBase().listeMiscs.append(m)
        ImportBase().listeMiscs = sorted(ImportBase().listeMiscs, key=attrgetter('name'))

        root = ImportBase().arbre.getroot()
        root.append(m.toXml())
        ImportBase.save(root)

    @staticmethod
    def delMisc(m):
        ImportBase().listeMiscs.remove(m)
        root = ImportBase().arbre.getroot()
        iterator = root.iter("MISC")
        item = None
        for elem in iterator :
            tempMisc = Misc.parse(elem)
            if m.name == tempMisc.name and m.type == tempMisc.type:
                item = elem
        if item is not None:
            root.remove(item)
            ImportBase.save(root)

    @staticmethod
    def addYeast(y):
        ImportBase().listeYeasts.append(y)
        ImportBase().listeYeasts = sorted(ImportBase().listeYeasts, key=attrgetter('name'))

        root = ImportBase().arbre.getroot()
        root.append(y.toXml())
        ImportBase.save(root)

    @staticmethod
    def delYeast(y):
        ImportBase().listeYeasts.remove(y)
        root = ImportBase().arbre.getroot()
        iterator = root.iter("YEAST")
        item = None
        for elem in iterator :
            tempYeast = Yeast.parse(elem)
            if y.name == tempYeast.name and y.form == tempYeast.form and y.labo == tempYeast.labo and y.productId == tempYeast.productId and y.attenuation == tempYeast.attenuation :
                item = elem
        if item is not None:
            root.remove(item)
            ImportBase.save(root)

    @staticmethod
    def exportjson() :
        # data = []
        dic ={}

        fermentables=[]
        for f in ImportBase().listeFermentables :
            fermentable =  {}
            fermentable['name'] = f.name
            fermentable['color'] = f.color
            fermentable['type'] = f.type
            fermentable['fyield'] = f.fyield
            fermentables.append(fermentable)
        dic['fermentables'] = fermentables

        hops=[]
        for h in ImportBase().listeHops :
            hop={}
            hop['name'] = h.name
            hop['alpha'] = h.alpha
            if h.form == HOP_FORM_PELLET :
                hop['form'] = "Pellet"
            elif h.form == HOP_FORM_LEAF :
                hop['form'] = "Leaf"
            elif h.form == HOP_FORM_PLUG :
                hop['form'] = "Plug"
            hops.append(hop)
        dic['hops'] = hops

        miscs=[]
        for m in ImportBase().listeMiscs :
            misc = {}
            misc['name'] = m.name
            misc['type'] = m.type
            misc['use'] = m.use
            miscs.append(misc)
        dic['miscs'] = miscs

        yeasts=[]
        for y in ImportBase().listeYeasts :
            yeast = {}
            yeast['name'] = y.name
            yeast['product_id'] = y.productId
            yeast['labo'] = y.labo
            yeast['form'] = y.form
            yeast['attenuation'] = y.attenuation
            yeasts.append(yeast)
        dic['yeasts'] = yeasts

        # data.append(dic)
        dic = json.dumps(dic)
        # dic = dic.replace("'","&#39;")

        return dic
