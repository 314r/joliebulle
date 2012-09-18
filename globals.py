#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#JolieBulle 2.7
#Copyright (C) 2010-2012 Pierre Tavares
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.


import os
from sys import platform
from settings import *

settings = Settings()

#Version Joliebulle à utiliser partout où nécessaire de l'afficher
# à modifier à chaque release pour :
#   - retirer le '-DEV' au moment de la livraison
#   - incrémenter le numéro de version et remettre le '-DEV' au commencement de la nouvelle itération
VERSION_JOLIBULLE = '2.8.0-DEV' 

if platform == 'win32':
    home_dir = os.path.expanduser("~")
    config_dir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "joliebulle")
    #recettes_dir = os.path.join(os.path.expanduser("~"), "AppData", "Local", "joliebulle", "recettes")
    recettes_dir = settings.conf.value("pathWin32", os.path.join(os.path.expanduser("~"), "AppData", "Local", "joliebulle", "recettes"))
    database_file = os.path.join(os.path.expanduser("~"), "AppData", "Local", "joliebulle", "database.xml")
    database_root = 'database.xml'
    mash_root = 'mash.xml'
    mash_file = os.path.join(os.path.expanduser("~"), "AppData", "Local", "joliebulle", "mash.xml")
    samples_dir = 'Samples'
    samples_target = os.path.join(os.path.expanduser("~"), "AppData", "Local", "joliebulle", "recettes","Samples")
    
    
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
    samples_dir='Samples'
    samples_target = os.path.join(os.path.expanduser("~"), ".config", "joliebulle", "recettes", "Samples")
