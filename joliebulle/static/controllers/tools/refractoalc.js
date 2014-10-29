toolsApp.controller('RefractoAlcToolCtrl', ['$scope', function ($scope) {
    "use strict";
    var fg;
/*
    FG = 1.0000 – 0.0044993*RIi + 0.011774*RIf + 0.00027581*RIi² – 0.0012717*RIf² – 0.0000072800*RIi³ + 0.000063293*RIf³
    http://seanterrill.com/2011/04/07/refractometer-fg-results/
*/
    $scope.wortFactor = 1.00;
    $scope.originalRi = 15;
    $scope.finalRi = 15;
    
    $scope.calcFgRefracto = function () {
        fg = 1.0000 - 0.0044993 * $scope.originalRi / $scope.wortFactor + 0.011774 * $scope.finalRi / $scope.wortFactor + 0.00027581 * Math.pow($scope.originalRi / $scope.wortFactor, 2) -  0.0012717 * Math.pow($scope.finalRi / $scope.wortFactor, 2) - 0.0000072800 * Math.pow($scope.originalRi / $scope.wortFactor, 3) +  0.000063293 * Math.pow($scope.finalRi / $scope.wortFactor, 3);
        fg = Math.round(fg*10000)/10000;
        return fg;
    };

}]);