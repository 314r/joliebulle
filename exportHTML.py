
#JolieBulle 2.7
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



import codecs
import PyQt4
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from base import *
from globals import *



  

class ExportHTML(QtGui.QDialog) : 

    def exportHtml (self, nomRecette, styleRecette, volume, boil, nbreFer, liste_ingr, liste_fAmount, liste_fUse, nbreHops,liste_houblons, liste_hAlpha,liste_hForm,liste_hAmount,liste_hTime,liste_hUse,nbreDivers,liste_divers, liste_dType, liste_dAmount, liste_dTime, liste_dUse, nbreLevures, liste_levuresDetail, rendement, OG, FG, ratioBUGU, EBC, IBU, ABV, recipeNotes, currentMash) :
        
        self.recetteHtmlHeader = '''
<!DOCTYPE html>
<html lang="fr">
<head>
<title>''' + nomRecette +'''</title>
<meta charset="utf-8" />
<style type="text/css">
html { font-size:100.01%; }
body {width:800px;margin:auto;line-height: 1.5;color: #222; font-size:80%}
h1,h2,h3,h4,h5,h6 { font-weight: normal; color: #111; }
h1 { font-size: 2em; margin-bottom: 0; text-align:center;}
h2 { font-size: 1.5em; line-height: 1; margin-bottom: 2em; margin-top:2em; padding-bottom:0.75em; padding-top:0.75em;border-bottom:solid 1px #ddd;clear:both;}
h3 { font-size: 1.2em; line-height: 1.25; margin-bottom: 1.25em; text-align:left; background-color:#eeeeee; border-bottom:1px solid #cccccc; border-top:1px solid #cccccc; padding:0.5em 0 0.5em 0.5em;}
ul{list-style-type: none;text-align:left;}
.genre {font-style:italic; text-align:center;color:#ddd;margin-top:0;padding-top:0;border:0;border-bottom:solid 1px #ddd;}
.profil{text-align:left;margin-bottom:1em; width:400px;background:url(/Images/glade.png);}
.profil td {min-width: 200px;}
.ingredients{text-align:left; margin-bottom:2em;}
.ingredients td {min-width: 200px;}

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

#         self.recetteHtmlInfo = self.trUtf8('''
# Recette prévue pour un brassin de ''') + str(volume) + self.trUtf8(''' litres <br/>''')

        grains_texte=self.trUtf8('''<h3>Grains et sucres</h3> ''') + '''<table class="ingredients">'''
        i = 0
        while i < nbreFer :
            i=i+1
            if liste_fUse[i-1] == self.trUtf8('''Après ébullition''') :
                use = self.trUtf8('''Ajout après ébullition''')
            else :
                use = ''
            grains_texte = grains_texte + '''<tr>''' + '''<td>'''+str("%.0f" %(liste_fAmount[i-1])) + '''g''' + '''</td>''' + '''<td>'''+ liste_ingr[i-1]  +  '''</td>''' + '''<td>''' + use +'''</td>''' + '''</tr>'''
        grains_texte=grains_texte + '''</table>'''
          
        houblons_texte=self.trUtf8('''<h3>Houblons</h3> ''') + '''<table class="ingredients">'''
        h = 0
        while h < nbreHops : 
            h = h+1    
            houblons_texte = houblons_texte + '''<tr>''' + '''<td>''' + str("%.0f" %(liste_hAmount[h-1])) + '''g''' + '''</td>''' + '''<td>''' + liste_houblons[h-1]  + ''' (α''' +  str(liste_hAlpha[h-1]) +'''%''' + ''', ''' + liste_hForm[h-1] +''')''' + '''</td>''' + '''<td>''' + str("%.0f" %(liste_hTime[h-1])) + '''min (''' +str(liste_hUse[h-1])  +  ''')'''+  '''</td>'''+ '''</tr>'''
        houblons_texte = houblons_texte + '''</table>'''
        
        divers_texte = self.trUtf8('''<h3>Ingrédients divers</h3> ''')  + '''<table class="ingredients">'''
        m = 0
        while  m < nbreDivers :
            m = m + 1 
            divers_texte = divers_texte +  '''<tr>''' + '''<td>''' +  str("%.0f" %(liste_dAmount[m-1])) + '''g''' + '''</td>'''+ '''<td>''' + liste_divers[m-1] +''' (''' + liste_dType[m-1] +''')''' + '''</td>''' + '''<td>''' + str("%.0f" %(liste_dTime[m-1]))+ '''min ('''+ str(liste_dUse[m-1]) + ''')</td>'''+ '''</tr>'''
            # divers_texte = divers_texte +'''<b>''' + liste_divers[m-1] +'''</b>'''+''' (''' +liste_dType[m-1] +''')''' + ''' : ''' +'''<b>''' +str(liste_dAmount[m-1]) + '''g''' +'''</b>'''+''' pendant ''' + '''<b>''' + str(liste_dTime[m-1]) + '''</b>''' + self.trUtf8(''' minutes''') +'''<br/>'''
        divers_texte = divers_texte + '''</table>'''
        
        levures_texte = self.trUtf8('''<h3>Levures</h3> ''')
        l = 0
        while l < nbreLevures : 
            l = l+1
            levures_texte = levures_texte + liste_levuresDetail[l-1] + '''<br/>'''
        

        self.recetteHtmlIng = self.trUtf8(''' <h2>Ingrédients pour un brassin de ''') + str(volume) + self.trUtf8(''' litres''')+ grains_texte + houblons_texte + divers_texte + levures_texte
        
        
        self.recetteHtmlProfil = ''' <table class="profil">'''+ self.trUtf8('''<tr><td>Rendement</td> ''') + '''<td> ''' + str(rendement) + '''% </td></tr>''' + self.trUtf8('''<tr><td>Densité initiale</td>''') + '''<td> '''  + str("%.3f" %(OG)) + '''</td></tr>''' + self.trUtf8('''<tr><td>Densité finale</td>''') + '''<td>''' + str("%.3f" %(FG)) + '''</td></tr>''' + self.trUtf8('''<tr><td>Teinte</td>''') + '''<td> '''+ str("%.0f" %(EBC)) + ''' EBC </td></tr>'''+ self.trUtf8('''<tr><td>Amertume</td>''') + '''<td> ''' + str("%.0f" %(IBU)) + ''' IBU </td></tr>''' + self.trUtf8('''<tr><td>Ratio BU/GU</td>''') + '''<td>''' + str("%.1f" %(ratioBUGU)) + '''</td></tr>''' + self.trUtf8('''<tr><td>Alcool (vol)</td>''') + '''<td>'''+ str("%.1f" %(ABV)) + ''' % </td></tr>''' + '''</table>'''             

        self.recetteHtmlMashProfile = self.trUtf8(''' <h2>Brassage</h2>''') + '''<p>''' + str(currentMash['name']) + '<br/>' + ''' pH : '''+currentMash['ph']+''' </p> ''' + '''<p>''' + '<b>' + self.trUtf8(''' Etapes : ''') + '</b>' + ''' </p> '''
        dicSteps = currentMash['mashSteps']
        for step in dicSteps:
            stepName = step['name']
            stepType = step['type']
            stepTime = step['stepTime']
            stepTemp = step['stepTemp']
            self.recetteHtmlMashProfile = self.recetteHtmlMashProfile + step['name'] + ' : ' + self.trUtf8(''' palier de type ''')+ stepType + self.trUtf8(''' à ''') + stepTemp +'''°C'''+ self.trUtf8(''' pendant ''')+ stepTime + self.trUtf8(''' minutes ''')+ '''<br/> '''
        self.recetteHtmlMashProfile = self.recetteHtmlMashProfile + '''<p>''' + '<b>' + self.trUtf8(''' Rinçage : ''') + '</b>' + ''' </p> ''' + currentMash['spargeTemp'] + " °C"


        self.recipeNotes = self.trUtf8(''' <h2>Notes</h2>''') + '''<p>''' + str(recipeNotes) + ''' </p> '''

        self.recetteHtmlFooter =self.trUtf8( '''
# <footer class="footer">Une recette générée par JolieBulle, logiciel de brassage libre.</footer>
</body>
</html>''')
                                        
                                        
    def generateHtml(self) :
        self.generatedHtml = self.recetteHtmlHeader + self.recetteHtmlProfil + self.recetteHtmlIng + self.recetteHtmlMashProfile + self.recipeNotes                                      
                                        
                                        
    def enregistrerHtml(self,fileHtml) :
        #self.exportHtml(nomRecette)
        contenuTexte = self.recetteHtmlHeader + self.recetteHtmlProfil + self.recetteHtmlIng + self.recipeNotes 
        if  fileHtml.open(QtCore.QIODevice.WriteOnly) :
            self.stream = QtCore.QTextStream(fileHtml)
            self.stream << contenuTexte
                                     
        else :
            fileHtml.close()
                        
