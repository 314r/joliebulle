from setuptools import setup

APP = ['../../main.py']
NAME = "Joliebulle"
VERSION = "2.7.0"

DATA_FILES = ["../../database.xml","../../mash.xml", "qt.conf"]

setup(
	options=dict(
		py2app=dict(
			iconfile='bulle.icns',
#			site_packages=True,
			plist=dict(
				CFBundleName               = NAME,
				CFBundleShortVersionString = VERSION,     # must be in X.X.X format
				CFBundleGetInfoString      = NAME + VERSION,
				CFBundleExecutable         = NAME,
				CFBundleIdentifier         = "com.joliebulle",
			),
			argv_emulation=True,
			includes=['sip', 'PyQt4','PyQt4.QtNetwork'],
#			packages=DATA_FILES
		),
  	),
	iconfile='../../Images/bulle.png',
	app=APP,
	data_files=DATA_FILES,
	#options={'py2app': OPTIONS},
	setup_requires=['py2app'],
	name = NAME,
	version = VERSION,
	description = "joliebulle, logiciel de brassage libre",
	author = "Pierre Tavares",
	author_email = "contact.314r@gmail.com",
	url = "http://joliebulle.tuxfamily.org"
)
