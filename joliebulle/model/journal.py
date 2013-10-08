#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­

import json
from globals import *
from helper.journalExporterRepository import *

class Journal :
    def __init__(self):
        self.dct={}
        self.itemsList=list()

    @staticmethod
    def load (jsonFile) :
        journal=Journal()
        with open(jsonFile, "r", encoding="utf-8") as f :
            journal.dct=json.load(f)
            journal.itemsList = journal.dct["items"]
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
        for entry in self.journal.itemsList :
            print("nom de la recette :", entry['recipe'])
        self.addJournal()

    def addJournal(self):
        entry = {}
        entry['recipe'] = 'toto'
        entry['date'] ="231415"
        entry['event'] ="essai"
        self.journal.itemsList.append(entry)
        self.journal.dump(self.journal,journal_file)

    def delEntry(self,index):
        del self.journal.itemsList[index]
        self.dump(self.journal,journal_file)
        
        

    def export(self,type) :
        return JournalExporterRepository[type](self.journal.itemsList)


