toolsApp.controller('DilutionToolCtrl', ['$scope', function ($scope) {
    "use strict";
    var initialVol, initialGravity, addedVolume, addedGravity, finalVol, finalGravity;
    
    $scope.initialVol = 0;
    $scope.initialGravity = 1.010;
    $scope.addedVolume = 0;
    $scope.addedGravity = 1;
    $scope.finalVol = 0;

    
    $scope.calcDilution = function () {
        
        /*volumeFinal*densFinale = (volumeInitial*densInitiale) + (volumeAjoute*densAjout)*/
        
        initialVol = parseFloat($scope.initialVol);
        initialGravity = parseFloat($scope.initialGravity);
        addedVolume = parseFloat($scope.addedVolume);
        addedGravity = parseFloat($scope.addedGravity);
        finalVol = initialVol + addedVolume;
        $scope.finalVol = finalVol;
        
        if (finalVol === 0) {
            finalGravity = 0;
        } else {
            finalGravity = ((initialVol * initialGravity) + (addedVolume * addedGravity)) / finalVol;
        }
    
        return finalGravity.toFixed(3);
    };
    
    
    
    $scope.finalVolChanged = function () {
        $scope.addedVolume = $scope.finalVol - $scope.initialVol;
    };
    
    
    
    
    
	
}]);