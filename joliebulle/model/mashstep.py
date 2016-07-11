#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­
#joliebulle 3.6
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
import model.constants
from model.fermentable import *
from model.hop import *
from model.yeast import *

logger = logging.getLogger(__name__)


class MashStep(Element):
    def __init__(self):
        self.name = ""
        self.type = ""
        self.time = ""
        self.temp = ""
        self.infuseAmount = 0.0
        self.version = 1

    def __repr__(self):
        return ('mashStep[name="%s", type="%s", time=%s, temp=%s, infuseAmount=%f, version=%d]' %
                (self.name, self.type, self.time, self.temp, self.infuseAmount, self.version) )