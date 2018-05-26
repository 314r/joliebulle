// This file is required by the index.html file and will
// be executed in the renderer process for that window.
// All of the Node.js APIs are available in this process.

var path = require('path');


var ipcRenderer = require('electron').ipcRenderer;

var loadLib = document.querySelector('.load');
loadLib.addEventListener('click', function () {
  ipcRenderer.send('load-button-clicked');
});

ipcRenderer.on('initRecipes' , function(event , data){ 
	displayRecipe(data);
});


var displayRecipe = function (data) {
	console.log(data); 
};

// var loadRend = document.querySelector('.load-from-renderer');
// var fs = require ('fs');
// var file = path.join(__dirname, 'recipe.xml');
// var parser = new xml2js.Parser({explicitArray : true});
// loadRend.addEventListener('click', function () {
// 	fs.readFile(file, 'utf-8', function (err, data) {
//   		parser.parseString(data, function (err, result) {
//     		displayRecipe(result);
// 		});
//   });
// });



// var displayRecipe = function (recipe) {
// 	console.log(recipe);
// 	var recipeContainer = document.querySelector('.recipeContainer');
// 	recipeContainer.appendChild(document.createElement('h2')).innerText = recipe.RECIPES.RECIPE[0].NAME[0];
// 	recipeContainer.appendChild(document.createElement('span')).innerText = recipe.RECIPES.RECIPE[0].TYPE[0] + ' by ' + recipe.RECIPES.RECIPE[0].BREWER[0];
// 	recipe.RECIPES.RECIPE[0].FERMENTABLES[0].FERMENTABLE.forEach(function(f){
// 		var fermentableUse;
// 		if (f.ADD_AFTER_BOIL === "TRUE") {
// 			fermentableUse = 'After Boil'; 
// 		} else {
// 			fermentableUse = 'Mash';
// 		}
// 		recipeContainer.appendChild(document.createElement('p')).innerText = f.NAME + ' ' + f.AMOUNT + 'g ' + fermentableUse;

// 	});
// 	recipe.RECIPES.RECIPE[0].HOPS[0].HOP.forEach(function (h) {
// 		recipeContainer.appendChild(document.createElement('p')).innerText = h.NAME[0] + '	α' + h.ALPHA[0] + '% ' + h.TIME[0] + 'min ' + h.USE[0];
// 	});
// 	recipe.RECIPES.RECIPE[0].YEASTS[0].YEAST.forEach(function (y) {
// 		recipeContainer.appendChild(document.createElement('p')).innerText = y.NAME[0] + ' ' + y.LABORATORY[0] + ' ' + y.PRODUCT_ID[0] + ' ' + y.FORM[0];
// 	});
// 	recipe.RECIPES.RECIPE[0].YEASTS[0].YEAST.forEach(function (y) {
// 		recipeContainer.appendChild(document.createElement('p')).innerText = y.NAME[0] + ' ' + y.LABORATORY[0] + ' ' + y.PRODUCT_ID[0] + ' ' + y.FORM[0];
// 	});
// 	recipeContainer.appendChild(document.createElement('p')).innerText = 'Mash Profile : ' + recipe.RECIPES.RECIPE[0].MASH[0].NAME[0];
// 	recipeContainer.appendChild(document.createElement('p')).innerText = 'pH : ' + recipe.RECIPES.RECIPE[0].MASH[0].PH[0];
// 	recipe.RECIPES.RECIPE[0].MASH[0].MASH_STEPS[0].MASH_STEP.forEach(function (m) {
// 		recipeContainer.appendChild(document.createElement('p')).innerText = m.NAME[0] + ' ' + m.TYPE[0] + ' ' + m.STEP_TIME[0] + 'min @' + m.STEP_TEMP[0] + '°C';
// 	});
// 	recipeContainer.appendChild(document.createElement('p')).innerText = 'Sparge temp : ' + recipe.RECIPES.RECIPE[0].MASH[0].SPARGE_TEMP[0];
// 	recipeContainer.appendChild(document.createElement('p')).innerText = recipe.RECIPES.RECIPE[0].MASH[0].NOTES;


// };



