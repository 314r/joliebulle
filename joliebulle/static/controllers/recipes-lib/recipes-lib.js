/*jslint nomen: true */
/*global main, _, beerCalc, recipesApp, jb2xml,angular*/
recipesApp.controller('RecipeslibCtrl', ['$scope', '$http', '$filter', function ($scope, $http, $filter) {
    "use strict";
    var parser, xml, string, fermentable, hop, misc, yeast;
    
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
    
    $scope.locale_fr = {
        "Grain" : "Grain",
        "Extract" : "Extrait",
        "Dry Extract" : "Extrait Sec",
        "Sugar" : "Sucre",
        "TRUE" : "Après Ebullition",
        "FALSE" : "Brassage",
        "Plug" : "Cône",
        "Leaf" : "Feuille",
        "Pellet" : "Pellet",
        "Boil" : "Ebullition",
        "Dry Hop" : "Dry Hop",
        "First Wort" : "Premier Moût",
        "Mash" : "Empâtage",
        "Aroma" : "Aromatique",
        "Spice" : "Epice",
        "Flavor" : "Arôme",
        "Water Agent" : "Traitement Eau",
        "Herb" : "Herbe",
        "Fining" : "Clarifiant",
        "Other" : "Autre",
        "Primary" : "Primaire",
        "Secondary" : "Secondaire",
        "Bottling" : "Embouteillage",
        "Liquid" : "Liquide",
        "Dry" : "Poudre",
        "Slant" : "Gélose",
        "Culture" : "Culture"
    };

    $scope.translate_fr = function (recipe) {
        recipe.hops.forEach(function (hop) {
            // If formView is in french (not undefined), we translate hop.form to english/beerxml. 
            // If formView is undefined, we translate hop.form to french.
            if (typeof hop.formView !== 'undefined') {
                hop.form = (_.invert($scope.locale_fr))[hop.formView];
            } else {
                hop.formView = $scope.locale_fr[hop.form];
            }
            if (typeof hop.useView !== 'undefined') {
                hop.use = (_.invert($scope.locale_fr))[hop.useView];
            } else {
                hop.useView = $scope.locale_fr[hop.use];
            }
        });
        recipe.fermentables.forEach(function (fermentable) {
            if (typeof fermentable.typeView !== 'undefined') {
                fermentable.type = (_.invert($scope.locale_fr))[fermentable.typeView];
            } else {
                fermentable.typeView = $scope.locale_fr[fermentable.type];
            }
            if (typeof fermentable.afterBoilView !== 'undefined') {
                fermentable.afterBoil = (_.invert($scope.locale_fr))[fermentable.afterBoilView];
            } else {
                fermentable.afterBoilView = $scope.locale_fr[fermentable.afterBoil];
            }
        });

        recipe.miscs.forEach(function (misc) {
            if (typeof misc.useView !== 'undefined') {
                misc.use = (_.invert($scope.locale_fr))[misc.useView];
            } else {
                misc.useView = $scope.locale_fr[misc.use];
            }
            if (typeof misc.typeView !== 'undefined') {
                misc.type = (_.invert($scope.locale_fr))[misc.ftypeView];
            } else {
                misc.typeView = $scope.locale_fr[misc.type];
            }

        });

        recipe.yeasts.forEach(function (yeast) {
            if (typeof yeast.formView !== 'undefined') {
                yeast.form = (_.invert($scope.locale_fr))[yeast.formView];
            } else {
                yeast.formView = $scope.locale_fr[yeast.form];
            }
        });


        return recipe;
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
        $scope.currentRecipe = $scope.translate_fr($scope.currentRecipe);
        $scope.calcProfile(recipe);
        $scope.sortRecipe();
        $scope.activeClass = $scope.currentRecipe.path;
//        console.log($scope.currentRecipe.hops);
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
        recipe = $scope.translate_fr(recipe);
        console.log(recipe);
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

    $scope.newFermentable = function () {
        fermentable = {};
        fermentable.name = "grain";
        fermentable.color = 5;
        fermentable.type = "Grain";
        fermentable.fyield = 90;
        fermentable.amount = 0;
        fermentable.afterBoil = "FALSE";
        $scope.currentRecipe.fermentables.push(fermentable);
        $scope.showFermentableEditor = true;
        $scope.currentFerm = fermentable;
        $scope.calcProfile($scope.currentRecipe);
    };

    $scope.newHop = function () {
        hop = {};
        hop.name = "generic";
        hop.alpha = 0;
        hop.use = "Boil";
        hop.form = "Plug";
        hop.time = 0;
        hop.amount = 0;
        $scope.currentRecipe.hops.push(hop);
        $scope.showHopEditor = true;
        $scope.currentHop = hop;
        $scope.calcProfile($scope.currentRecipe);
    };

    $scope.newMisc = function () {
        misc = {};
        misc.name = "generic";
        misc.amount = 0;
        misc.type = "Spice";
        misc.use = "Boil";
        misc.time = 0;
        $scope.currentRecipe.miscs.push(misc);
        $scope.showMiscEditor = true;
        $scope.currentMisc = misc;
        $scope.calcProfile($scope.currentRecipe);
    };

    $scope.newYeast = function () {
        yeast = {};
        yeast.name = "generic";
        yeast.labo = "generic";
        yeast.product_id = "generic";
        yeast.form = "Dry";
        yeast.attenuation = 75;
        $scope.currentRecipe.yeasts.push(yeast);
        $scope.showYeastEditor = true;
        $scope.currentYeast = yeast;
        $scope.calcProfile($scope.currentRecipe);
    };

    $scope.removeFermentable = function (index) {
        $scope.currentRecipe.fermentables.splice(index, 1);
        $scope.calcProfile($scope.currentRecipe);
    };

    $scope.removeHop = function (index) {
        $scope.currentRecipe.hops.splice(index, 1);
        $scope.calcProfile($scope.currentRecipe);
    };

    $scope.removeMisc = function (index) {
        $scope.currentRecipe.miscs.splice(index, 1);
        $scope.calcProfile($scope.currentRecipe);
    };

    $scope.removeYeast = function (index) {
        $scope.currentRecipe.yeasts.splice(index, 1);
        $scope.calcProfile($scope.currentRecipe);
    };



    
}]);



