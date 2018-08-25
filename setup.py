#!/usr/bin/python3
#­*­coding: utf­8 -­*­

APP = ["joliebulle/main.py"]
NAME = "Joliebulle"
VERSION = "3.7.3"

setup_info = dict(
    name = NAME,
    version = VERSION,
    app = APP,
    license='GPLv3',
    options=dict(
        py2app=dict(
            iconfile='dist/Mac/bulle.icns',
            plist=dict(
                CFBundleName               = NAME,
                CFBundleShortVersionString = VERSION,     # must be in X.X.X format
                CFBundleGetInfoString      = NAME + " " + VERSION,
                CFBundleExecutable         = NAME,
                CFBundleIdentifier         = "com.joliebulle",
            ),
            argv_emulation=True,
            includes=['sip', 'PyQt5','PyQt5.QtNetwork'],
        ),
    ),
    description = "JolieBulle, logiciel de brassage libre",
    author = "Pierre Tavares",
    author_email = "contact.314r@gmail.com",
    url = "http://joliebulle.tuxfamily.org",
    package_data = {
        "joliebulle":[
            "*.py",
            "*.qm",
            "*.xml",
            "*.json",
            "Images/*.png",
            "Samples/*.xml",
            "*/*.py",
            "*/*/*.py",
            "static/beercalc/*",
            "static/controllers/brewday/*",
            "static/controllers/journal/*",
            "static/controllers/recipe/*",
            "static/controllers/recipes-lib/*",
            "static/controllers/tools/*",
            "static/css/*",
            "static/bootstrap/LICENCE",
            "static/bootstrap/css/*",
            "static/bootstrap/js/*",
            "static/font-awesome/css/*",
            "static/font-awesome/fonts/*",
            "static/jquery/*",
            "static/angular/*",
            "static/underscore/*",
            "static/html/*"
        ]
    },
    setup_requires=['py2app'],
    scripts = ["bin/joliebulle"],
    iconfile='joliebulle/Images/bulle.png'       
)  

from sys import platform

if platform == 'darwin':
    from setuptools import setup
    setup_info['data_files'] = ["joliebulle/database.xml","joliebulle/mash.xml","joliebulle/journal.json", "dist/Mac/qt.conf"]
    setup_info['data_files'] += ["joliebulle/static/"]
    setup_info['data_files'] += ["joliebulle/"]
elif platform.startswith('linux'):
    from distutils.core import setup
    setup_info['packages'] = [ "joliebulle" ]
    setup_info['data_files'] = [("applications", ["dist/Linux/joliebulle.desktop"])]

setup(**setup_info)
