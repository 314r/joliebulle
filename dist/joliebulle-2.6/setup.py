#!/usr/bin/python
#­*­coding: utf­8 -­*­


from distutils.core import setup

setup(name = "joliebulle",
      version = "2.6",
      description = "JolieBulle, logiciel de brassage libre",
      author = "Pierre Tavares",
      author_email = "contact.314r@gmail.com",
      url = "http://joliebulle.tuxfamily.org",
      py_modules = [],
      data_files = [("joliebulle", ["base.py",
                                     "brewCalc.py",
                                     "densimetre_ui.py",
                                     "editdivers.py",
                                     "editgrain.py",
                                     "edithoublon.py",
                                     "editlevures.py",
                                     "editorG_ui.py",
                                     "editorH_ui.py",
                                     "editorM_ui.py",
                                     "editorY_ui.py",
                                     "exportHTML.py",
                                     "export.py",
                                     "exportMash.py",
                                     "globals.py",
                                     "importMashXml.py",
                                     "joliebulle_en.qm",
                                     "main.py",
                                     "mashEditor_ui.py",
                                     "mashEditWindow.py",
                                     "outilAlc.py",
                                     "outilAlc_ui.py",
                                     "outilDens.py",
                                     "outilDilution.py",
                                     "outilDilution_ui.py",
                                     "outilEvaporation.py",
                                     "outilEvaporation_ui.py",
                                     "outilPaliers.py",
                                     "outilPaliers_ui.py",
                                     "preferences.py",
                                     "preferences_ui.py",
                                     "reader.py",
                                     "ressources_rc.py",
                                     "settings.py",
                                     "stepAdjust_ui.py",
                                     "stepAdjustWindow.py",
                                     "stepEditor_ui.py",
                                     "stepEditWindow.py",
                                     "database.xml",
                                     "mash.xml",
                                     "launch.sh",
                                     "README",
                                     "COPYING"
                                     ]),
                      ("applications", ["joliebulle.desktop"]),
                      ("joliebulle/Images", ["Images/application-exit.png",
                                            "Images/add.png",
                                            "Images/bulle.png",
                                            "Images/brewday.png",
                                            "Images/config.png",
                                            "Images/document-open.png",
                                            "Images/document-properties.png",
                                            "Images/edit.png",
                                            "Images/help-about.png",
                                            "Images/library.png",
                                            "Images/document-open.svg",
                                            "Images/more.png",
                                            "Images/print.png",
                                            "Images/reload.png",
                                            "Images/remove.png",
                                            "Images/save.png",])
                                                    ],
      scripts = ["joliebulle"],
      long_description = ""          
      )    