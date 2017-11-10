/*jshint esversion: 6 */

const electron = require('electron');
const os = require('os');
// Module to control application life.
const app = electron.app;
// Module to create native browser window.
const BrowserWindow = electron.BrowserWindow;
const fs = require ('fs');
const path = require('path');
const url = require('url');
const ipcMain = require('electron').ipcMain;
const dialog = electron.dialog;
const XML = require('pixl-xml');


// Keep a global reference of the window object, if you don't, the window will
// be closed automatically when the JavaScript object is garbage collected.
var mainWindow;

function createWindow () {
  // Create the browser window.
  mainWindow = new BrowserWindow({width: 800, height: 600});

  // and load the index.html of the app.
  mainWindow.loadURL(url.format({
    pathname: path.join(__dirname, '/app/index.html'),
    protocol: 'file:',
    slashes: true
  }));

  // Open the DevTools.
  mainWindow.webContents.openDevTools();

  // Emitted when the window is closed.
  mainWindow.on('closed', function () {
    // Dereference the window object, usually you would store windows
    // in an array if your app supports multi windows, this is the time
    // when you should delete the corresponding element.
    mainWindow = null;
  });
}

// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', createWindow);

// Quit when all windows are closed.
app.on('window-all-closed', function () {
  // On OS X it is common for applications and their menu bar
  // to stay active until the user quits explicitly with Cmd + Q
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', function () {
  // On OS X it's common to re-create a window in the app when the
  // dock icon is clicked and there are no other windows open.
  if (mainWindow === null) {
    createWindow();
  }
});


function walkRecipes(dir) {
  return fs.readdirSync(dir).reduce(function(list, file) {
    var name = path.join(dir, file);
    var isDir = fs.statSync(name).isDirectory();
    return list.concat(isDir ? walkRecipes(name) : [name]);
  }, []);
}

function parseAll(f, dirStorage) {
//    First we need a list of paths. f is the function used to read each directory inside dirStorage.
    var listFiles = f(dirStorage);
    return listFiles.reduce(function (list, filePath) {
        var recipeObject = parseFile(filePath);
          if (typeof recipeObject !== "undefined") {
          recipeObject.path = filePath;
          return list.concat([recipeObject]);
        } else {
          return list;}
    }, []);
}

function parseFile(filePath) {
  let rawXml = fs.readFileSync(filePath, 'utf8');
  try {
    let rawObject = XML.parse(rawXml, { lowerCase: true}).recipe;
    return rawObject;
  } catch(err) {
    console.log("XML parser error : " + err);
  }

}

function recipesList(recipesDir) {
  // parse all recipes recursively
  let recipes = parseAll(walkRecipes, recipesDir);

  // cleaning ingredients arrays.
  function flatten(recipe) {
    // recipe.fermentables.fermentable : [] ---> recipe.fermentables : []
    // if only 1 fermentable,
    //
    // recipe.fermentables.fermentable : fermentable ---> recipe.fermentables : [fermentable]
    // if 0 fermentable ---> []
    let fermentablesArray = [];
    if (recipe.fermentables.fermentable instanceof Array) {
      recipe.fermentables.fermentable.map((item) => fermentablesArray.push(item));
    }  else {
      fermentablesArray.push(recipe.fermentables.fermentable);
    }
    recipe.fermentables = (fermentablesArray[0] == null) ? [] : fermentablesArray;

    let hopsArray = [];
    if (recipe.hops.hop instanceof Array) {
      recipe.hops.hop.map((item) => hopsArray.push(item));
    } else {
      hopsArray.push(recipe.hops.hop);
    }
    recipe.hops = (hopsArray[0] == null) ? [] : hopsArray;

    let miscsArray = [];
    if (recipe.miscs.misc instanceof Array) {
      recipe.miscs.misc.map((item) => miscsArray.push(item));
    } else {
      miscsArray.push(recipe.miscs.misc);
    }
    recipe.miscs = (miscsArray[0] == null) ? [] : miscsArray;

    let yeastsArray = [];
    if (recipe.yeasts.yeast instanceof Array) {
      recipe.yeasts.yeast.map((item) => yeastsArray.push(item));
    } else {
      yeastsArray.push(recipe.yeasts.yeast);
    }
    recipe.yeasts = (yeastsArray[0] == null) ? [] : yeastsArray;

    let stepsArray = [];
    if (recipe.mash.mash_steps.mash_step instanceof Array) {
      recipe.mash.mash_steps.mash_step.map((item) => stepsArray.push(item));
    } else {
      stepsArray.push(recipe.mash.mash_steps.mash_step);
    }
    recipe.mash.mash_steps = (stepsArray[0] == null) ? [] : stepsArray;



    return recipe;
  }

  function fixAmounts (recipe) {
    let toGrams = (item) => {item.amount = item.amount * 1000; return item; };
    recipe.fermentables = recipe.fermentables.map(toGrams);
    recipe.hops = recipe.hops.map(toGrams);
    recipe.miscs = recipe.miscs.map(toGrams);
    return recipe;
  }

  recipes.map(flatten);
  recipes.map(fixAmounts);

  return recipes;
}


ipcMain.on('load-button-clicked', function () {
  let recipesFolder = path.join(os.homedir(), '/.config/joliebulle/recettes');
  const jsonList = recipesList(recipesFolder);
  mainWindow.webContents.send('initRecipes', jsonList);

});
