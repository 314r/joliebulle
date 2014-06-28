var beerCalc = (function () {
    var i, volPreCool, volPreBoil, ratio, gus, preBoilSg, strikeTemp, strikeVol, Vm, infuseVol, newRatio, grainRetentionVol, spargeVol, grainVolume, satGrain, volSat, waterAfterSat, mashVolume, mashVolumeStrike, mashVolumeLastStep, infusionSteps;
    return {
      
        preBoilCalc : function (coolingLossRate, boilOffRate, boilTime, volume) {
            volPreCool = volume / (1 - coolingLossRate);
            volPreBoil = volPreCool / (1 - (boilOffRate * boilTime / 60));
            return volPreBoil;
        },
        
        preBoilSgCalc : function (gravityUnits, volume, volPreBoil) {
            ratio = volume / volPreBoil;
            gus = gravityUnits * ratio;
            preBoilSg = 1 + (gus / 1000);
            return preBoilSg;
        },
        
        strikeTempCalc : function (fudgeFactor, grainTemp, targetTemp, ratio) {
            /*Tstrike = [targetTemp + (0.4 * (Ttarget - Tgrain) / ratio)] + FF  */
            strikeTemp = (targetTemp + (0.4 * (targetTemp - grainTemp) / ratio)) + fudgeFactor;
            return strikeTemp;
        },
        
        strikeVolCalc : function (grainWeight, ratio) {
            strikeVol = grainWeight * ratio / 1000;
            return strikeVol;
        },
        
        strikeVolreCalc : function (fudgeFactor, grainTemp, targetTemp, grainWeight, strikeTemp) {
            /*strike vol when temp changed*/
            grainWeight = grainWeight / 1000;
            strikeVol = 0.4 * grainWeight * (targetTemp - grainTemp) / (strikeTemp - targetTemp - fudgeFactor);
            return strikeVol;
        
        },
        
        infusionVolCalc : function (grainWeight, ratio, targetTemp, mashTemp, mashVolume, strikeTemp, fudgeFactor) {
            /*Vm = Wgrain (0.4 + ratio)
            Tstrike = (Ttarget*(Vstrike+Vm) - (Vm*Tmash)) / Vstrike*/
            Vm = (grainWeight / 1000) * (0.4 + ratio);
            strikeTemp = strikeTemp - fudgeFactor;
            infuseVol = ((targetTemp * Vm) - (Vm * mashTemp)) / (strikeTemp - targetTemp);
            newRatio = (mashVolume + infuseVol) / (grainWeight / 1000);
            return {"newRatio" : newRatio, "infuseVol" : infuseVol};
        },
        
        infusionTempCalc : function (grainWeight, ratio, targetTemp, mashTemp, mashVolume, strikeVol) {
            Vm = (grainWeight / 1000) * (0.4 + ratio);
            strikeTemp = ((targetTemp * (strikeVol + Vm)) - (Vm * mashTemp)) / strikeVol;
            return strikeTemp;
        },
        
        grainRetentionCalc : function (grainRetentionRate, grainWeight) {
            grainRetentionVol = grainRetentionRate * grainWeight / 1000;
            return grainRetentionVol;
        },
        
        spargeVolCalc : function (grainRetentionVol, volPreBoil, stepsVol) {
            spargeVol = volPreBoil - (stepsVol - grainRetentionVol);
            return spargeVol;
        },
        
        grainVolumeCalc : function (grainWeight) {
            grainVolume = grainWeight * 1.5 / 1000;
            return grainVolume;
        },
        
        mashVolumeCalc : function (grainWeight, strikeVol) {
            /* 1l water+ 500g grain = 1.325 l to saturate grain. After saturation add water vol. */
            satGrain = grainWeight * 2 / 1000;
            volSat = satGrain * 1.325;
            waterAfterSat = strikeVol - satGrain;
            mashVolume = volSat + waterAfterSat;
            return mashVolume;
        },
        
        mashVolumeLastStepCalc : function (mashVolumeStrike, strikeVol, mashVol) {
            mashVolumeLastStep = mashVolumeStrike + mashVol - strikeVol;
            return mashVolumeLastStep;
        },
        
        checkBiab : function (steps) {
            infusionSteps = 0;
            for (i = 0; i < steps.length; i += 1) {
                if (steps[i].type === "infusion") {
                    infusionSteps += 1;
                }
            }
            if (infusionSteps > 1) {
                return false;
            } else {
                return true;
            }
            
            
        }
    
    };
 
})();