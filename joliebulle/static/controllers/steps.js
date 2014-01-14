toolsApp.controller("StepAssistantCtrl", ['$scope', function ($scope) {
    "use strict";
    var targetTemp, addedVolume, grainWeight, mashTemp, waterVolumeMash, fudgeFactor, grainTemp, initialRatio, vm, temp, finalRatio, ratio, strikeTemp;
    
	$scope.stepTypes = ["Palier", "Empâtage"];
	$scope.stepType = 'Palier';
	$scope.targetTemp = 68;
	$scope.addedVolume = 10;
	$scope.grainWeight = 4;
	$scope.grainTemp = 20;
	$scope.mashTemp = 65;
	$scope.waterVolumeMash = 6;
	$scope.factor = 1.7;

	$scope.waterTemp = function () {
		if ($scope.stepType === 'Palier') {
			// Vm = Wgrain (0.4 + ratio)
            //Tstrike = (Ttarget*(Vstrike+Vm) - (Vm*Tmash)) / Vstrike
			targetTemp = parseFloat($scope.targetTemp);
			addedVolume = parseFloat($scope.addedVolume);
			grainWeight = parseFloat($scope.grainWeight);
			mashTemp = parseFloat($scope.mashTemp);
			waterVolumeMash = parseFloat($scope.waterVolumeMash);
			fudgeFactor = parseFloat($scope.factor);

			initialRatio = waterVolumeMash / grainWeight;
			vm = grainWeight * (initialRatio + 0.4);

			temp = ((targetTemp * (addedVolume + vm) - (vm * mashTemp)) / addedVolume) + fudgeFactor;

			finalRatio = (addedVolume + waterVolumeMash) / grainWeight;

			return {temp: (temp).toFixed(1), ratio: (finalRatio).toFixed(1)};
		} else {
            // Tstrike = [Ttarget + (0.4 * (Ttarget - Tgrain) / ratio)] + FF 
            targetTemp = parseFloat($scope.targetTemp);
            addedVolume = parseFloat($scope.addedVolume);
            grainWeight = parseFloat($scope.grainWeight);
            grainTemp = parseFloat($scope.grainTemp);
            fudgeFactor = parseFloat($scope.factor);
            ratio = addedVolume / grainWeight;

            strikeTemp = (targetTemp + (0.4 * (targetTemp - grainTemp) / ratio)) + fudgeFactor;

            return {temp: (strikeTemp).toFixed(1), ratio: (ratio).toFixed(1)};
        }
	};
}]);