toolsApp.controller('BoiloffToolCtrl', ['$scope', function ($scope) {
    "use strict";
    var volPre, preBoilGravity, boilOffRate, boilTime, coolingLoss, volBoilOff, volPost, volCoolingLoss, finalVol, finalSg;
    
    $scope.preboilVol = 10;
    $scope.preboilGravity = 1.065;
    $scope.boilOffRate = 10;
    $scope.boilTime = 60;
    $scope.coolingLoss = 5;

	$scope.calcBoilOff = function () {
        
        volPre = $scope.preboilVol;
        preBoilGravity = $scope.preboilGravity;
        boilOffRate = $scope.boilOffRate;
        boilTime = $scope.boilTime;
        coolingLoss = $scope.coolingLoss;
        
        /*volume évaporé*/
        volBoilOff = volPre * (boilOffRate / 100) * (boilTime / 60);
        
        /*volume après ébu*/
        volPost = volPre - volBoilOff;
        
        /*pertes refroidissement*/
        volCoolingLoss = volPost * coolingLoss / 100;
        
        /*volume après refroidissement*/
        finalVol = volPost - volCoolingLoss;
        
        /*sg finale * volume final = (sg preEbu * vol preEbu) - vol manquant*/
        finalSg = ((preBoilGravity * volPre) - (volBoilOff + volCoolingLoss)) / finalVol;
        
        return {boilOffVol : volBoilOff.toFixed(1), coolingLoss : volCoolingLoss.toFixed(1), finalVol : finalVol.toFixed(1), finalSg : finalSg.toFixed(3)};
                
	};
}]);