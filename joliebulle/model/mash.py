#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­

#JolieBulle 2.9
#Copyright (C) 2010-2013 Pierre Tavares
#Copyright (C) 2012-2013 joliebulle's authors
#See AUTHORS file.

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 3
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.


import logging
import model.constants
from model.mashstep import *

logger = logging.getLogger(__name__)

class Mash:
    def __init__(self):
        self.name = ""
        self.grainTemp = ""
        self.tunTemp = ""
        self.spargeTemp = "0"
        self.ph = 0.0
        self.listeSteps = list()

    def __repr__(self):
        return ('mash[name="%s", grainTemp="%s", tunTemp=%s, spargeTemp=%s, ph=%s]' %
                (self.name, self.grainTemp, self.tunTemp, self.spargeTemp, self.ph) )

    @staticmethod
    def parse(tree):
        m = Mash()
        for element in tree:
            if 'NAME' == element.tag :
                m.name = element.text
            if 'GRAIN_TEMP' == element.tag :
                m.grainTemp = element.text
            if 'TUN_TEMP' == element.tag  :
                m.tunTemp = element.text
            if 'SPARGE_TEMP' == element.tag  :
                m.spargeTemp = "%.1f" %float(element.text)
            # else :
            #     m.spargeTemp = 78
            if 'PH' == element.tag :
                m.ph = "%.1f" %float(element.text)

        try :
            mashStep = tree.findall('.//MASH_STEP')
            for element in mashStep:
                m.listeSteps.append(MashStep.parse(element))
        except :
            pass

        logger.debug(repr(m))
        return m

