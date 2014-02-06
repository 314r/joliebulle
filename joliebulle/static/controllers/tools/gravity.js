toolsApp.controller('GravityToolCtrl', ['$scope', function ($scope) {
    "use strict";
    var measuredGravity, calibTemp, sampleTemp, correctionFactor;
    
	$scope.measuredGravity = 1.035;
	$scope.calibTemp = 20;
	$scope.sampleTemp = 70;

	$scope.calcGravity = function () {
        measuredGravity = parseFloat($scope.measuredGravity);
        calibTemp = parseFloat($scope.calibTemp);
        sampleTemp = parseFloat($scope.sampleTemp);

        correctionFactor = ((measuredGravity - (calibTemp + 288.9414) / (508929.2 * (calibTemp + 68.12963)) * Math.pow((calibTemp - 3.9863), 2)) / (1 - (sampleTemp + 288.9414) / (508929.2 * (sampleTemp + 68.12963)) * Math.pow((sampleTemp - 3.9863), 2))) - measuredGravity;

		return (measuredGravity + correctionFactor).toFixed(3);
	};
}]);



