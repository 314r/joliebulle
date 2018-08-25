#!/usr/bin/python3
#­*­coding: utf­8 -­*­

#joliebulle 3.7
#Copyright (C) 2010-2018 Pierre Tavares
#Copyright (C) 2012-2018 joliebulle's authors
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
import time

import shutil
import os
import os.path
import glob
import logging
import logging.config
from sys import platform
import PyQt5
import sys
from PyQt5 import QtWebKit
from PyQt5 import QtWebKitWidgets
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtPrintSupport
from reader_ui import *
from settings import *
from about import *
from base import *
from editgrain import *
from edithoublon import *
from editdivers import *
from editlevures import *
from helper.toolExporterRepository import *
from helper.libExporterRepository import *
from helper.brewdayExporterRepository import *
from importIng import *
from preBoilDialog import *
from stepEditWindow import *
from mashEditWindow import *
from mashDetail import *
from exportMash import *
from preferences import *
from home import *
from globals import *
#from ui.MainWindow import *

import xml.etree.ElementTree as ET
from model.recipe import *
from model.journal import *
from model.hop import *
from model import recipe
import model.constants
import view.constants
from view.fermentableview import *
from view.recipeview import *
from view.hopview import *
from view.yeastview import *
from view.mashstepview import *
import view.base
import itertools
from errors import *



def initLogging():
    home = QtCore.QDir(home_dir)
    config = QtCore.QDir(config_dir)
    if not config.exists() :
        home.mkpath (config_dir)
    config = {
        'version': 1,
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s]: %(message)s'
            },
            'detailed': {
                'format': '%(asctime)s %(module)-17s line:%(lineno)-4d %(levelname)-8s %(message)s'
            }
        },
        'handlers': {
            'console': {
                'level':'DEBUG',
                'class':'logging.StreamHandler',
                'stream':'ext://sys.stdout',
                'formatter':'standard'
            },
        }
    }
    logging.config.dictConfig(config)


class AppWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)




######################################################################################
######################################################################################
        self.settings = Settings()
        self.initRep()
        self.dlgEditG = Dialog(self)
        self.dlgEditH = DialogH(self)
        self.dlgEditD = DialogD(self)
        self.dlgEditY = DialogL(self)
        self.dlgPref = DialogPref(self)
        self.dlgStep = DialogStep(self)
        self.dlgMash = DialogMash(self)



        self.base = ImportBase()
        self.mashProfileExport = ExportMash()


#        self.base.importBeerXML()
        self.s=0
        self.recipe = None


        #Les connexions
        self.actionEnregistrer.triggered.connect(self.enregistrer)
        self.actionQuitter.triggered.connect(app.quit)
#        self.connect(self.actionQuitter, QtCore.SIGNAL("triggered()"), app, QtCore.SLOT("quit()"))

        self.actionShowJournal.triggered.connect(self.showJournal)


        self.actionEditGrains.triggered.connect(self.editGrains)
        self.actionEditHoublons.triggered.connect(self.editHoublons)
        self.actionEditDivers.triggered.connect(self.editDivers)
        self.actionEditLevures.triggered.connect(self.editLevures)
        self.actionRestaurerIngredients.triggered.connect(self.restoreDataBase)
        self.actionImportIng.triggered.connect(self.importIng)
        self.actionManageProfiles.triggered.connect(self.seeMash)

        self.actionAbout.triggered.connect(self.about)

        self.actionAllTools.triggered.connect(self.showTools)

        self.actionPreferences.triggered.connect(self.dialogPreferences)



        #######################################################################################################
        # Profil de brassage       #########################################################################################################


        self.listWidgetSteps.itemSelectionChanged.connect (self.stepDetails)
        self.listWidgetMashProfiles.itemSelectionChanged.connect (self.mashClicked)
        self.buttonBoxMashDetails.rejected.connect(self.mashRejected)
#        self.comboBoxStepType.addItems(["Infusion", "Température", "Décoction"])
        self.pushButtonStepEdit.clicked.connect(self.stepEdit)
        self.dlgStep.stepChanged.connect(self.stepReload)
        self.pushButtonStepRemove.clicked.connect(self.removeStep)
        self.pushButtonNewStep.clicked.connect(self.addStep)
        self.pushButtonMashEdit.clicked.connect(self.mashEdit)
        self.dlgMash.mashChanged.connect(self.mashReload)
        self.pushButtonNewProfile.clicked.connect(self.addMash)
        self.pushButtonRemoveProfile.clicked.connect(self.removeMash)
        self.pushButtonSaveProfile.clicked.connect(self.saveProfile)

        #La bibliotheque
        ###################################################################################################################
        ###################################################################################################################


        # self.listdir(recettes_dir)
        self.showLib()

###################################################################################################
######## gestion des arguments au lancement du programme  #########################################


        argumentsList=QtWidgets.QApplication.arguments()
        if len(argumentsList) > 1 :
            logger.debug("la liste d'arguments: %s",argumentsList)
            logger.debug("le chemin: %s",argumentsList[1])
            # for part in argumentsList :
            #     recipePath=recipePath + " " + part
            try:
                recipePath= argumentsList[1]
                for part in argumentsList[2:] :
                    recipePath= recipePath +" " + part

                self.openRecipeFile(recipePath)
            except :
                pass
        else:
            pass

########################################################################################################################
####################################################################################################################
# le signal émit à la fermeture de la fenêtre de préférences
        self.dlgPref.prefAccepted.connect(self.prefReload)



###########################################################
############### Journal ##############################
######################################################

    def loadJournal(self):
        self.journal=Journal()
        self.journal.loadJournal()
        # self.actionEditJournal.setEnabled(True)

    @QtCore.pyqtSlot()
    def showJournal(self,entry=" '' ") :
        self.stackedWidget.setCurrentIndex(0)
        self.loadJournal()
        pyDir = os.path.abspath(os.path.dirname(__file__))
        baseUrl = QtCore.QUrl.fromLocalFile(os.path.join(pyDir, "static/"))
        self.webViewBiblio.setHtml(self.journal.export("html",entry), baseUrl)
        self.webViewBiblio.page().mainFrame().addToJavaScriptWindowObject("main", self)
        # self.webViewBiblio.page().settings().setAttribute(QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)
        # self.webInspector = QtWebKit.QWebInspector(self)
        # self.webInspector.setPage(self.webViewBiblio.page())
        # self.webInspector.setVisible(True)
        # self.verticalLayout_13.addWidget(self.webInspector)


    @QtCore.pyqtSlot(str, str)
    def addToJournal(self,event, recipeName) :
        self.loadJournal()
        entry = '''{recipe:%s,date:%s,event:%s,editing:'True'} ''' %( "'" + recipeName + "'", "'" + str(int(time.time())) + "'" , "'" + self.journal.eventsLabels[event] + "'")
        self.showJournal(entry)


    @QtCore.pyqtSlot(str)
    def dumpJournal(self,journalJson) :
        journalJson= '{"name":"journal","items": %s }' %journalJson
        d=json.loads(journalJson)
        with open(journal_file, mode="w", encoding="utf-8") as f :
            json.dump(d,f,indent=2)



############## Bibliothèque ##############################
##########################################################
    @QtCore.pyqtSlot()
    def showLib(self) :
        # data = json.dumps(self.recipesSummary)
        # data = data.replace("'","&#39;")
        self.stackedWidget.setCurrentIndex(0)
        self.brewdayLock = 0

        self.webSettings = self.webViewBiblio.settings()
        self.webSettings.setAttribute(QtWebKit.QWebSettings.LocalContentCanAccessRemoteUrls, True)

        pyDir = os.path.abspath(os.path.dirname(__file__))
        baseUrl = QtCore.QUrl.fromLocalFile(os.path.join(pyDir, "static/html/"))
        self.webViewBiblio.setHtml(LibExporterRepository['html'](), baseUrl)
        self.webViewBiblio.page().mainFrame().addToJavaScriptWindowObject("main", self)
        self.webViewBiblio.page().settings().setAttribute(QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)
        self.webViewBiblio.page().action(QtWebKitWidgets.QWebPage.Reload).setVisible(False)


    @QtCore.pyqtSlot(str)
    def deleteLib(self,path) :
        confirmation = QtWidgets.QMessageBox.question(self,
                            self.tr("Supprimer"),
                            self.tr("La recette sera définitivement supprimée <br/> Continuer ?"),
                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if (confirmation == QtWidgets.QMessageBox.Yes):
            os.remove(path)
            self.listdir(recettes_dir)
            self.showLib()
        else :
            self.showLib()


    @QtCore.pyqtSlot()
    def backWebViewBiblio(self) :
        self.stackedWidget.setCurrentIndex(0)


    @QtCore.pyqtSlot(str, str)
    def saveRecipe(self, recipe, path) :
        # if not path :
        #     path = recettes_dir + "/" + str(int(time.time())) + ".xml"
        print(path)
        recipeFile = QtCore.QFile(path)
        if recipeFile.open(QtCore.QIODevice.WriteOnly):
            try:
                stream = QtCore.QTextStream(recipeFile)
                stream.setCodec("UTF-8")
                stream << recipe
            finally:
                recipeFile.close()
        else:
            # TODO : Prévenir l'utilisateur en cas d'échec de l'enregistrement
            pass

    @QtCore.pyqtSlot(result=str)
    def createPath(self) :
        path = recettes_dir + "/" + str(int(time.time()*10)) + ".xml"
        print (path)
        return path

    @QtCore.pyqtSlot()
    def resetLock(self):
        self.brewdayLock = 0;




############# Mode Brassage ################################
############################################################

    @QtCore.pyqtSlot(str)
    def showBrewdayMode(self, data):
        if self.brewdayLock == 0 :
            self.stackedWidget.setCurrentIndex(1)
            self.brewdayLock = 1
            data = data.replace("'","&#39;")
            pyDir = os.path.abspath(os.path.dirname(__file__))
            baseUrl = QtCore.QUrl.fromLocalFile(os.path.join(pyDir, "static/"))
            self.webViewBrewday.setHtml(BrewdayExporterRepository['html'](data), baseUrl)
            self.webViewBrewday.page().mainFrame().addToJavaScriptWindowObject("main", self)
            self.webViewBrewday.page().settings().setAttribute(QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)
            self.webViewBrewday.page().action(QtWebKitWidgets.QWebPage.Reload).setVisible(False)
        else :
            self.stackedWidget.setCurrentIndex(1)





###### Outils ############################################
##########################################################

    @QtCore.pyqtSlot()
    def showTools(self):
        self.stackedWidget.setCurrentIndex(0)
        pyDir = os.path.abspath(os.path.dirname(__file__))
        baseUrl = QtCore.QUrl.fromLocalFile(os.path.join(pyDir, "static/"))
        self.webViewBiblio.setHtml(ToolExporterRepository["html"](), baseUrl)
        self.webViewBiblio.page().mainFrame().addToJavaScriptWindowObject("main", self)
        # self.webViewBiblio.page().settings().setAttribute(QtWebKit.QWebSettings.DeveloperExtrasEnabled, True)
        # self.webInspector = QtWebKit.QWebInspector(self)
        # self.webInspector.setPage(self.webViewBiblio.page())
        # self.webInspector.setVisible(True)
        # self.verticalLayout_13.addWidget(self.webInspector)



    @QtCore.pyqtSlot(result=str)
    def dataRecipes(self) :
        # f = open(recipeData_file, 'w')
        # f.write(self.recipesSummary)
        self.listdir(recettes_dir)
        return self.recipesSummary

    @QtCore.pyqtSlot(result=str)
    def dataProfiles(self) :
        return self.mashProfileExport.exportJson(ImportBase().listeMashes)


    @QtCore.pyqtSlot(result=str)
    def dataIngredients(self) :
        return ImportBase().exportjson()


    @QtCore.pyqtSlot(result=str)
    def dataPref(self) :
        dic = {}
        dic["boilOffRate"] = settings.conf.value("BoilOffRate")
        dic["coolingLossRate"] = settings.conf.value("CoolingLoss")
        dic["grainTemp"] = settings.conf.value("GrainTemp")
        dic["fudgeFactor"] = settings.conf.value("FudgeFactor")
        dic["grainRetention"] = settings.conf.value("GrainRetention")
        dic = json.dumps(dic)
        return dic











    #Une fonction qui gère l'aperçu des couleurs.
    #Contient un tupple avec plusieurs références de couleurs, classées par rang selon la valeur SRM.
    #################################################################################################
    # def colorPreview (self) :
    #     self.colorTuppleSrm = ('FFE699', 'FFD878', 'FFCA5A', 'FFBF42', 'FBB123', 'F8A600', 'F39C00', 'EA8F00', 'E58500', 'DE7C00', 'D77200', 'CF6900', 'CB6200', 'C35900','BB5100', 'B54C00', 'B04500', 'A63E00', 'A13700', '9B3200', '952D00', '8E2900', '882300', '821E00', '7B1A00', '771900', '701400', '6A0E00', '660D00','5E0B00','5A0A02','600903', '520907', '4C0505', '470606', '440607', '3F0708', '3B0607', '3A070B', '36080A')

    #     colorRef= round(self.recipe.compute_EBC()/1.97)

    #     if colorRef >= 30 :
    #         color = "#" + self.colorTuppleSrm[30]
    #     elif colorRef <= 1 :
    #         color = "#" + self.colorTuppleSrm[0]
    #     else :
    #         color = "#" + self.colorTuppleSrm[colorRef-1]
    #     self.widgetColor.setStyleSheet("background-color :" + color)



    def listdir(self, rootdir) :
        self.recipesSummary="["
        fileList=[]
        filenameList=[]
        for root, subFolders, files in os.walk(rootdir):
            for file2 in files:
                fileList.append(os.path.join(root,file2))
                filenameList.append(file2)

        #on parse
        j=0
        while j < len(filenameList) :
            j=j+1
            recipe = fileList[j-1]
            try :
                self.recipesSummary += str (self.jsonRecipeLib(recipe))
                if j < len(filenameList) :
                    self.recipesSummary += ","
            except :
                logger.debug("le fichier %s n'est pas une recette" %(recipe))

        self.recipesSummary += "]"
        logger.debug("%s fichiers détectés" %(len(filenameList)))






    def jsonRecipeLib(self,recipe) :
        self.s = recipe
        self.recipe = Recipe.parse(recipe)
        data = self.recipe.export("json")
        data = data[1:-1]
        return data



    def initRep(self) :
        home = QtCore.QDir(home_dir)
        config = QtCore.QDir(config_dir)
        logger.debug (config)
        if not config.exists() :
            home.mkpath (config_dir)
        else :
            pass
        database = QtCore.QFile(database_file)
        if not database.exists() :
            database.copy(database_root, database_file)
        else :
            pass
        recettes = QtCore.QFile(recettes_dir)
        if not recettes.exists() :
            try :
                shutil.copytree(samples_dir, samples_target)
            except :
                home.mkpath(recettes_dir)
        mash  = QtCore.QFile(mash_file)
        if not mash.exists() :
            mash.copy(mash_root, mash_file)
        else :
            pass
        journal  = QtCore.QFile(journal_file)
        if not journal.exists() :
            journal.copy(journal_root, journal_file)
        else :
            pass

        # on configure des valeurs par défaut
        if not settings.conf.contains("BoilOffRate") :
            settings.conf.setValue("BoilOffRate", 10)
        if not settings.conf.contains("CoolingLoss") :
            settings.conf.setValue("CoolingLoss", 5)
        if not settings.conf.contains("GrainTemp") :
            settings.conf.setValue("GrainTemp", 20)
        if not settings.conf.contains("FudgeFactor") :
            settings.conf.setValue("FudgeFactor", 1.7)
        if not settings.conf.contains("GrainRetention") :
            settings.conf.setValue("GrainRetention", 1)
        if not settings.conf.contains("Menus") :
            settings.conf.setValue("Menus", "button")


    def prefReload(self) :
        if platform == 'win32':
            recettes_dir = settings.conf.value("pathWin32")
        else :
            recettes_dir = settings.conf.value("pathUnix")
        self.initRep()
        self.listdir(recettes_dir)
        self.showLib()


    @QtCore.pyqtSlot()
    def switchToLibrary(self) :
        self.stackedWidget.setCurrentIndex(0)
        # self.viewRecipeLib(self.s)

    def switchToMash(self) :
        self.stackedWidget.setCurrentIndex(2)


    def restoreDataBase(self) :
        home = QtCore.QDir(home_dir)
        config = QtCore.QDir(config_dir)
        database = QtCore.QFile(database_file)
        confirmation = QtWidgets.QMessageBox.question(self,
                                    self.tr("Remplacer la base ?"),
                                    self.tr("La base des ingrédients actuelle va être effacée et remplacée par la base originale. Toutes vos modifications vont être effacées. Un redémarrage de l'application sera nécessaire.<br> Continuer ?"),
                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if (confirmation == QtWidgets.QMessageBox.Yes):
            database.remove(database_file)
            database.copy(database_root, database_file)
        else :

            pass


    def editGrains(self) :
        self.dlgEditG.setModal(True)
        self.dlgEditG.setModel()
        self.dlgEditG.show()

    def editHoublons(self) :
        self.dlgEditH.setModal(True)
        self.dlgEditH.setModel()
        self.dlgEditH.show()

    def editDivers(self) :
        self.dlgEditD.setModal(True)
        self.dlgEditD.setModel()
        self.dlgEditD.show()

    def editLevures(self) :
        self.dlgEditY.setModal(True)
        self.dlgEditY.setModel()
        self.dlgEditY.show()

    @QtCore.pyqtSlot(float, float, float, float)
    def preBoilCheck(self,volPreBoil,preBoilSg,GU,volume) :
        self.dlgPreBoil = DialogPreBoil(self)
        self.dlgPreBoil.setData(volPreBoil,preBoilSg,GU,volume)
        self.dlgPreBoil.setModal(True)
        self.dlgPreBoil.show()


    def dialogPreferences (self) :
        self.dlgPref.setModal(True)
        self.dlgPref.show()




    def importBeerXML(self) :
        fichierBeerXML = self.s
        try:
            self.recipe = Recipe.parse(fichierBeerXML)
            self.currentRecipeMash = self.recipe.mash

        except :
            errors = Errors()
            errors.warningXml()


    def about(self) :
        about = DialogAbout(self)
        about.show()


    def enregistrerRecette(self, destination):
        recipeFile = QtCore.QFile(destination)
        if recipeFile.open(QtCore.QIODevice.WriteOnly):
            try:
                stream = QtCore.QTextStream(recipeFile)
                stream.setCodec("UTF-8")
                stream << self.recipe.export("beerxml")
            finally:
                recipeFile.close()
        else:
            # TODO : Prévenir l'utilisateur en cas d'échec de l'enregistrement
            pass
        self.fileSaved = True


    def enregistrer (self) :
        if self.recipe.name != self.lineEditRecette.text() :
            self.nameChanged = True
        else :
            self.nameChanged = False

        self.recipe.name = self.lineEditRecette.text()
        self.recipe.style = self.lineEditGenre.text()
        self.recipe.brewer = self.lineEditBrewer.text()
        self.recipe.boil = self.spinBoxBoil.value()
        if not self.s:
            destination = recettes_dir + "/" + self.recipe.name.replace('/', ' ') + ".xml"
            if os.path.exists(destination) :
                errors=Errors()
                errors.warningExistingPath()
                self.fileSaved = False
            else :
                self.s = destination
                self.enregistrerRecette(destination)
        else :
            self.enregistrerRecette(self.s)




    def enregistrerSous (self) :
        self.s = QtGui.QFileDialog.getSaveFileName (self,
                                                    self.tr("Enregistrer dans un fichier"),
                                                    recettes_dir + "/" + self.recipe.name.replace('/', ' ') + ".xml",
                                                    "BeerXML (*.xml)")
        self.enregistrerRecette(self.s)

    @QtCore.pyqtSlot(str)
    def copyBbcode (self, bbcode):
        app.clipboard().setText(bbcode)


    def importIng(self):
        s = QtWidgets.QFileDialog.getOpenFileName(self,
            self.tr("Ouvrir un fichier"),
            home_dir,
            )
        if not s :
            pass
        else :
            self.importIngList = ImportIng()
            self.importIngList.parseFile(s)


    def mashComboChanged (self) :
        #on remet le verrou à 0, il va falloir recalculer en repassant en brewday mode
        self.brewdayLock = 0
        try :
            i =self.comboBoxMashProfiles.currentIndex()
            self.currentMash = ImportBase().listeMashes[i]
        except :
            self.currentMash = self.currentRecipeMash
        if i == -1 :
            self.currentMash = Mash()
        self.recipe.mash = self.currentMash

    def seeMash(self) :
        self.switchToMash()
        index = self.listWidgetMashProfiles.currentRow()
        i = self.listWidgetSteps.currentRow()
        self.listWidgetMashProfiles.clear()
        self.listWidgetSteps.clear()

        self.numMash = len(ImportBase().listeMashes)
        #self.numSteps = self.mashProfilesBase.numSteps
        self.popMashList()
        self.pushButtonMashEdit.setEnabled(False)
        self.pushButtonRemoveProfile.setEnabled(False)
        self.pushButtonStepRemove.setEnabled(False)
        self.pushButtonStepEdit.setEnabled(False)
        self.listWidgetMashProfiles.setCurrentRow(index)
        self.listWidgetSteps.setCurrentRow(i)

    def popMashList(self) :
        self.listWidgetMashProfiles.clear()
        for mash in ImportBase().listeMashes :
           self.listWidgetMashProfiles.addItem(mash.name)

    def mashClicked(self) :
        self.listWidgetSteps.clear()
        index = self.listWidgetMashProfiles.currentRow()
        if index > -1:
            mash = ImportBase().listeMashes[index]
            for step in mash.listeSteps :
                self.listWidgetSteps.addItem(step.name)

            self.labelStepName.setTextFormat(QtCore.Qt.RichText)
            self.labelMashName.setText("<b>" + mash.name + "</b>")
            self.labelMashPh.setText("%.1f" %float(mash.ph))
    #        self.labelMashGrainTemp.setText("%.1f" %float(self.dicMashDetail['grainTemp']))
    #        self.labelMashTunTemp.setText("%.1f" %float(self.dicMashDetail['tunTemp']))
            try :
                self.labelMashSpargeTemp.setText("%.1f" %float(mash.spargeTemp))
            except :
                pass
            try :
                self.listWidgetSteps.setCurrentRow(0)
            except :
                pass
    #        print(self.dicMashDetail)
            self.pushButtonMashEdit.setEnabled(True)
            self.pushButtonRemoveProfile.setEnabled(True)

    def mashDetails(self) :
        self.dlgMashDetail = DialogMashDetail(self)
        self.dlgMashDetail.setModal(True)
        self.dlgMashDetail.show()
        self.dlgMashDetail.setFields(self.currentMash)
        self.dlgMashDetail.setAttribute( QtCore.Qt.WA_DeleteOnClose, True )


    def stepDetails(self) :
        index = self.listWidgetMashProfiles.currentRow()
        if index > -1:
            selected_mash = ImportBase().listeMashes[index]
            i = self.listWidgetSteps.currentRow()
            if i > -1:
                try:
                    selected_step = selected_mash.listeSteps[i]
                    self.labelStepName.setTextFormat(QtCore.Qt.RichText)
                    self.labelStepName.setText("<b>" + selected_step.name +"</b>")
                    self.labelStepType.setText(selected_step.type)
                    self.labelStepTemp.setText(MashStepView.temp_to_display(selected_step.temp))
                    self.labelStepTime.setText(MashStepView.time_to_display(selected_step.time))
                    self.pushButtonStepRemove.setEnabled(True)
                    self.pushButtonStepEdit.setEnabled(True)
                except:
                    pass


    def stepEdit(self) :
        index = self.listWidgetMashProfiles.currentRow()
        if  index > -1:
            selected_mash = ImportBase().listeMashes[index]
            i = self.listWidgetSteps.currentRow()
            if i > -1:
                selected_step = selected_mash.listeSteps[i]

                self.dlgStep.show()
                self.dlgStep.fields (selected_step)

    def stepReload(self, step) :
        index = self.listWidgetMashProfiles.currentRow()
        if index > -1:
            selected_mash = ImportBase().listeMashes[index]
            i = self.listWidgetSteps.currentRow()
            if i > -1:
                selected_step = selected_mash.listeSteps[i]

                selected_step.name = step.name
                selected_step.type = step.type
                selected_step.temp = step.temp
                selected_step.time = step.time
                self.seeMash()
                self.stepDetails()
                self.listWidgetMashProfiles.setCurrentRow(index)
                self.listWidgetSteps.setCurrentRow(i)

    def removeStep(self) :
        index = self.listWidgetMashProfiles.currentRow()
        if index > -1:
            selected_mash = ImportBase().listeMashes[index]
            i = self.listWidgetSteps.currentRow()
            if i > -1:
                item = self.listWidgetSteps.currentItem()
                del selected_mash.listeSteps[i]
                # self.listWidgetSteps.clearSelection()
                #self.listWidgetSteps.takeItem(item)
                #On force la sélection sur la ligne précédente
                self.listWidgetSteps.setCurrentRow(i-1)
                self.seeMash()

    def addStep(self) :
        index = self.listWidgetMashProfiles.currentRow()
        selected_mash = ImportBase().listeMashes[index]
        i = self.listWidgetSteps.currentRow()
        step = MashStep()
        step.name = 'Nouveau palier'
        step.type = 'Infusion'
        step.time = '0'
        step.temp = '0'
        step.vol = '0'
        selected_mash.listeSteps.append(step)

        self.listWidgetMashProfiles.setCurrentRow(index)
        self.seeMash()
        self.stepDetails()
        self.listWidgetMashProfiles.setCurrentRow(index)
        # self.listWidgetSteps.setCurrentRow(i-1)
        # self.stepEdit()

    def mashEdit(self) :
        index = self.listWidgetMashProfiles.currentRow()
        selected_mash = ImportBase().listeMashes[index]
        self.dlgMash.show()
        self.dlgMash.fields(selected_mash)

    def mashReload(self,mash) :
        #on remet le verrou à 0, il va falloir recalculer en repassant en brewday mode
        self.brewdayLock = 0
        f = self.listWidgetMashProfiles.currentRow()
        selected_mash = ImportBase().listeMashes[f]
        selected_mash.name = mash.name
        selected_mash.ph = mash.ph
        selected_mash.grainTemp = 20
        selected_mash.tunTemp = 20
        selected_mash.spargeTemp = mash.spargeTemp
        self.popMashList()
        self.listWidgetMashProfiles.setCurrentRow(f)

    def addMash(self) :
        new_mash = Mash()
        new_mash.name = 'Nouveau profil'
        new_mash.grainTemp = '0'
        new_mash.tunTemp = '0'
        new_mash.spargeTemp = '78'
        new_mash.ph = 5.4
        new_step = MashStep()
        new_step.name = 'Nouveau Palier'
        new_step.type = 'Infusion'
        new_step.time = '0'
        new_step.temp = '0'
        new_mash.listeSteps.append(new_step)
        ImportBase().listeMashes.append(new_mash)
        self.seeMash()
        self.listWidgetMashProfiles.setCurrentRow(len(ImportBase().listeMashes)-1)

    def removeMash(self) :
        i = self.listWidgetMashProfiles.currentRow()
        del ImportBase().listeMashes[i]
        self.seeMash()
        self.listWidgetSteps.clear()

    def mashRejected (self) :
        self.showLib()

    def saveProfile(self) :
        self.mashProfileExport.export(ImportBase().listeMashes)
        self.mashProfileExport.enregistrer(mash_file)

    @QtCore.pyqtSlot()
    def printRecipe (self) :
        printer=QtPrintSupport.QPrinter()
        dialog = QtPrintSupport.QPrintDialog(printer)
        dialog.setModal(True)
        dialog.setWindowTitle("Print Document" )
        if dialog.exec_() == True:
            self.webViewBiblio.print(printer)
            # document=QtGui.QTextDocument()
            # stringHtml=self.recipe.export("print")
            # document.setHtml(stringHtml)
            # document.print(printer)


    @QtCore.pyqtSlot()
    def printBrewday(self) :
        printer=QtPrintSupport.QPrinter()
        dialog = QtPrintSupport.QPrintDialog(printer)
        dialog.setModal(True)
        dialog.setWindowTitle("Print Document" )
        if dialog.exec_() == True:
            self.webViewBrewday.print(printer)
            # document = self.webViewBrewday.page().currentFrame().toHtml()
            # document.print(printer)



if __name__ == "__main__":

    initLogging()

    logger = logging.getLogger(__name__)

    logger.debug("Initializing UI");
    QtCore.QTextCodec.setCodecForLocale(QtCore.QTextCodec.codecForName("utf-8"))
    app = QtWidgets.QApplication(sys.argv)

    locale = QtCore.QLocale.system().name()
    translator=QtCore.QTranslator ()
    translator.load('joliebulle_' + locale)
    app.installTranslator(translator)

    translatorQt = QtCore.QTranslator ()
    translatorQt.load('qt_' + locale)
    app.installTranslator(translatorQt)

    main_window = AppWindow()
    #main_window = MainWindow()
    # main_window.show()
    main_window.showMaximized()

    logger.debug("UI initialized");

    app.exec_()
