#!/usr/bin/python3
#­*­coding: utf­8 -­*­




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