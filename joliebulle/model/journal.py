#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­
from PyQt4.QtCore import QCoreApplication
import json
from globals import *
from helper.journalExporterRepository import *
import time

class Journal :
    def __init__(self):
        self.dct={}
        self.itemsList=list()
        self.text=""

        self.eventsLabels = {
            'brewed': QCoreApplication.translate("Export", "brassée", None, QCoreApplication.UnicodeUTF8),
            'ferment': QCoreApplication.translate("Export", "mise en fermentation", None, QCoreApplication.UnicodeUTF8),
            'bottled': QCoreApplication.translate("Export", "embouteillée", None, QCoreApplication.UnicodeUTF8)
        }

    @staticmethod
    def load (jsonFile) :
        journal=Journal()
        with open(jsonFile, "r", encoding="utf-8") as f :
            journal.dct=json.load(f)
            journal.itemsList = journal.dct["items"]
        return journal
        json.dump(self.journal,f,default=self.customEncode,indent=2)


    def loadJournal(self):
        self.journal = Journal().load(journal_file)
        
    def export(self,type,entry) :
        return JournalExporterRepository[type](json.dumps(self.journal.itemsList), entry)
# '''{recipe : 'recipe', date : '1386261776',event:'event', editing :'True' }'''


