#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.5
#Copyright (C) 2010-2016 Pierre Tavares
#Copyright (C) 2012-2015 joliebulle's authors
#See AUTHORS file.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.



import os
from sys import platform
import codecs
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore


class Settings:
    def __init__ (self) :
        self.conf = QtCore.QSettings("joliebulle", "joliebulle")
        #self.conf.setValue("pathUnix", os.path.join(os.path.expanduser("~"), ".config", "joliebulle", "recettes")) 
        #self.conf.setValue("pathWin32", os.path.join(os.path.expanduser("~"), "AppData", "Local", "joliebulle", "recettes"))
