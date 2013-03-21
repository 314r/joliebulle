#!/usr/bin/python3
#­*­coding: utf­8 -­*­

APP = ["joliebulle/main.py"]
NAME = "Joliebulle"
VERSION = "2.8.0"

setup_info = dict(
      name = NAME,
      version = VERSION,
      app = APP,
      license='GPLv3',
      options=dict(
	py2app=dict(
		iconfile='Mac/bulle.icns',
		plist=dict(
			CFBundleName               = NAME,
			CFBundleShortVersionString = VERSION,     # must be in X.X.X format
			CFBundleGetInfoString      = NAME + " " + VERSION,
			CFBundleExecutable         = NAME,
			CFBundleIdentifier         = "com.joliebulle",
			LSEnvironment			   = {'LC_ALL':'en_US.UTF-8'}
		),
		argv_emulation=True,
		includes=['sip', 'PyQt4','PyQt4.QtNetwork'],
	),
      ),
      description = "JolieBulle, logiciel de brassage libre",
      author = "Pierre Tavares",
      author_email = "contact.314r@gmail.com",
      url = "http://joliebulle.tuxfamily.org",
      package_data = { "joliebulle":["*.py", "*.qm", "*.xml", "Images/*.png", "Samples/*.xml"] },
      setup_requires=['py2app'],
      scripts = ["joliebulle/joliebulle"],
      iconfile='joliebulle/Images/bulle.png'       
)  

from sys import platform

if platform == 'darwin':
    from setuptools import setup
    setup_info['data_files'] = ["joliebulle/database.xml","joliebulle/mash.xml", "dist/Mac/qt.conf"]
elif platform.startswith('linux'):
    from distutils.core import setup
    setup_info['packages'] = [ "joliebulle" ]
    setup_info['data_files'] = [("applications", ["joliebulle/joliebulle.desktop"])]

setup(**setup_info)
