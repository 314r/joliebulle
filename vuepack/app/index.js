'use strict'
const electron = require('electron')
// Module to control application life.
const app = electron.app
// Module to create native browser window.
const BrowserWindow = electron.BrowserWindow
const os = require('os')
const fs = require('fs')
const ini = require('ini')
const path = require('path')
// const url = require('url')
const ipcMain = require('electron').ipcMain
// const dialog = electron.dialog
const XML = require('pixl-xml')

// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
let mainWindow

const isDev = process.env.NODE_ENV === 'development'

let config

if (isDev) {
  config = require('../build/config')
} else {
  config = {}
}

function createWindow () {
  // Create the browser window.
  mainWindow = new BrowserWindow({ width: 900, height: 750 })
  mainWindow.setMenu(null)

  // and load the index.html of the app.
  const url = isDev ? `http://${config.devServer.host}:${config.devServer.port}` : `file://${__dirname}/dist/index.html`
  mainWindow.loadURL(url)

  // Open the DevTools.
  if (isDev) {
    mainWindow.webContents.openDevTools()

    const installExtension = require('electron-devtools-installer')
    installExtension.default(installExtension.VUEJS_DEVTOOLS)
      .then(name => console.log(`Added Extension:  ${name}`))
      .catch(err => console.log('An error occurred: ', err))
  }

  // Emitted when the window is closed.
  mainWindow.on('closed', () => {
    // Dereference the window object, usually you would store windows
    // in an array if your app supports multi windows, this is the time
    // when you should delete the corresponding element.
    mainWindow = null
  })
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', () => {
  if (process.env.NODE_ENV !== 'production') {
    require('vue-devtools').install()
  }
//  use .uninstall to uninstall
  createWindow()
})

// Quit when all windows are closed.
app.on('window-all-closed', () => {
  // On OS X it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (mainWindow === null) {
    createWindow()
  }
})

// In this file you can include the rest of your app's specific main process
// code. You can also put them in separate files and require them here.

function walkRecipes (dir) {
  return fs.readdirSync(dir).reduce(function (list, file) {
    var name = path.join(dir, file)
    var isDir = fs.statSync(name).isDirectory()
    return list.concat(isDir ? walkRecipes(name) : [name])
  }, [])
}

function parseAll (f, dirStorage) {
//    First we need a list of paths. f is the function used to read each directory inside dirStorage.
  var listFiles = f(dirStorage)
  return listFiles.reduce(function (list, filePath) {
    var recipeObject = parseFile(filePath)
    if (typeof recipeObject !== 'undefined') {
      recipeObject.path = filePath
      return list.concat([recipeObject])
    } else {
      return list
    }
  }, [])
}

function parseFile (filePath) {
  const rawXml = fs.readFileSync(filePath, 'utf8')
  try {
    const rawObject = XML.parse(rawXml, { lowerCase: true }).recipe
    return rawObject
  } catch (err) {
    console.log('XML parser error : ' + err)
  }
}

function recipesList (recipesDir) {
  // parse all recipes recursively
  const recipes = parseAll(walkRecipes, recipesDir)

  // cleaning ingredients arrays.
  function flatten (recipe) {
    // recipe.fermentables.fermentable : [] ---> recipe.fermentables : []
    // if only 1 fermentable,
    //
    // recipe.fermentables.fermentable : fermentable ---> recipe.fermentables : [fermentable]
    // if 0 fermentable ---> []
    const fermentablesArray = []
    if (recipe.fermentables.fermentable instanceof Array) {
      recipe.fermentables.fermentable.map((item) => fermentablesArray.push(item))
    } else {
      fermentablesArray.push(recipe.fermentables.fermentable)
    }
    recipe.fermentables = (fermentablesArray[0] == null) ? [] : fermentablesArray

    const hopsArray = []
    if (recipe.hops.hop instanceof Array) {
      recipe.hops.hop.map((item) => hopsArray.push(item))
    } else {
      hopsArray.push(recipe.hops.hop)
    }
    recipe.hops = (hopsArray[0] == null) ? [] : hopsArray

    const miscsArray = []
    if (recipe.miscs.misc instanceof Array) {
      recipe.miscs.misc.map((item) => miscsArray.push(item))
    } else {
      miscsArray.push(recipe.miscs.misc)
    }
    recipe.miscs = (miscsArray[0] == null) ? [] : miscsArray

    const yeastsArray = []
    if (recipe.yeasts.yeast instanceof Array) {
      recipe.yeasts.yeast.map((item) => yeastsArray.push(item))
    } else {
      yeastsArray.push(recipe.yeasts.yeast)
    }
    recipe.yeasts = (yeastsArray[0] == null) ? [] : yeastsArray

    const stepsArray = []
    if (recipe.mash.mash_steps.mash_step instanceof Array) {
      recipe.mash.mash_steps.mash_step.map((item) => stepsArray.push(item))
    } else {
      stepsArray.push(recipe.mash.mash_steps.mash_step)
    }
    recipe.mash.mash_steps = (stepsArray[0] == null) ? [] : stepsArray

    return recipe
  }

  function fixAmounts (recipe) {
    const toGrams = (item) => { item.amount = item.amount * 1000; return item }
    recipe.fermentables = recipe.fermentables.map(toGrams)
    recipe.hops = recipe.hops.map(toGrams)
    recipe.miscs = recipe.miscs.map(toGrams)
    return recipe
  }

  function fixNumbers (recipe) {
    recipe.batch_size = parseFloat(recipe.batch_size)
    recipe.efficiency = parseFloat(recipe.efficiency)
    recipe.boil_time = parseFloat(recipe.boil_time)
    recipe.fermentables.map((item) => {
      item.amount = parseFloat(item.amount)
      item.yield = parseFloat(item.yield)
      item.color = parseFloat(item.color)
    })
  }

  function fixColor (recipe) {
    const toEbc = (item) => { item.color = item.color * 1.97; return item }
    recipe.fermentables = recipe.fermentables.map(toEbc)
    return recipe
  }

  recipes.map(flatten)
  recipes.map(fixAmounts)
  recipes.map(fixNumbers)
  recipes.map(fixColor)

  return recipes
}

ipcMain.on('load', function () {
  const recipesFolder = path.join(os.homedir(), '/.config/joliebulle/recettes/test')
  const jsonList = recipesList(recipesFolder)
  console.log(JSON.stringify(jsonList))
  mainWindow.webContents.send('initRecipes', jsonList)
})

ipcMain.on('loadConfig', function () {
  const configPath = path.join(os.homedir(), '/.config/joliebulle/joliebulle.conf')
  const config = ini.parse(fs.readFileSync(configPath, 'utf-8'))
  mainWindow.webContents.send('initConfig', config)
})

