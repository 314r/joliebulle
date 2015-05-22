/*jslint nomen: true */
/*global main, _, beerCalc, recipesApp*/
recipesApp.controller('RecipeslibCtrl', ['$scope', '$http', '$filter', function ($scope, $http, $filter) {
    "use strict";
    var parser, xml, string;
    
    $scope.active = false;
    

    $scope.init = function (dataJson, ingredients) {
        $scope.recipes = dataJson;
        $scope.recipes = _.chain($scope.recipes)
            .sortBy(function (o) {return o.name.toLowerCase(); })
            .sortBy(function (o) {return o.brewer.toLowerCase(); })
            .value();
        $scope.ingredients = ingredients;
        // return $scope.recipes;
    };

    $scope.deleteLib = function (recipe) {
		$scope.recipes.splice($scope.recipes.indexOf(recipe), 1);
        main.deleteLib(recipe.path);
    };

    $scope.openRecipeClicked = function (recipe) {
        main.viewRecipeLib(recipe.path);
    };

    $scope.editIngredient = function (index) {
        $scope.showIngredientEditor = true;
        $scope.currentIng = $scope.currentRecipe.fermentables[index];
        // $scope.currentIng.index = index;
    };

    $scope.closeIngredientEditor = function () {
        $scope.showIngredientEditor = false;
        // $scope.currentRecipe.fermentables[$scope.currentIng.index] = $scope.currentIng; 

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
        $scope.currentIng.name = fermentable.name;
    };

    $scope.jb2xml = function (recipe) {
        parser = new DOMParser();
        string = "<RECIPES><RECIPE>";
        string += "<NAME>" + recipe.name + "</NAME>";
        string += "<VERSION>1</VERSION>";
        string += "<TYPE>" + recipe.type + "</TYPE>";
        string += "<BREWER>" + recipe.brewer + "</BREWER>";
        string += "<STYLE><NAME>" + recipe.style + "</NAME><VERSION>1</VERSION><CATEGORY /><CATEGORY_NUMBER /><STYLE_LETTER /><STYLE_GUIDE /><TYPE /><OG_MIN /><OG_MAX /><FG_MIN /><FG_MAX /><IBU_MIN /><IBU_MAX /><COLOR_MIN /><COLOR_MAX /></STYLE>";
        string += "<BATCH_SIZE>" + recipe.volume + "</BATCH_SIZE>";
        string += "<BOIL_SIZE />";
        string += "<BOIL_TIME>" + recipe.boilTime + "</BOIL_TIME>";
        string += "<EFFICIENCY>" + recipe.efficiency + "</EFFICIENCY>";
        string += "<OG>" + recipe.og + "</OG><FG>" + recipe.fg + "</FG>";
        string += "<FERMENTABLES>";
        recipe.fermentables.forEach(function (fermentable) {
            string += "<FERMENTABLE>";
            string += "<NAME>" + fermentable.name + "</NAME>";
            string += "<VERSION>1</VERSION>";
            string += "<AMOUNT>" + fermentable.amount / 1000 + "</AMOUNT>";
            string += "<TYPE>" + fermentable.type + "</TYPE>";
            string += "<YIELD>" + fermentable.fyield + "</YIELD>";
            string += "<RECOMMEND_MASH>" + fermentable.recoMash + "</RECOMMEND_MASH>";
            string += "<ADD_AFTER_BOIL>" + fermentable.afterBoil + "</ADD_AFTER_BOIL>";
            string += "<COLOR>" + fermentable.color / 1.97 + "</COLOR>";
            string += "</FERMENTABLE>";
        });
        string += "</FERMENTABLES>";
        string += "<HOPS>";
        recipe.hops.forEach(function (hop) {
            string += "<HOP>";
            string += "<NAME>" + hop.name + "</NAME>";
            string += "<VERSION>1</VERSION>";
            string += "<AMOUNT>" + hop.amount / 1000 + "</AMOUNT>";
            if (hop.form === 0) {
                string += "<FORM>Pellet</FORM>";
            } else if (hop.form === 1) {
                string += "<FORM>Leaf</FORM>";
            } else if (hop.form === 2) {
                string += "<FORM>Plug</FORM>";
            }
            string += "<TIME>" + hop.time + "</TIME>";
            string += "<ALPHA>" + hop.alpha + "</ALPHA>";
            string += "<USE>" + hop.use + "</USE>";
            string += "</HOP>";
            // revoir form
        });
        string += "</HOPS>";
        string += "<YEASTS>";
        recipe.yeasts.forEach(function (yeast) {
            string += "<YEAST>";
            string += "<NAME>" + yeast.name + "</NAME>";
            string += "<VERSION>1</VERSION>";
            string += "<TYPE />";
            string += "<FORM>" + yeast.form + "</FORM>";
            string += "<LABORATORY>" + yeast.labo + "</LABORATORY>";
            string += "<PRODUCT_ID>" + yeast.product_id + "</PRODUCT_ID>";
            string += "<ATTENUATION>" + yeast.attenuation + "</ATTENUATION>";
            string += "</YEAST>";
        });
        string += "</YEASTS>";
        string += "<MISCS>";
        recipe.miscs.forEach(function (misc) {
            string += "<MISC>";
            string += "<NAME>" + misc.name + "</NAME>";
            string += "<VERSION>1</VERSION>";
            string += "<AMOUNT>" + misc.amount / 1000 + "</AMOUNT>";
            string += "<TYPE>" + misc.type + "</TYPE>";
            string += "<TIME>" + misc.time + "</TIME>";
            string += "<USE>" + misc.use + "</USE>";
            string += "</MISC>";
        });
        string += "</MISCS>";
        string += "<WATERS/>";
        string += "<MASH>";
        string += "<NAME>" + recipe.mashProfile.name + "</NAME>";
        string += "<VERSION>1</VERSION>";
        string += "<GRAIN_TEMP>" + recipe.grainTemp + "</GRAIN_TEMP>";
        string += "<TUN_TEMP>" + recipe.mashProfile.tunTemp + "</TUN_TEMP>";
        string += "<SPARGE_TEMP>" + recipe.mashProfile.sparge + "</SPARGE_TEMP>";
        string += "<PH>" + recipe.mashProfile.ph + "</PH>";
        string += "<MASH_STEPS>";
        recipe.mashProfile.steps.forEach(function (step) {
            string += "<MASH_STEP>";
            string += "<NAME>" + step.name + "</NAME>";
            string += "<VERSION>1</VERSION>";
            string += "<TYPE>" + step.type + "</TYPE>";
            string += "<STEP_TIME>" + step.time + "</STEP_TIME>";
            string += "<STEP_TEMP>" + step.temp + "</STEP_TEMP>";
            string += "<INFUSE_AMOUNT>0</INFUSE_AMOUNT>";
            string += "</MASH_STEP>";
        });
        string += "</MASH_STEPS>";
        string += "</MASH>";
        string += "<NOTES>" + recipe.notes + "</NOTES>";
        string += "</RECIPE></RECIPES>";
        
        xml = parser.parseFromString(string, "application/xml");
        console.log(xml);
        return string;
    };
    
    $scope.save = function (recipe) {
        main.saveRecipe($scope.jb2xml(recipe), recipe.path);
    
    };
}]);



