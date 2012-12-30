#!/usr/bin/python
#­*­coding: utf­8 -­*­

APP = ["main.py"]
NAME = "Joliebulle"
VERSION = "2.7.0"

setup_info = dict(
      name = NAME,
      version = VERSION,
      app = APP,
      options=dict(
	py2app=dict(
		iconfile='dist/Mac/bulle.icns',
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
      packages = [ "" ],
      package_data = { "":["*.py", "*.qm", "*.xml", "Images/*.png", "Samples/*.xml", "README", "COPYING"] },
      data_files = [("applications", ["joliebulle.desktop"])],
      setup_requires=['py2app'],
      scripts = ["joliebulle"],
      iconfile='Images/bulle.png'       
)  

from sys import platform

if platform == 'darwin':
    from setuptools import setup
    del setup_info['packages']
elif platform.startswith('linux'):
    from distutils.core import setup

setup(**setup_info)
