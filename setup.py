#!/usr/bin/python
#­*­coding: utf­8 -­*­


from distutils.core import setup

setup(name = "joliebulle",
      version = "2.0",
      description = "jolibulle, logiciel de brassage libre",
      author = "Pierre Tavares",
      author_email = "contact.314r@gmail.com",
      url = "http://joliebulle.tuxfamily.org",
      py_modules = [],
      data_files = [("joliebulle", ["base.py",
                                     "calculs.py",
                                     "densimetre_ui.py",
                                     "editdivers.py",
                                     "editgrain.py",
                                     "edithoublon.py",
                                     "editlevures.py",
                                     "editorG_ui.py",
                                     "editorH_ui.py",
                                     "editorM_ui.py",
                                     "editorY_ui.py",
                                     "export.py",
                                     "joliebulle_en.qm"
                                     "main.py",
                                     "outilAlc.py",
                                     "outilAlc_ui.py",
                                     "outilDens.py",
                                     "reader.py",
                                     "database.xml",
                                     "launch.sh",
                                     "README",
                                     "COPYING"
                                     ]),
                      ("applications", ["joliebulle.desktop"]),
                      ("joliebulle/Images", ["Images/application-exit.png",
                                            "Images/bulle.png",
                                            "Images/document-open.png",
                                            "Images/document-properties.png",
                                            "Images/help-about.png",
                                            "Images/document-open.svg"
                                            "Images/more.png"])
                                                    ],
      scripts = ["joliebulle"],
      long_description = ""          
      )    
