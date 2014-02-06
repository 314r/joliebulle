toolsApp.controller('SgPlatoToolCtrl', ['$scope', function ($scope) {
    "use strict";
    var plato, sg;
    
    $scope.specificGravity = 1.085 ;
    $scope.plato = 20.5;
    

    $scope.platoChanged = function () {
        plato = parseFloat($scope.plato);
        sg = 1 + (plato / (258.6 - ((plato / 258.2) * 227.1)));
        $scope.specificGravity = Math.round(sg*1000)/1000;
        };

    $scope.sgChanged = function () {
        sg = $scope.specificGravity;
        plato = (1111.14 * sg) - (630.272 * Math.pow(sg,2)) + (135.997 * Math.pow(sg,3)) - 616.868;
        $scope.plato = Math.round(plato*10)/10;
        };
}]);



