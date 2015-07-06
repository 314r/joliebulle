/*jslint nomen: true */
/*global main, _, beerCalc, recipesApp, jb2xml*/
recipesApp.controller('RecipeslibCtrl', ['$scope', '$http', '$filter', function ($scope, $http, $filter) {
    "use strict";
    var parser, xml, string;
    
    $scope.active = false;
    $scope.editMode = false;
    

    $scope.init = function (dataJson, ingredients, profiles) {
        $scope.recipes = dataJson;
        $scope.recipes = _.chain($scope.recipes)
            .sortBy(function (o) {return o.name.toLowerCase(); })
            .sortBy(function (o) {return o.brewer.toLowerCase(); })
            .value();
        $scope.ingredients = ingredients;
        $scope.mashProfiles = profiles.mashes;
    };

    $scope.deleteLib = function (recipe) {
		$scope.recipes.splice($scope.recipes.indexOf(recipe), 1);
        main.deleteLib(recipe.path);
    };

    $scope.openRecipeClicked = function (recipe) {
        main.viewRecipeLib(recipe.path);
    };

    $scope.editFermentable = function (index) {
        $scope.showFermentableEditor = true;
        $scope.currentFerm = $scope.currentRecipe.fermentables[index];
        // $scope.currentIng.index = index;
    };

    $scope.closeFermentableEditor = function () {
        $scope.showFermentableEditor = false;
        // $scope.currentRecipe.fermentables[$scope.currentIng.index] = $scope.currentIng; 
    };

    $scope.editHop = function (index) {
        $scope.showHopEditor = true;
        $scope.currentHop = $scope.currentRecipe.hops[index];
    };

    $scope.closeHopEditor = function () {
        $scope.showHopEditor = false;
    };

    $scope.editMisc = function (index) {
        $scope.showMiscEditor = true;
        $scope.currentMisc = $scope.currentRecipe.miscs[index];
    };

    $scope.closeMiscEditor = function () {
        $scope.showMiscEditor = false;
    };

    $scope.editYeast = function (index) {
        $scope.showYeastEditor = true;
        $scope.currentYeast = $scope.currentRecipe.yeasts[index];
    };

    $scope.closeYeastEditor = function () {
        $scope.showYeastEditor = false;
    };


    $scope.recipeSelected = function (recipe) {
        $scope.active = true;
        $scope.currentRecipe = recipe;
        $scope.calcProfile(recipe);
        $scope.sortRecipe();
        $scope.activeClass = $scope.currentRecipe.path;
        main.viewRecipeLib(recipe.path);
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
        $scope.currentRecipe.fermentables = _.sortBy($scope.currentRecipe.fermentables, function (o) {return parseInt(o.amount, 10); }).reverse();
        $scope.currentRecipe.hops = _.sortBy($scope.currentRecipe.hops, function (o) {return parseInt(o.time, 10); }).reverse();
        $scope.currentRecipe.miscs = _.sortBy($scope.currentRecipe.miscs, function (o) {return parseInt(o.amount, 10); }).reverse();
        return $scope.currentRecipe;
    };

    $scope.calcProfile = function (recipe) {
        recipe.ebc = Math.round(beerCalc.ebc(recipe.fermentables, recipe.volume));
        recipe.og = (Math.round(beerCalc.originalGravity(recipe) * 1000) / 1000).toFixed(3);
        recipe.fg = (Math.round(beerCalc.finalGravity(recipe) * 1000) / 1000).toFixed(3);
        recipe.ibu = Math.round(beerCalc.ibus(recipe));
        recipe.bugu = Math.round(beerCalc.bugu(recipe) * 10) / 10;
        recipe.alc = Math.round(beerCalc.alc(recipe) * 10) / 10;
    };

    $scope.fermentableSelected = function (fermentable) {
        $scope.currentFerm.name = fermentable.name;
        $scope.currentFerm.color = fermentable.color;
        $scope.currentFerm.type = fermentable.type;
        $scope.currentFerm.fyield = fermentable.fyield;
        $scope.calcProfile($scope.currentRecipe);
    };

    $scope.hopSelected = function (hop) {
        $scope.currentHop.name = hop.name;
        $scope.currentHop.alpha = hop.alpha;
        $scope.currentHop.form = hop.form;
        $scope.calcProfile($scope.currentRecipe);
    };

    $scope.miscSelected = function (misc) {
        $scope.currentMisc.name = misc.name;
        $scope.currentMisc.use = misc.use;
        $scope.currentMisc.type = misc.type;
        $scope.calcProfile($scope.currentRecipe);
    };

    $scope.yeastSelected = function (yeast) {
        $scope.currentYeast.name = yeast.name;
        $scope.currentYeast.form = yeast.form;
        $scope.currentYeast.product_id = yeast.product_id;
        $scope.currentYeast.labo = yeast.labo;
        $scope.currentYeast.attenuation = yeast.attenuation;
        $scope.calcProfile($scope.currentRecipe);
    };
    
    $scope.save = function (recipe) {
        main.saveRecipe(jb2xml.exportString(recipe), recipe.path);
        $scope.editMode = false;
    };

    $scope.editRecipe = function () {
        $scope.editMode = true;
        $scope.oldRecipes = angular.copy($scope.recipes);
        $scope.oldCurrentRecipe = angular.copy($scope.currentRecipe);
    };
    
    $scope.cancel = function () {
        $scope.recipes = $scope.oldRecipes;
        $scope.currentRecipe = $scope.oldCurrentRecipe;
        $scope.editMode = false;
    };
    
}]);



