
#JolieBulle 2.15
#Copyright (C) 2010-2011 Pierre Tavares

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




import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore



  

class ExportHTML : 

    def exportHtml (self, nomRecette, styleRecette, volume, boil, nbreFer, liste_ingr, liste_fAmount, nbreHops,liste_houblons, liste_hAlpha,liste_hForm,liste_hAmount,liste_hTime, nbreDivers,liste_divers, liste_dType, liste_dAmount) :
        
        self.recetteHtmlHeader = '''
<!DOCTYPE html>
<html lang="fr">
<head>
<title>''' + nomRecette +'''</title>
<meta charset="utf-8" />
</head>
<body>
<h1>''' + nomRecette + '''</h1>
<h2>''' + styleRecette + '''</h2>'''

        self.recetteHtmlInfo = '''
Recette prévue pour un brassin de ''' + boil +''' litres <br/>
Durée d'ébullition : ''' + boil + ''' minutes <br/>'''
        grains_texte=''' '''
        i = 0
        while i < nbreFer :
            i=i+1
            grains_texte = grains_texte + '''<b>'''+ liste_ingr[i-1] + ''' : ''' + '''</b>'''+ str(liste_fAmount[i-1]) + '''g'''+'''<br/>'''
          
        houblons_texte=''' '''  
        h = 0
        while h < nbreHops : 
            h = h+1        
            houblons_texte = houblons_texte + '''<b>''' + liste_houblons[h-1] + '''</b>''' +  ''' (''' +  str(liste_hAlpha[h-1]) +'''%''' + ''', ''' + liste_hForm[h-1] +''')''' + ''' : ''' +'''<b>'''+ str(liste_hAmount[h-1]) + '''g'''+'''</b>''' +''' pendant ''' +'''<b>''' +str(liste_hTime[h-1]) +'''</b>'''+ ''' minutes''' + '''<br/>'''
        
        divers_texte = ''' '''
        m = 0
        while  m < nbreDivers :
            m = m + 1    
            divers_texte = divers_texte +'''<b>''' +liste_divers[m-1] +'''</b>'''+''' (''' +liste_dType[m-1] +''')''' + ''' : ''' +'''<b>''' +str(liste_dAmount[m-1]) + '''g''' +'''</b>'''+'''<br/>'''
           
        

        self.ing = grains_texte + houblons_texte + divers_texte


                                        
                                        
                                        
                                        
                                        
                                        
    def enregistrerHtml(self,fileHtml) :
        #self.exportHtml(nomRecette)
        contenuTexte = self.recetteHtmlHeader + self.recetteHtmlInfo + self.ing
        if  fileHtml.open(QtCore.QIODevice.WriteOnly) :
            self.stream = QtCore.QTextStream(fileHtml)
            self.stream << contenuTexte
                                        
        else :
            fileHtml.close()
                        