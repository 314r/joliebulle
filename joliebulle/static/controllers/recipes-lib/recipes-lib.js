recipesApp.controller('RecipeslibCtrl', ['$scope','$http', '$filter', function ($scope,$http,$filter) {
    "use strict";
    $scope.active = false;

    $scope.$watch('dataJson', function () {
        $scope.recipes = $scope.dataJson;
        $scope.recipes = _.chain($scope.recipes)
            .sortBy(function(o){return o.name.toLowerCase();})
            .sortBy(function(o){return o.author.toLowerCase();})
            .value();
        return $scope.recipes;
    });

    $scope.deleteLib = function (recipe) {
		$scope.recipes.splice($scope.recipes.indexOf(recipe), 1);
		main.deleteLib(recipe.path);	
    };

    $scope.openRecipeClicked = function (recipe) {
    	main.viewRecipeLib(recipe.path);
    	
    };
    $scope.recipeSelected = function (recipe) {
        $scope.active = true;
        $scope.currentRecipe = recipe;
        main.viewRecipeLib(recipe.path);
        
    };








}]);
