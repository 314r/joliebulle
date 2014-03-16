recipesApp.controller('RecipeslibCtrl', ['$scope','$http', '$filter', function ($scope,$http,$filter) {
    "use strict";


    $scope.$watch('dataJson', function () {
        $scope.recipes = $scope.dataJson;
        // $scope.recipes = _.sortBy($scope.recipes, 'author').reverse();
        return $scope.recipes;
    });

    $scope.deleteLib = function (recipe) {
		$scope.recipes.splice($scope.recipes.indexOf(recipe), 1);
		main.deleteLib(recipe.path);	
    };

    $scope.openRecipeClicked = function (recipe) {
    	main.viewRecipeLib(recipe.path);
    	console.log("reçu")
    };




}]);
