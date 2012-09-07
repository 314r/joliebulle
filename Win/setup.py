#!/usr/bin/python
#­*­coding: utf­8 -­*­


import sys, os
from cx_Freeze import setup, Executable



includes=["base.py","brewCalc.py","densimetre_ui.py","editdivers.py","editgrain.py","edithoublon.py","editlevures.py","editorG_ui.py","editorH_ui.py","editorM_ui.py","editorY_ui.py","exportHTML.py","export.py","exportMash.py","globals.py","home.py","importMashXml.py", "joliebulle_en.qm","main.py","mashEditor_ui.py","mashEditWindow.py","outilAlc.py","outilAlc_ui.py","outilDens.py","outilDilution.py", "outilDilution_ui.py","outilEvaporation.py","outilEvaporation_ui.py","outilPaliers.py","outilPaliers_ui.py","preferences.py", "preferences_ui.py", "reader.py", "settings.py","stepAdjust_ui.py","stepAdjustWindow.py","stepEditor_ui.py","stepEditWindow.py","database.xml","mash.xml","launch.sh","README","COPYING"]

excludes = []
packages = ["database.xml","mash.xml"]
icon = ["main.ico"]

options = {"includes": includes,
           "excludes": excludes,
           "packages": packages,
		   "icon":icon
           }



base = None
if sys.platform == "win32":
    base = "Win32GUI"



cible_1 = Executable(
    script = "main.py",
    base = base,
    compress = True,
    icon = "main.ico",
    )









setup(name = "joliebulle",
      version = "2.7",
      description = "joliebulle, logiciel de brassage libre",
      author = "Pierre Tavares",
      author_email = "contact.314r@gmail.com",
      url = "http://joliebulle.tuxfamily.org", 

      executables = [cible_1]
      )    
