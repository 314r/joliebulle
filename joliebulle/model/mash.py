#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­

import logging
import model.constants
from model.mashstep import *

logger = logging.getLogger(__name__)

class Mash:
    def __init__(self):
        self.name = ""
        self.grainTemp = ""
        self.tunTemp = ""
        self.spargeTemp = ""
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
                m.spargeTemp = element.text
            if 'PH' == element.tag :
                m.ph = element.text

        try :
            mashStep = tree.findall('.//MASH_STEP')
            for element in mashStep:
                m.listeSteps.append(MashStep.parse(element))
        except :
            pass

        logger.debug(repr(m))
        return m

