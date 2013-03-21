from plugins.PluginManager import PluginMetaclass

class AppLifecycleExtensionPoint(object,metaclass=PluginMetaclass):
    def startup(self):
        pass

    def shutdown(self):
        pass

class NavTreeViewExtensionPoint(object,metaclass=PluginMetaclass):
    def get_items(self, parent=None):
        pass
    
    def itemSelected(self, window, item):
        pass


#Import extensions after extensions point definitions
from plugins.extensions import *
