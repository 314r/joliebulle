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
            journal.itemsList=sorted(journal.itemsList, key= lambda k :k['date'], reverse=True)
            # print(journal.itemsList)
        return journal

    def customEncode(self,obj) :
        if isinstance(obj,Journal):
            return {
                "__class__" : "Journal",
                "name" : "journal",
                "items" : obj.itemsList
            }
        else :
            pass

    def dump (self,journal,journal_file) :
        with open(journal_file, mode="w", encoding="utf-8") as f :
            json.dump(journal,f,default=self.customEncode,indent=2)


    def loadJournal(self):
        self.journal = Journal().load(journal_file)
        # for entry in self.journal.itemsList :
        #     print("nom de la recette :", entry['recipe'])
        # self.addJournal("essai", "event")

    def addJournal(self,date,event,recipe):
        entry = {}
        entry['recipe'] = recipe
        entry['date'] =date
        entry['event'] = event
        entry['__class__'] = 'JournalItem'
        self.journal.itemsList.append(entry)
        self.journal.dump(self.journal,journal_file)

    def delEntry(self,index):
        # del self.journal.itemsList[index]
        self.journal.itemsList=[dic for dic in self.journal.itemsList if dic.get('date') != str(index)]
        print(self.journal.itemsList)
        self.dump(self.journal,journal_file)
        
    def export(self,type) :
        return JournalExporterRepository[type](json.dumps(self.journal.itemsList), '''{recipe : 'recipe', date : '1386261776',event:'event', editing :'True' }''')



