
#JolieBulle 2.4
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



import codecs
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from base import *
from globals import *



  

class ExportHTML(QtGui.QDialog) : 

    def exportHtml (self, nomRecette, styleRecette, volume, boil, nbreFer, liste_ingr, liste_fAmount, nbreHops,liste_houblons, liste_hAlpha,liste_hForm,liste_hAmount,liste_hTime, nbreDivers,liste_divers, liste_dType, liste_dAmount, nbreLevures, liste_levuresDetail, rendement, OG, FG, EBC, IBU, ABV, recipeNotes) :
        
        self.recetteHtmlHeader = '''
<!DOCTYPE html>
<html lang="fr">
<head>
<title>''' + nomRecette +'''</title>
<meta charset="utf-8" />
<style type="text/css">
html { font-size:100.01%; }
body {width:960px;margin:auto;line-height: 1.5;color: #222;text-align:center; font-size:80%}
h1,h2,h3,h4,h5,h6 { font-weight: normal; color: #111; }
h1 { font-size: 2em; margin-bottom: 0; text-align:center;}
h2 { font-size: 1.5em; line-height: 1; margin-bottom: 1em; padding-bottom:0.75em; padding-top:0.75em;border-bottom:solid 1px #ddd; border-top:solid 1px #ddd;}
h3 { font-size: 1.2em; line-height: 1.25; margin-bottom: 1.25em; }
.genre {font-style:italic; text-align:center;color:#ddd;margin-top:0;padding-top:0;border:0;}
.footer { width:700px;
margin:auto; 
margin-top:4em;
margin-bottom:4em;
padding:0.5em;
background-color:#eeeeee;
border-bottom :1px solid #cccccc;
border-top :1px solid #cccccc;
text-align : center;}
</style>
</head>
<body>
<h1>''' + nomRecette + '''</h1>
<h2 class="genre">''' + styleRecette + '''</h2>'''

        self.recetteHtmlInfo = self.trUtf8('''
Recette prévue pour un brassin de ''') + str(volume) + self.trUtf8(''' litres <br/>''')

        grains_texte=self.trUtf8('''<h3>Grains</h3> ''')
        i = 0
        while i < nbreFer :
            i=i+1
            grains_texte = grains_texte + '''<b>'''+ liste_ingr[i-1] + ''' : ''' + '''</b>'''+ str(liste_fAmount[i-1]) + '''g'''+'''<br/>'''
          
        houblons_texte=self.trUtf8('''<h3>Houblons</h3> ''')  
        h = 0
        while h < nbreHops : 
            h = h+1        
            houblons_texte = houblons_texte + '''<b>''' + liste_houblons[h-1] + '''</b>''' +  ''' (''' +  str(liste_hAlpha[h-1]) +'''%''' + ''', ''' + liste_hForm[h-1] +''')''' + ''' : ''' +'''<b>'''+ str(liste_hAmount[h-1]) + '''g'''+'''</b>''' +self.trUtf8(''' pendant ''') +'''<b>''' +str(liste_hTime[h-1]) +'''</b>'''+ self.trUtf8(''' minutes d'ébullition''') + '''<br/>'''
        
        divers_texte = self.trUtf8('''<h3>Ingrédients divers</h3> ''')
        m = 0
        while  m < nbreDivers :
            m = m + 1    
            divers_texte = divers_texte +'''<b>''' +liste_divers[m-1] +'''</b>'''+''' (''' +liste_dType[m-1] +''')''' + ''' : ''' +'''<b>''' +str(liste_dAmount[m-1]) + '''g''' +'''</b>'''+'''<br/>'''
        
        levures_texte = self.trUtf8('''<h3>Levures</h3> ''')
        l = 0
        while l < nbreLevures : 
            l = l+1
            levures_texte = levures_texte + liste_levuresDetail[l-1] + '''<br/>'''
        

        self.recetteHtmlIng = self.trUtf8(''' <h2>Ingrédients</h2>''') + grains_texte + houblons_texte + divers_texte + levures_texte
        
        
        self.recetteHtmlProfil = self.trUtf8(''' <h2>Profil</h2>''') + self.trUtf8(''' <p><b>Rendement : </b>''') + str(rendement) + '''% <br/>''' + self.trUtf8('''<b>Densité initiale : </b>''') + str("%.3f" %(OG)) + '''<br/>''' + self.trUtf8('''<b>Densité finale : </b>''') + str("%.3f" %(FG)) + '''<br/>'''+ self.trUtf8('''<b>Teinte : </b>''') + str("%.0f" %(EBC)) + ''' EBC<br/>'''+ self.trUtf8('''<b>Amertume : </b>''') + str("%.0f" %(IBU)) + ''' IBU<br/>''' + self.trUtf8(''' <b>Alcool (vol): </b>''') + str("%.0f" %(ABV)) + ''' %</p>'''              

        self.recipeNotes = self.trUtf8(''' <h2>Notes</h2>''') + '''<p>''' + recipeNotes + ''' </p> '''

        self.recetteHtmlFooter =self.trUtf8( '''
<footer class="footer">Une recette générée par JolieBulle, logiciel de brassage libre.</footer>
</body>
</html>''')
                                        
                                        
                                        
                                        
                                        
    def enregistrerHtml(self,fileHtml) :
        #self.exportHtml(nomRecette)
        contenuTexte = self.recetteHtmlHeader + self.recetteHtmlInfo + self.recetteHtmlIng + self.recetteHtmlProfil + self.recipeNotes + self.recetteHtmlFooter
        if  fileHtml.open(QtCore.QIODevice.WriteOnly) :
            self.stream = QtCore.QTextStream(fileHtml)
            self.stream << contenuTexte
                                     
        else :
            fileHtml.close()
                        
