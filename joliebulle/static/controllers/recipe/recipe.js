recipeApp.controller('RecipeCtrl', ['$scope', '$http', '$filter', function ($scope, $http, $filter) {
    "use strict";

    $scope.recipe = '';

    $scope.init = function (dataJson) {
        $scope.recipe = dataJson[0];
        $scope.genGraphProfile($scope.recipe);

    };
    
    $scope.genGraphProfile = function (recipe) {
        var stepsArray = $scope.recipe.mashProfile.steps;
        $scope.chartData = [];
        stepsArray.forEach(function (step) {
            if (step === stepsArray[0]) {
                $scope.chartData.push({"x" : (parseFloat(0) + " min"), "temp" : step.temp});
                $scope.chartData.push({"x" : (parseFloat(_.last($scope.chartData).x) + parseFloat(step.time)) + " min", "temp" : step.temp});
            } else {      
                $scope.chartData.push({"x" : (parseFloat(_.last($scope.chartData).x) + 5 + " min"), "temp" : step.temp});
                $scope.chartData.push({"x" : (parseFloat(_.last($scope.chartData).x) + parseFloat(step.time)) + " min", "temp" : step.temp});
            }
        });
        console.log($scope.chartData)
        return $scope.chartData;
    };
    
    $scope.xkey = 'x';
    $scope.ykeys = ['temp'];
}]);
