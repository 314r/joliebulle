#!/usr/bin/python3.1
#­*­coding: utf­8 -­*­



#JolieBulle

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

class Fermentable:
    """"A class for storing Fermentable attributes"""

    def __init__(self):
        self.name = ''
        self.amount = 0.0
        self.type = ''
        self.fyield = 0.0
        self.recommendMash = ''
        self.color = 0.0
        self.useAfterBoil = False

    def __repr__(self):
        return ('fermentable[name="%s", amount=%s, type=%s, yield=%s, recommendMash=%s, color=%s, useAfterBoil=%s]' % 
            (self.name, self.amount, self.type, self.fyield, self.recommendMash, self.color, self.useAfterBoil) )

    @staticmethod
    def parse(element):
        f = Fermentable()
        for balise in element:
            if 'NAME' == balise.tag:
                f.name = balise.text
            elif 'AMOUNT' == balise.tag:
                f.amount = 1000*(float(balise.text))
            elif 'TYPE' == balise.tag:
                if 'Grain' == balise.text:
                    f.type = model.constants.FERMENTABLE_TYPE_GRAIN
                elif 'Sugar' == balise.text:
                    f.type = model.constants.FERMENTABLE_TYPE_SUGAR
                elif 'Extract' == balise.text:
                    f.type = model.constants.FERMENTABLE_TYPE_EXTRACT
                elif 'Dry Extract' == balise.text:
                    f.type = model.constants.FERMENTABLE_TYPE_DRY_EXTRACT
                elif 'Adjunct' == balise.text:
                    f.type = model.constants.FERMENTABLE_TYPE_ADJUNCT
                else:
                    logger.warn ("Unkown fermentable type '%', assuming 'Sugar' by default", balise.text)
                    f.type = model.constants.FERMENTABLE_TYPE_SUGAR
            elif 'YIELD' == balise.tag:
                f.fYield = float(balise.text)
            elif 'RECOMMEND_MASH' == balise.tag:
                f.recommendMash = balise.text
            elif 'COLOR' == balise.tag:
                #ATTENTION ! le format BeerXML utilise des unités SRM ! 
                #srm*1.97 =ebc
                f.color = float(balise.text)*1.97
            elif 'ADD_AFTER_BOIL' == balise.tag:
                if balise.text == 'FALSE' :
                    f.useAfterBoil = False
                elif balise.text == 'TRUE':
                    f.useAfterBoil = True
        #logger.debug(repr(f))
        return f

    def equivSucre(self):
        #division par 1000 et 100 pour passer des g aux kg et parce que le rendement est un pourcentage
        return (self.amount/1000)*(self.fYield/100)