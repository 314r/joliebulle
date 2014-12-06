toolsApp.controller('AlcToolCtrl', ['$scope', function ($scope) {
    "use strict";
    var abv, og, fg, sugar, appAtten;
    
    $scope.originalGravity = 1.001;
    $scope.finalGravity = 1.001;
    $scope.addedSugar = 0;
    
    $scope.calcAlcoolVol = function () {
/*
        ABV = ((((OG - FG) * 1.05) / FG) * 100) / 0.795 + ((Sugar * 0.5) / 0.795) / 10
*/
        og = parseFloat($scope.originalGravity);
        fg = parseFloat($scope.finalGravity);
        sugar = parseFloat($scope.addedSugar);
        
        abv = ((((og - fg) * 1.05) / fg) * 100) / 0.795 + ((sugar * 0.5) / 0.795) / 10;
        return abv.toFixed(1);
         
    };
    
    $scope.calcAppAttenuation = function () {
    
    /*
        Apparent Attenuation = 100 * (OG – FG)/(OG – 1)
    */
        og = parseFloat($scope.originalGravity);
        fg = parseFloat($scope.finalGravity);
        
        appAtten = 100 * (og - fg) / (og - 1);
        return appAtten.toFixed(1);
    };

	
}]);
