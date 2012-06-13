 #!/usr/bin/python3
#­*­coding: utf­8 -­*­

import os
from sys import platform
from settings import *

settings = Settings()

if platform == 'win32':
    home_dir = os.path.expanduser("~")
    config_dir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "joliebulle")
    #recettes_dir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "joliebulle", "recettes")
    recettes_dir = settings.conf.value("pathWin32", os.path.join(os.path.expanduser("~"), "AppData", "Local", "joliebulle", "recettes"))
    database_file = os.path.join(os.path.expanduser("~"), "AppData", "Local", "joliebulle", "database.xml")
    database_root = 'database.xml'
    mash_root = 'mash.xml'
    mash_file = os.path.join(os.path.expanduser("~"), "AppData", "Local", "joliebulle", "mash.xml")
    
else:
    home_dir = os.path.expanduser("~")
    config_dir = os.path.join(os.path.expanduser("~"), ".config", "joliebulle")
    #recettes_dir = os.path.join(os.path.expanduser("~"), ".config", "joliebulle", "recettes")
    recettes_dir = settings.conf.value("pathUnix", os.path.join(os.path.expanduser("~"), ".config", "joliebulle", "recettes"))
    database_file = os.path.join(os.path.expanduser("~"), ".config", "joliebulle", "database.xml")
    database_root = '/usr/share/joliebulle/database.xml'
    #essai = settings.conf.value("pathUnix")
    mash_file = os.path.join(os.path.expanduser("~"), ".config", "joliebulle", "mash.xml")
    mash_root = '/usr/share/joliebulle/mash.xml'


