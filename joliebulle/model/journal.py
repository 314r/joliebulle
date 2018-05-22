#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­

#joliebulle 3.6
#Copyright (C) 2010-2016 Pierre Tavares


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


from PyQt5.QtCore import QCoreApplication
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
            'brewed': "brassée",
            'ferment': "mise en fermentation",
            'dryhop': "dryhopée",
            'bottled': "embouteillée",
            'maturation': "mise en garde", 
        }

    @staticmethod
    def load (jsonFile) :
        journal=Journal()
        with open(jsonFile, "r", encoding="utf-8") as f :
            journal.dct=json.load(f)
            journal.itemsList = journal.dct["items"]
            print(journal.itemsList)
        return journal
        # json.dump(self.journal,f,default=self.customEncode,indent=2)


    def loadJournal(self):
        self.journal = Journal().load(journal_file)

    def export(self,type,entry) :
        data = json.dumps(self.journal.itemsList)
        data = data.replace("'","&#39;")
        return JournalExporterRepository[type](data, entry)
# '''{recipe : 'recipe', date : '1386261776',event:'event', editing :'True' }'''
