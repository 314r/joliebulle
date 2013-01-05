#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­



#JolieBulle 2.6
#Copyright (C) 2010-2012 Pierre Tavares

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

logger = logging.getLogger(__name__)

class Hop:
    """A class for storing Hops attributes"""
    def __init__(self):
        self.name = ''
        self.amount = 0.0
        self.form = model.constants.HOP_FORM_LEAF
        self.time = 0.0
        self.alpha = 0.0
        self.use = ''
    
    def __repr__(self):
        return 'hop[name="%s", amount=%s, form=%s, time=%s, alpha=%s]' % (self.name, self.amount, self.form, self.time, self.alpha)

    @staticmethod
    def parse(element):
        h = Hop()
        for balise in element:
            if 'NAME' == balise.tag :
                h.name = balise.text
            elif 'AMOUNT' == balise.tag :
                h.amount = 1000*(float(balise.text)) 
            elif 'FORM' == balise.tag :
                if 'Pellet' == balise.text:
                    h.form = model.constants.HOP_FORM_PELLET
                elif 'Leaf' == balise.text:
                    h.form = model.constants.HOP_FORM_LEAF
                elif 'Plug' == balise.text:
                    h.form = model.constants.HOP_FORM_PLUG
                else :
                    logger.warn ("Unkown hop form '%s', assuming 'Pellet' by default", balise.text)
                    h.form = model.constants.HOP_FORM_PELLET
            elif 'TIME' == balise.tag :
                h.time = float(balise.text)
            elif 'ALPHA' == balise.tag :
                h.alpha = float(balise.text)
            elif 'USE' == balise.tag:
                if 'Boil' == balise.text :
                    h.use = model.constants.HOP_USE_BOIL
                elif 'Dry Hop' == balise.text or 'Dry Hopping' == balise.text:
                    h.use = model.constants.HOP_USE_DRY_HOP
                elif 'Mash' == balise.text:
                    h.use == model.constants.HOP_USE_MASH
                elif 'First Wort' == balise.text:
                    h.use = model.constants.HOP_USE_FIRST_WORT
                elif 'Aroma' == balise.text:
                    h.use = model.constants.HOP_USE_AROMA
                else :
                    logger.warn ("Unkown hop use '%s', assuming 'Boil' by default", balise.text)
                    h.use = model.constants.HOP_USE_BOIL
        return h