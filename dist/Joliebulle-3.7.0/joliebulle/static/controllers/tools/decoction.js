toolsApp.controller('DecocToolCtrl', ['$scope', function ($scope) {
    "use strict";
    var fraction, targetTemp, startTemp, boilTemp, correction, decocVol, mashVol;
    
    $scope.mashVol = 10;
    $scope.targetTemp = 65;
    $scope.startTemp = 50;
    $scope.boilTemp = 100;
    $scope.correction = 15;
    

	$scope.calcDecoction = function () {
        /*decoction volume = total mash volume * (target temp - start temp) / (boil temp - start temp)*/
        
        mashVol = $scope.mashVol;
        targetTemp = $scope.targetTemp;
        startTemp = $scope.startTemp;
        boilTemp = $scope.boilTemp;
        correction = $scope.correction;
        
        fraction = (targetTemp - startTemp) / (boilTemp - startTemp);
        fraction += fraction * correction / 100;
        decocVol = fraction * mashVol;
        
        return {fraction : (fraction*100).toFixed(2), decocVol : decocVol.toFixed(2)};
	};
}]);



