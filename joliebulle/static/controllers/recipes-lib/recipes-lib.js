/*jslint nomen: true */
/*global main, _, beerCalc, recipesApp, jb2xml,angular, translate, jb2bb */
recipesApp.controller('RecipeslibCtrl', ['$scope', '$http', '$filter', function ($scope, $http, $filter) {
    "use strict";
    var parser, xml, string, fermentable, hop, misc, yeast;
    
    $scope.active = false;
    $scope.editMode = false;
    
    $scope.init = function () {
        // $scope.recipes = JSON.parse(main.dataRecipes());
        $scope.recipes = [{"name": "Blanche", "type": "All Grain", "hops": [{"name": "Hallertauer Mittelfrueh", "ibuPart": "11.6", "use": "Boil", "amount": 10.0, "alpha": 5.0, "form": "Leaf", "time": 60.0}, {"name": "Hallertauer Mittelfrueh", "ibuPart": "4.2", "use": "Boil", "amount": 10.0, "alpha": 5.0, "form": "Leaf", "time": 10.0}], "fudgeFactor": 1.7, "notes": "Essai de notes.", "grainRetention": 1, "coolingLossRate": 5, "miscs": [{"name": "Zeste dorange", "type": "Flavor", "amount": 10.0, "use": "Boil", "time": 0.0}, {"name": "Coriandre", "type": "Spice", "amount": 5.0, "use": "Boil", "time": 0.0}], "path": "/Users/pierre/.config/joliebulle/recettes/Samples/Blanche.xml", "gu": 49.4719043, "style": "Blanche", "efficiency": 70.0, "boilTime": 60.0, "grainTemp": 20, "brewer": "314r", "preBoilGu": 49.4719043, "grainWeight": 2300.0, "yeasts": [{"name": "Belgian Wit Ale", "labo": "White Labs", "product_id": "WLP400", "form": "Liquid", "attenuation": 76.0}], "boilOffRate": 10, "volume": 10.0, "fermentables": [{"name": "Pale Wheat Malt", "type": "Grain", "color": 3.94, "recoMash": "TRUE", "amount": 1000.0, "fyield": 80.0, "afterBoil": "FALSE"}, {"name": "Pilsner", "type": "Grain", "color": 3.94, "recoMash": "TRUE", "amount": 1000.0, "fyield": 81.0, "afterBoil": "FALSE"}, {"name": "Flaked Wheat", "type": "Grain", "color": 3.94, "recoMash": "TRUE", "amount": 300.0, "fyield": 77.0, "afterBoil": "FALSE"}], "mashProfile": {"name": "Infusion simple, corps moyen", "sparge": "78.0", "ph": "5.4", "tunTemp": "20", "steps": [{"name": "Emp\u00e2tage", "type_view": "Infusion", "type": "Infusion", "temp": "67.0", "time": "60"}, {"name": "Mash Out", "type_view": "Temp\u00e9rature", "type": "Temperature", "temp": "75.0", "time": "10"}]}},{"name": "SMASH Amarillo", "type": "All Grain", "hops": [{"name": "Amarillo", "ibuPart": "0.0", "use": "Boil", "amount": 10.0, "alpha": 9.0, "form": "Leaf", "time": 0.0}, {"name": "Amarillo", "ibuPart": "7.1", "use": "Boil", "amount": 10.0, "alpha": 9.0, "form": "Leaf", "time": 10.0}, {"name": "Amarillo", "ibuPart": "29.6", "use": "Boil", "amount": 15.0, "alpha": 9.0, "form": "Leaf", "time": 60.0}], "fudgeFactor": 1.7, "notes": null, "grainRetention": 1, "coolingLossRate": 5, "miscs": [], "path": "/Users/pierre/.config/joliebulle/recettes/Samples/SMASH Amarillo.xml", "gu": 55.760022499999984, "style": "Pale Ale", "efficiency": 70.0, "boilTime": 60.0, "grainTemp": 20, "brewer": "314r", "preBoilGu": 55.760022499999984, "grainWeight": 2500.0, "yeasts": [{"name": "Safale", "labo": "Fermentis", "product_id": "S-04", "form": "Dry", "attenuation": 73.0}], "boilOffRate": 10, "volume": 10.0, "fermentables": [{"name": "Marris Otter", "type": "Grain", "color": 5.91, "recoMash": "TRUE", "amount": 2500.0, "fyield": 83.0, "afterBoil": "FALSE"}], "mashProfile": {"name": "Infusion simple, corps moyen", "sparge": "78.0", "ph": "5.4", "tunTemp": "20", "steps": [{"name": "Emp\u00e2tage", "type_view": "Infusion", "type": "Infusion", "temp": "67.0", "time": "60"}, {"name": "Mash Out", "type_view": "Temp\u00e9rature", "type": "Temperature", "temp": "75.0", "time": "10"}]}}];
        $scope.recipes = _.chain($scope.recipes)
            .sortBy(function (o) {return o.name.toLowerCase(); })
            .sortBy(function (o) {return o.brewer.toLowerCase(); })
            .value();
        $scope.ingredients = JSON.parse(main.dataIngredients());
        $scope.ingredients = translate.translate_fr($scope.ingredients);
        $scope.mashProfiles = JSON.parse(main.dataProfiles()).mashes;

    };

    $scope.deleteLib = function (recipe) {
		$scope.recipes.splice($scope.recipes.indexOf(recipe), 1);
        main.deleteLib(recipe.path);
    };

    $scope.openRecipeClicked = function (recipe) {
        main.viewRecipeLib(recipe.path);
    };

    $scope.editFermentable = function (index) {
        $scope.freezeRecipe();
        $scope.showFermentableEditor = true;
        $scope.currentFerm = $scope.currentRecipe.fermentables[index];
        // $scope.currentIng.index = index;
    };

    $scope.closeFermentableEditor = function () {
        $scope.showFermentableEditor = false;
        // $scope.currentRecipe.fermentables[$scope.currentIng.index] = $scope.currentIng; 
    };

    $scope.editHop = function (index) {
        $scope.freezeRecipe();
        $scope.showHopEditor = true;
        $scope.currentHop = $scope.currentRecipe.hops[index];
    };

    $scope.closeHopEditor = function () {
        $scope.showHopEditor = false;
    };

    $scope.editMisc = function (index) {
        $scope.freezeRecipe();
        $scope.showMiscEditor = true;
        $scope.currentMisc = $scope.currentRecipe.miscs[index];
    };

    $scope.closeMiscEditor = function () {
        $scope.showMiscEditor = false;
    };

    $scope.editYeast = function (index) {
        $scope.freezeRecipe();
        $scope.showYeastEditor = true;
        $scope.currentYeast = $scope.currentRecipe.yeasts[index];
    };

    $scope.closeYeastEditor = function () {
        $scope.showYeastEditor = false;
    };


    $scope.recipeSelected = function (recipe) {
        $scope.active = true;
//        if editMode do nothing
        if ($scope.editMode) {
            return null;
        } else {
            $scope.currentRecipe = recipe;
            // $scope.currentRecipe = $scope.translate_fr($scope.currentRecipe);
            $scope.calcProfile($scope.currentRecipe);
            $scope.sortRecipe();
            $scope.activeClass = $scope.currentRecipe.path;
    //        console.log($scope.currentRecipe.hops);
            main.viewRecipeLib(recipe.path);
        }

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
        recipe = translate.translate_fr(recipe);

        if ($scope.scaleIngredients) {
            $scope.scaleRatio = recipe.volume / recipe.oldVolume;
            beerCalc.scaleIngredients($scope.scaleRatio, recipe.fermentables, recipe.hops, recipe.miscs);
        } else {
            $scope.scaleRatio = 1;
            recipe.ebc = Math.round(beerCalc.ebc(recipe.fermentables, recipe.volume));
            recipe.og = (Math.round(beerCalc.originalGravity(recipe) * 1000) / 1000).toFixed(3);
            recipe.fg = (Math.round(beerCalc.finalGravity(recipe) * 1000) / 1000).toFixed(3);
            recipe.ibu = Math.round(beerCalc.ibus(recipe));
            recipe.bugu = Math.round(beerCalc.bugu(recipe) * 10) / 10;
            recipe.alc = Math.round(beerCalc.alc(recipe) * 10) / 10;
        }
        console.log("ratio", $scope.scaleRatio);
        recipe.oldVolume = recipe.volume;
    };

    $scope.fermentableSelected = function (fermentable) {
        $scope.currentFerm.name = fermentable.name;
        $scope.currentFerm.color = fermentable.color;
        $scope.currentFerm.type = fermentable.type;
        $scope.currentFerm.typeView = fermentable.typeView;
        $scope.currentFerm.fyield = fermentable.fyield;
        $scope.calcProfile($scope.currentRecipe);
    };

    $scope.hopSelected = function (hop) {
        $scope.currentHop.name = hop.name;
        $scope.currentHop.alpha = hop.alpha;
        $scope.currentHop.form = hop.form;
        $scope.currentHop.formView = hop.formView;
        $scope.calcProfile($scope.currentRecipe);
    };

    $scope.miscSelected = function (misc) {
        $scope.currentMisc.name = misc.name;
        $scope.currentMisc.use = misc.use;
        $scope.currentMisc.useView = misc.useView;
        $scope.currentMisc.type = misc.type;
        $scope.currentMisc.typeView = misc.typeView;
        $scope.calcProfile($scope.currentRecipe);
    };

    $scope.yeastSelected = function (yeast) {
        $scope.currentYeast.name = yeast.name;
        $scope.currentYeast.form = yeast.form;
        $scope.currentYeast.formView = yeast.formView;
        $scope.currentYeast.product_id = yeast.product_id;
        $scope.currentYeast.labo = yeast.labo;
        $scope.currentYeast.attenuation = yeast.attenuation;
        $scope.calcProfile($scope.currentRecipe);
    };
    
    $scope.cancelIngredient = function () {
        $scope.currentRecipe = $scope.freezedRecipe;
        $scope.showFermentableEditor = false;
        $scope.showHopEditor = false;
        $scope.showMiscEditor = false;
        $scope.showYeastEditor = false;
    };
    
    $scope.freezeRecipe = function () {
        $scope.freezedRecipe = angular.copy($scope.currentRecipe);
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
        $scope.freezeRecipe();
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
        $scope.freezeRecipe();
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
        $scope.freezeRecipe();
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
        $scope.freezeRecipe();
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

    $scope.exportToBb = function () {
        main.copyBbcode(jb2bb.exportString($scope.currentRecipe));
    };

    
}]);



