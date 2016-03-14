#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­

#joliebulle 3.5
#Copyright (C) 2010-2016 Pierre Tavares
#Copyright (C) 2012-2015 joliebulle's authors
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
from model.mashstep import *

logger = logging.getLogger(__name__)


class Mash(Element):
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

        logger.debug(repr(m))
        return m

