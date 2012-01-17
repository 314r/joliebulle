#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.


import os
from sys import platform
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from preferences import *
from globals import *
import xml.etree.ElementTree as ET

class ExportMash :

    def export(self,listMash) :
#        print (listMash)
        
        self.database = ET.Element('DATABASE')
        numMash = len(listMash)
        i = 0
        while i < numMash :
            i=i+1
            mash = ET.SubElement(self.database, 'MASH')
            dicMash = listMash[i-1]
            mashVersion = ET.SubElement(mash, 'VERSION')
            mashVersion.text = '1'
            mashName = ET.SubElement(mash, 'NAME')
            mashName.text = dicMash['name']
            grainTemp = ET.SubElement(mash, 'GRAIN_TEMP')
            grainTemp.text = dicMash['grainTemp']
            tunTemp = ET.SubElement(mash, 'TUN_TEMP')
            tunTemp.text = dicMash['tunTemp']
            ph = ET.SubElement(mash, 'PH')
            ph.text = dicMash['ph']
            spargeTemp = ET.SubElement(mash, 'SPARGE_TEMP')
            spargeTemp.text =dicMash['spargeTemp']
            steps = ET.SubElement(mash, 'MASH_STEPS')
            
            listSteps = dicMash['mashSteps']
            numSteps = len(listSteps)
            h = 0
            while h < numSteps :
                h = h+1
                step = ET.SubElement(steps, 'MASH_STEP')
                dicStep = listSteps[h-1] 
                stepVersion = ET.SubElement(step, 'VERSION')
                stepVersion.text = '1'
                stepName = ET.SubElement(step, 'NAME')
                stepName.text = dicStep['name']
                stepType = ET.SubElement(step, 'TYPE')
                stepType.text = dicStep['type']
                stepTemp = ET.SubElement(step, 'STEP_TEMP')
                stepTemp.text = dicStep['stepTemp']
                stepTime = ET.SubElement(step, 'STEP_TIME')
                stepTime.text = dicStep['stepTime']
                stepVol = ET.SubElement(step, 'INFUSE_AMOUNT')
                stepVol.text = dicStep['stepVol']
                
                
            
            
            
            
        
        ET.ElementTree(self.database).write('/home/pierre/essai.xml',encoding="utf-8")
            
            
                
                
        
