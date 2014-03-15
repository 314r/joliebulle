recipesApp.controller('RecipeslibCtrl', ['$scope','$http', '$filter', function ($scope,$http,$filter) {
    "use strict";


    $scope.$watch('dataJson', function () {
        $scope.recipes = $scope.dataJson;
        return $scope.recipes;
});




}]);
