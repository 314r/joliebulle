#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.5
#Copyright (C) 2013-2014 Thomas Gerbet

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


class Element:
    def __init__(self):
        self._name=''

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value if value is not None else '' 

    @classmethod
    def parse(cls, data, parser="beerxml"):
        from helper.recipeImporterRepository import RecipeImporterRepository
        return RecipeImporterRepository[parser][cls](data)