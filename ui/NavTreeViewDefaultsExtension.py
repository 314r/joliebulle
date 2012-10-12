from plugins.ExtensionPoints import NavTreeViewExtensionPoint
from PyQt4 import QtCore

__author__ = 'nico'

class NavTreeViewDefaultsExtension(NavTreeViewExtensionPoint):
    def __init__(self):
        self.model = [
            {'id':'recipes',
             'label':QtCore.QCoreApplication.translate(__name__, '''Recettes'''),
             'items' : {
               'id':'recipes.all',
               'label':QtCore.QCoreApplication.translate(__name__, '''Toutes''')
             }
            },
            {'id':'catalog',
             'label':QtCore.QCoreApplication.translate(__name__, '''Catalogue''')},
            {'id':'tools',
             'label':QtCore.QCoreApplication.translate(__name__, '''Outils''')},
            ]

    def getItems(self, parentId=None):
        if parentId is None :
            #return list of parent items from model
            return [{item['id'], item['label']} for item in self.model] 
        if not parentId is None:
            #return list of subitems
            return [parent['items'] for parent in self.model if parent['id']==parentId]
        return None
