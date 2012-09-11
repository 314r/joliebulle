from setuptools import setup

APP = ['../../main.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True,
 'includes': ['sip', 'PyQt4']}

setup(
app=APP,
data_files=DATA_FILES,
options={'py2app': OPTIONS},
setup_requires=['py2app'],
)
