/*jslint nomen: true */
/*global main, _, beerCalc, recipesApp, jb2xml, jbrecipe, angular, translate, jb2bb */
recipesApp.controller('RecipeslibCtrl', ['$scope', '$http', '$filter', function ($scope, $http, $filter) {
    "use strict";
    var fermentable, hop, misc, yeast, generatedRecipe, clone;
    var ipcRenderer = require('electron').ipcRenderer;

    $scope.active = false;
    $scope.editMode = false;

    $scope.init = function () {
        $scope.recipes = $scope.importRecipes();
    };

    $scope.importRecipes = function () {
        ipcRenderer.send('load-button-clicked');
    };

    ipcRenderer.on('initRecipes' , function(event , data){
    $scope.sortRecipes(data);
    });

    $scope.sortRecipes = function (data) {

        $scope.recipes = data;
        $scope.$apply();
        $scope.recipes = _.chain(data)
            .sortBy(function (o) {return o.name.toLowerCase(); })
            .sortBy(function (o) {return o.brewer.toLowerCase(); })
            .value();
        console.log($scope.recipes);
    };


    $scope.openRecipeClicked = function (recipe) {
        main.viewRecipeLib(recipe.path);
    };


    $scope.recipeSelected = function (recipe) {
        $scope.active = true;
        $scope.currentRecipe = (translate.translate_en(recipe));
        console.log($scope.currentRecipe);
        $scope.calcProfile($scope.currentRecipe);
        $scope.sortRecipe();
        $scope.activeClass = $scope.currentRecipe.path;


    };

    $scope.sortByName = function () {
        $scope.recipes = _.chain($scope.recipes)
            .sortBy(function (o) {return o.brewer.toLowerCase(); })
            .sortBy(function (o) {return o.name.toLowerCase(); })
            .value();
        return $scope.recipes;
    };

    $scope.sortByBrewer = function () {
        $scope.recipes = _.chain($scope.recipes)
            .sortBy(function (o) {return o.name.toLowerCase(); })
            .sortBy(function (o) {return o.brewer.toLowerCase(); })
            .value();
        return $scope.recipes;
    };

    $scope.sortRecipe = function () {
        var aromaArray, dryArray, boilArray, firstArray, mashArray, concanArray;
        $scope.currentRecipe.fermentables = _.chain($scope.currentRecipe.fermentables)
            .sortBy(function (o) {return o.name.toLowerCase(); }).reverse()
            .sortBy(function (o) {return parseInt(o.amount,10); }).reverse()
            .value();
        $scope.currentRecipe.hops = _.chain($scope.currentRecipe.hops)
            .sortBy(function (o) {return o.name.toLowerCase(); }).reverse()
            .sortBy(function (o) {return parseInt(o.time, 10); }).reverse()
            .value();

        aromaArray = [];
        dryArray = [];
        boilArray = [];
        firstArray = [];
        mashArray = [];
        $scope.currentRecipe.hops.forEach(function (h) {
            if (h.use === "Aroma") {
                aromaArray.push(h);
            }
            if (h.use === "Dry Hop") {
                dryArray.push(h);
            }
            if (h.use === "Boil") {
                boilArray.push(h);
            }
            if (h.use === "First Wort") {
                firstArray.push(h);
            }
            if (h.use === "Mash") {
                mashArray.push(h);
            }

        });
        concanArray = mashArray.concat(firstArray, boilArray, aromaArray, dryArray);
        $scope.currentRecipe.hops = concanArray;

        $scope.currentRecipe.miscs = _.chain($scope.currentRecipe.miscs)
            .sortBy(function (o) {return o.name.toLowerCase();}).reverse()
            .sortBy(function (o) {return parseInt(o.amount, 10); }).reverse()
            .value();
        return $scope.currentRecipe;
    };


    $scope.calcProfile = function (recipe) {
        recipe = (translate.translate_en(recipe));

        $scope.scaleRatio = 1;
        recipe.ebc = Math.round(beerCalc.ebc(recipe.fermentables, recipe.batch_size));
        recipe.og = (Math.round(beerCalc.originalGravity(recipe) * 1000) / 1000).toFixed(3);
        recipe.fg = (Math.round(beerCalc.finalGravity(recipe) * 1000) / 1000).toFixed(3);
        recipe.ibu = Math.round(beerCalc.ibus(recipe).ibu);
        recipe.bugu = Math.round(beerCalc.bugu(recipe) * 10) / 10;
        recipe.alc = Math.round(beerCalc.alc(recipe) * 10) / 10;
        recipe.colorHtml = beerCalc.colorHtml($scope.currentRecipe.ebc);
        recipe.fermentables.forEach(function (fermentable) {
            fermentable.amountRatio = (beerCalc.ingRatio(recipe.fermentables, fermentable.amount) * 100).toFixed(1);
            return fermentable;
        });
        recipe.hops.forEach(function (hop) {
            hop.amountRatio = (beerCalc.ingRatio(recipe.hops, hop.amount) * 100).toFixed(1);
            return hop;
        });

        recipe.oldVolume = recipe.batch_size;

    };








}]);
