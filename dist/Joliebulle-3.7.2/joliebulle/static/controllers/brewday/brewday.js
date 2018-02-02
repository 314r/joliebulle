brewdayApp.controller('BrewdayCtrl', ['$scope', '$http', '$filter', function ($scope, $http, $filter) {
    "use strict";

    var i, j, ratio, waterVol, mashVolume, strikeTemp, mashTemp, infusionCalc, element, index, list, step, sumWaterVol, volSteps, grainRetentionVol, spargeVol, grainVolume, strikeVol;

    $scope.editMode = false;
    $scope.brewType = "classic";

    $scope.init = function (dataJson) {
        $scope.data = dataJson;
        $scope.steps = $scope.data.mashProfile.steps;
        $scope.steps[0].ratio = 3;
        _.each($scope.steps, $scope.stepsCalc);

    };


    $scope.preBoilVol = function () {
        return beerCalc.preBoilCalc(parseFloat($scope.data.coolingLossRate) / 100, parseFloat($scope.data.boilOffRate) / 100, parseFloat($scope.data.boilTime), parseFloat($scope.data.volume));
    };

    $scope.preBoilSg = function () {
        return beerCalc.preBoilSgCalc(parseFloat($scope.data.preBoilGu), parseFloat($scope.data.volume), $scope.preBoilVol()).toFixed(3);
    };

    $scope.strikeTemp = function (ratio) {
        return beerCalc.strikeTempCalc(parseFloat($scope.data.fudgeFactor), parseFloat($scope.data.grainTemp), parseFloat($scope.data.mashProfile.steps[0].temp), ratio);
    };

    $scope.stepsCalc = function (step, index, array) {
        if (index === 0) {
            ratio = step.ratio;
            
            waterVol = beerCalc.strikeVolCalc(parseFloat($scope.data.grainWeight), ratio);
            step.waterVol = Math.round(waterVol * 10) / 10;
            step.waterTemp = Math.round($scope.strikeTemp(ratio) * 10) / 10;
            $scope.steps[index] = step;
        } else if (index !== 0 && step.type === "Temperature") {
            step.ratio = $scope.steps[index - 1].ratio;
            step.waterVol = 0;
            $scope.steps[index] = step;
        } else if (index !== 0 && step.type === "Infusion") {
            strikeTemp = 90;
            mashTemp = $scope.steps[index - 1].temp;
            ratio = $scope.steps[index - 1].ratio;
            mashVolume = 0;
            for (i = 0; i < index; i += 1) {
                mashVolume = mashVolume + $scope.steps[i].waterVol;
            }
            infusionCalc = beerCalc.infusionVolCalc(parseFloat($scope.data.grainWeight), ratio, parseFloat(step.temp), mashTemp, mashVolume, strikeTemp, parseFloat($scope.data.fudgeFactor));
            step.ratio = Math.round(infusionCalc.newRatio * 10) / 10;
            step.waterVol = Math.round(infusionCalc.infuseVol * 10) / 10;
            step.waterTemp = Math.round(strikeTemp * 10) / 10;
            $scope.steps[index] = step;
        }
    };
    
    $scope.biabCalc = function () {
        console.log(beerCalc.checkBiab($scope.steps));
        strikeVol = $scope.preBoilVol() + beerCalc.grainRetentionCalc(parseFloat($scope.data.grainRetention), parseFloat($scope.data.grainWeight));
        ratio = strikeVol / (parseFloat($scope.data.grainWeight) / 1000);
        strikeTemp = $scope.strikeTemp(ratio);
        $scope.steps[0].ratio = Math.round(ratio * 10) / 10;
        $scope.steps[0].waterTemp = Math.round(strikeTemp * 10) / 10;
        $scope.steps[0].waterVol = Math.round(strikeVol * 10) / 10;
         
    };

    $scope.ratioChanged = function (index) {
        step = $scope.steps[index];
        sumWaterVol = 0;
        for (i = 0; i < $scope.steps.slice(0, index).length; i += 1) {
            sumWaterVol += $scope.steps[i].waterVol;
        }
        step.waterVol = (parseFloat($scope.data.grainWeight) * step.ratio / 1000) - sumWaterVol;
        step.waterVol = Math.round(step.waterVol * 10) / 10;
        $scope.steps[index] = step;
        if (index === 0) {
            _.each($scope.steps, $scope.stepsCalc);
        } else if (index !== 0 && step.type === "Infusion") {
            mashTemp = $scope.steps[index - 1].temp;
            mashVolume = 0;
            for (i = 0; i < index; i += 1) {
                mashVolume = mashVolume + $scope.steps[i].waterVol;
            }
            step.waterTemp = beerCalc.infusionTempCalc(parseFloat($scope.data.grainWeight), $scope.steps[index - 1].ratio, parseFloat(step.temp), mashTemp, mashVolume, step.waterVol);
            step.waterTemp = Math.round(step.waterTemp * 10) / 10;
            $scope.steps[index] = step;

            for (i = index + 1; i < $scope.steps.length; i += 1) {
                if ($scope.steps[i].type === "Temperature") {
                    $scope.steps[i].ratio = $scope.steps[i - 1].ratio;
                } else if ($scope.steps[i].type === "Infusion") {
                    strikeTemp = 90;
                    mashTemp = $scope.steps[i - 1].temp;
                    mashVolume = 0;
                    for (j = 0; j < $scope.steps.slice(0, index + 1).length; j += 1) {
                        mashVolume += $scope.steps[j].waterVol;
                    }
                    infusionCalc = beerCalc.infusionVolCalc(parseFloat($scope.data.grainWeight), $scope.steps[i - 1].ratio, parseFloat($scope.steps[i].temp), mashTemp, mashVolume, strikeTemp, parseFloat($scope.data.fudgeFactor));

                    $scope.steps[i].ratio = Math.round(infusionCalc.newRatio * 10) / 10;
                    $scope.steps[i].waterVol = Math.round(infusionCalc.infuseVol * 10) / 10;
                }
            }
        }
    };


    $scope.tempChanged = function (index) {
        step = $scope.steps[index];
        if (index === 0) {
            waterVol = beerCalc.strikeVolreCalc(parseFloat($scope.data.fudgeFactor), parseFloat($scope.data.grainTemp), parseFloat(step.temp), parseFloat($scope.data.grainWeight), parseFloat(step.waterTemp));
            step.waterVol = Math.round(waterVol * 10) / 10;
            step.ratio = waterVol / (parseFloat($scope.data.grainWeight) / 1000);
            step.ratio = Math.round(step.ratio * 10) / 10;
            $scope.steps[index] = step;
        } else if (index !== 0 && step.type === "Infusion") {
            mashTemp = $scope.steps[index - 1].temp;
            ratio = $scope.steps[index - 1].ratio;
            mashVolume = 0;
            for (i = 0; i < index; i += 1) {
                mashVolume = mashVolume + $scope.steps[i].waterVol;
            }
            strikeTemp = step.waterTemp;

            infusionCalc = beerCalc.infusionVolCalc(parseFloat($scope.data.grainWeight), ratio, parseFloat(step.temp), mashTemp, mashVolume, strikeTemp, parseFloat($scope.data.fudgeFactor));

            step.ratio = Math.round(infusionCalc.newRatio * 10) / 10;
            step.waterVol = Math.round(infusionCalc.infuseVol * 10) / 10;
            $scope.steps[index] = step;
        }

        for (i = index + 1; i < $scope.steps.length; i += 1) {
            if ($scope.steps[i].type === "Temperature") {
                $scope.steps[i].ratio = $scope.steps[i - 1].ratio;
            } else if ($scope.steps[i].type === "Infusion") {
                strikeTemp = 90;
                mashTemp = $scope.steps[i - 1].temp;
                mashVolume = 0;
                for (j = 0; j < $scope.steps.slice(0, index + 1).length; j += 1) {
                    mashVolume += $scope.steps[j].waterVol;
                }
                infusionCalc = beerCalc.infusionVolCalc(parseFloat($scope.data.grainWeight), $scope.steps[i - 1].ratio, parseFloat($scope.steps[i].temp), mashTemp, mashVolume, strikeTemp, parseFloat($scope.data.fudgeFactor));
                $scope.steps[i].ratio = Math.round(infusionCalc.newRatio * 10) / 10;
                $scope.steps[i].waterVol = Math.round(infusionCalc.infuseVol * 10) / 10;
            }
        }

    };

    $scope.volChanged = function (index) {
        step = $scope.steps[index];
        mashVolume = 0;
        for (i = 0; i < index; i += 1) {
            mashVolume = mashVolume + $scope.steps[i].waterVol;
        }
        mashVolume += step.waterVol;
        step.ratio = mashVolume / (parseFloat($scope.data.grainWeight) / 1000);
        $scope.steps[index] = step;
        $scope.ratioChanged(index);
    };


    $scope.spargeVol = function () {
        grainRetentionVol = beerCalc.grainRetentionCalc(parseFloat($scope.data.grainRetention), parseFloat($scope.data.grainWeight));
        volSteps = 0;
        for (i = 0; i < $scope.steps.length; i += 1) {
            volSteps += parseFloat($scope.steps[i].waterVol);
        }
        spargeVol = beerCalc.spargeVolCalc(grainRetentionVol, $scope.preBoilVol(), volSteps);
        return spargeVol;

    };

    $scope.grainVolume = function () {
        grainVolume = beerCalc.grainVolumeCalc(parseFloat($scope.data.grainWeight));
        return grainVolume;
    };

    $scope.mashVolumeStrike = function () {
        mashVolume = beerCalc.mashVolumeCalc(parseFloat($scope.data.grainWeight), parseFloat($scope.steps[0].waterVol));
        return mashVolume;
    };

    $scope.mashVolumeLastStep = function () {
        volSteps = 0;
        for (i = 0; i < $scope.steps.length; i += 1) {
            volSteps += parseFloat($scope.steps[i].waterVol);
        }
        mashVolume = beerCalc.mashVolumeLastStepCalc($scope.mashVolumeStrike(), parseFloat($scope.steps[0].waterVol), volSteps);
        return mashVolume;
    };

    $scope.brewTypeChanged = function () {
        if ($scope.brewType === "classic") {
            $scope.invalidBiab = false;
            $scope.steps[0].ratio = 3;
            _.each($scope.steps, $scope.stepsCalc);
        } else if ($scope.brewType === "biab") {
            if (beerCalc.checkBiab($scope.steps) === true) {
                $scope.biabCalc();
            } else {
                $scope.invalidBiab = true;
            }
        }

    };

    $scope.preBoilCheck = function () {
        main.preBoilCheck($scope.preBoilVol(),$scope.preBoilSg(), parseFloat($scope.data.gu), $scope.data.volume);
    };

    $scope.printBrewday = function (){
        main.printBrewday();

    };



}]);
