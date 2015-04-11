/*jslint nomen: true */
var beerCalc = (function () {
    "use strict";
    var i, volPreCool, volPreBoil, ratio, gus, preBoilSg, strikeTemp, strikeVol, Vm, infuseVol, newRatio, grainRetentionVol, spargeVol, grainVolume, satGrain, volSat, waterAfterSat, mashVolume, mashVolumeStrike, mashVolumeLastStep, infusionSteps, ebc, mcu, mcuTot, _sugars, sugarEquivalents, _equivSugar, _gravityUnits, _originalGravity;
    
    _equivSugar = function (fermentable) {
        return (fermentable.amount / 1000) * (fermentable.fyield / 100);
    };

    _sugars = function (fermentables) {
        sugarEquivalents = {
            totalSugars : 0,
            mashedSugars : 0,
            nonMashedSugars : 0,
            preBoilSugars : 0,
            preBoilMashed : 0,
            preBoilNonMashed : 0
        };
        fermentables.forEach(function (fermentable) {
            sugarEquivalents.totalSugars +=  _equivSugar(fermentable);
            if (fermentable.type === "Sugar" || fermentable.type === "Dry Extract" || fermentable.type === "Extract") {
                sugarEquivalents.nonMashedSugars +=  _equivSugar(fermentable);
            } else {
                sugarEquivalents.mashedSugars +=  _equivSugar(fermentable);
            }

            /* Sugars added after boil, to compute pre-boil gravity. Impact on IBU.  */
            if (fermentable.afterBoil === 'false') {
                sugarEquivalents.preBoilSugars += _equivSugar(fermentable);
                if (fermentable.type === "Sugar" || fermentable.type === "Dry Extract" || fermentable.type === "Extract") {
                    sugarEquivalents.preBoilNonMashed += _equivSugar(fermentable);
                } else {
                    sugarEquivalents.preBoilMashed += _equivSugar(fermentable);
                }
            }
            
        });
        return sugarEquivalents;
    };

    _gravityUnits = function (fermentables, volume, efficiency) {
        return (383.89 * _sugars(fermentables).mashedSugars / volume) * (efficiency / 100) + (383.89 * _sugars(fermentables).nonMashedSugars / volume);
    };

    _originalGravity = function (recipe) {
        return 1 + (_gravityUnits(recipe.fermentables, recipe.volume, recipe.efficiency) / 1000);
    };


    return {

        ebc : function (fermentables, volume) {
/*          calcul de la couleur
            calcul du MCU pour chaque grain :
            MCU=4.23*EBC(grain)*Poids grain(Kg)/Volume(L)
            puis addition de tous les MCU
            puis calcul EBC total :
            EBC=2.939*MCU^0.6859*/
            mcuTot = 0;
            fermentables.forEach(function (fermentable) {
                mcu = 4.23 * fermentable.color * (fermentable.amount / 1000) / volume;
                mcuTot = mcuTot + mcu;
            });
            ebc = 2.939 * Math.pow(mcuTot, 0.6859);
            return ebc;
        },

        sugars : function (fermentables) {
            return _sugars(fermentables);
        },

        originalGravity : function (recipe) {
            return _originalGravity(recipe);
        },
      
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
}());