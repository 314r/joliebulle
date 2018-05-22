const _ = require('underscore')

const _equivSugar = function (fermentable) {
  return (fermentable.amount / 1000) * (fermentable.yield / 100)
}

const _colorArray = function () {
  const array = ['FFE699', 'FFD878', 'FFCA5A', 'FFBF42', 'FBB123', 'F8A600', 'F39C00', 'EA8F00', 'E58500', 'DE7C00', 'D77200', 'CF6900', 'CB6200', 'C35900', 'BB5100', 'B54C00', 'B04500', 'A63E00', 'A13700', '9B3200', '952D00', '8E2900', '882300', '821E00', '7B1A00', '771900', '701400', '6A0E00', '660D00', '5E0B00', '5A0A02', '600903', '520907', '4C0505', '470606', '440607', '3F0708', '3B0607', '3A070B', '36080A']
  return array
}

const _sugars = function (fermentables) {
  var sugarEquivalents = {
    totalSugars: 0,
    mashedSugars: 0,
    nonMashedSugars: 0,
    preBoilSugars: 0,
    preBoilMashed: 0,
    preBoilNonMashed: 0
  }
  fermentables.forEach(function (fermentable) {
    sugarEquivalents.totalSugars += _equivSugar(fermentable)
    if (fermentable.type === 'Sugar' || fermentable.type === 'Dry Extract' || fermentable.type === 'Extract') {
      sugarEquivalents.nonMashedSugars += _equivSugar(fermentable)
    } else {
      sugarEquivalents.mashedSugars += _equivSugar(fermentable)
      console.log(sugarEquivalents)
    }

        /* Sugars added after boil, to compute pre-boil gravity. Impact on IBU.  */
    if (fermentable.add_after_boil === 'FALSE') {
      sugarEquivalents.preBoilSugars += _equivSugar(fermentable)
      if (fermentable.type === 'Sugar' || fermentable.type === 'Dry Extract' || fermentable.type === 'Extract') {
        sugarEquivalents.preBoilNonMashed += _equivSugar(fermentable)
      } else {
        sugarEquivalents.preBoilMashed += _equivSugar(fermentable)
      }
    }
  })

  return sugarEquivalents
}

const _gravityUnits = function (fermentables, volume, efficiency) {
  return (383.89 * _sugars(fermentables).mashedSugars / volume) * (efficiency / 100) + (383.89 * _sugars(fermentables).nonMashedSugars / volume)
}

const _preBoilGravityUnits = function (fermentables, volume, efficiency) {
  return (383.89 * _sugars(fermentables).preBoilMashed / volume) * (efficiency / 100) + (383.89 * _sugars(fermentables).preBoilNonMashed / volume)
}

const _preBoilGravity = function (fermentables, volume, efficiency) {
  return 1 + (_preBoilGravityUnits(fermentables, volume, efficiency) / 1000)
}

const _originalGravity = function (recipe) {
  return 1 + (_gravityUnits(recipe.fermentables, recipe.batch_size, recipe.efficiency) / 1000)
}

const _ibus = function (recipe) {
/*      #Tinseth method
    #IBUs = decimal alpha acid utilization * mg/l of added alpha acids

    #mg/l of added alpha acids = decimal AA rating * grams hops * 1000 / liters of wort
    #Decimal Alpha Acid Utilization = Bigness Factor * Boil Time Factor
    #Bigness factor = 1.65 * 0.000125^(wort gravity - 1)
    #Boil Time factor = 1 - e^(-0.04 * time in mins) / 4.15
    */
  let totalIbus = 0
  let ibu
  const bignessFactor = 1.65 * (Math.pow(0.000125, (_preBoilGravity(recipe.fermentables, recipe.batch_size, recipe.efficiency) - 1)))
  recipe.hops.forEach(function (hop) {
    const btFactor = (1 - Math.pow(2.71828182845904523536, (-0.04 * hop.time))) / 4.15
    const decimalUtil = btFactor * bignessFactor
    const mgAcid = (hop.alpha / 100) * (hop.amount * 1000) / recipe.batch_size

    if (hop.use !== 'Dry Hop') {
      ibu = mgAcid * decimalUtil
      if (hop.form === 'Pellet') {
        ibu = ibu + 0.1 * ibu
      }
    } else {
      ibu = 0
    }

    if (hop.use === 'Aroma') {
      ibu = 0.5 * ibu
    }

    totalIbus += ibu
    hop.ibuPart = ibu
  })
  recipe.ibu = totalIbus
  return recipe
}

export function ebc (fermentables, volume) {
/*          calcul de la couleur
        calcul du MCU pour chaque grain :
        MCU=4.23*EBC(grain)*Poids grain(Kg)/Volume(L)
        puis addition de tous les MCU
        puis calcul EBC total :
        EBC=2.939*MCU^0.6859*/
  let mcuTot = 0
  let mcu
  fermentables.forEach(function (fermentable) {
    mcu = 4.23 * fermentable.color * (fermentable.amount / 1000) / volume
    mcuTot = mcuTot + mcu
  })
  const ebc = 2.939 * Math.pow(mcuTot, 0.6859)
  return ebc
}

export function sugars (fermentables) {
  return _sugars(fermentables)
}

export function weight (fermentables) {
  let weight = 0
  fermentables.forEach(function (fermentable) {
    if (fermentable.type === 'Grain') {
      weight += fermentable.amount
    }
  })
  return weight
}

export function originalGravity (recipe) {
  return _originalGravity(recipe)
}

export function finalGravity (recipe) {
        /* Use the highest attenuation in a list of yeasts */
  let hiAtten
  try {
    recipe.yeasts = _.sortBy(recipe.yeasts, 'attenuation')
    hiAtten = _.last(recipe.yeasts).attenuation
  } catch (e) {
    hiAtten = 75
  }

  if (hiAtten === 'undefined') {
    hiAtten = 75
  }
  hiAtten = hiAtten / 100
  const gu = _gravityUnits(recipe.fermentables, recipe.batch_size, recipe.efficiency) * (1 - hiAtten)
  return 1 + gu / 1000
}

export function ibus (recipe) {
  return _ibus(recipe)
}

export function gu (recipe) {
  return _gravityUnits(recipe.fermentables, recipe.batch_size, recipe.efficiency)
}

export function preBoilGu (recipe) {
  return _preBoilGravityUnits(recipe.fermentables, recipe.batch_size, recipe.efficiency)
}

export function bugu (recipe) {
  if (recipe.ibu === 'undefined') {
    recipe.ibu = 0
  }
  return recipe.ibu / _gravityUnits(recipe.fermentables, recipe.batch_size, recipe.efficiency)
}

export function alc (recipe) {
    /* ABV = 0.130((OG-1)-(FG-1))*1000 */
  return 0.130 * ((recipe.og - 1) - (recipe.fg - 1)) * 1000
}

export function preBoilCalc (coolingLossRate, boilOffRate, boilTime, volume) {
  const volPreCool = volume / (1 - coolingLossRate)
  const volPreBoil = volPreCool / (1 - (boilOffRate * boilTime / 60))
  return volPreBoil
}

export function preBoilSgCalc (gravityUnits, volume, volPreBoil) {
  const ratio = volume / volPreBoil
  const gus = gravityUnits * ratio
  const preBoilSg = 1 + (gus / 1000)
  return preBoilSg
}

export function strikeTempCalc (fudgeFactor, grainTemp, targetTemp, ratio) {
        /* Tstrike = [targetTemp + (0.4 * (Ttarget - Tgrain) / ratio)] + FF  */
  const strikeTemp = (targetTemp + (0.4 * (targetTemp - grainTemp) / ratio)) + fudgeFactor
  return strikeTemp
}

export function strikeVolCalc (grainWeight, ratio) {
  const strikeVol = grainWeight * ratio / 1000
  return strikeVol
}

export function strikeVolreCalc (fudgeFactor, grainTemp, targetTemp, grainWeight, strikeTemp) {
        /* strike vol when temp changed*/
  grainWeight = grainWeight / 1000
  const strikeVol = 0.4 * grainWeight * (targetTemp - grainTemp) / (strikeTemp - targetTemp - fudgeFactor)
  return strikeVol
}

export function infusionVolCalc (grainWeight, ratio, targetTemp, mashTemp, mashVolume, strikeTemp, fudgeFactor) {
        /* Vm = Wgrain (0.4 + ratio)
        Tstrike = (Ttarget*(Vstrike+Vm) - (Vm*Tmash)) / Vstrike*/
  const Vm = (grainWeight / 1000) * (0.4 + ratio)
  strikeTemp = strikeTemp - fudgeFactor
  const infuseVol = ((targetTemp * Vm) - (Vm * mashTemp)) / (strikeTemp - targetTemp)
  const newRatio = (mashVolume + infuseVol) / (grainWeight / 1000)
  return { 'newRatio': newRatio, 'infuseVol': infuseVol }
}

export function infusionTempCalc (grainWeight, ratio, targetTemp, mashTemp, mashVolume, strikeVol) {
  const Vm = (grainWeight / 1000) * (0.4 + ratio)
  const strikeTemp = ((targetTemp * (strikeVol + Vm)) - (Vm * mashTemp)) / strikeVol
  return strikeTemp
}

export function grainRetentionCalc (grainRetentionRate, grainWeight) {
  const grainRetentionVol = grainRetentionRate * grainWeight / 1000
  return grainRetentionVol
}

export function spargeVolCalc (grainRetentionVol, volPreBoil, stepsVol) {
  const spargeVol = volPreBoil - (stepsVol - grainRetentionVol)
  return spargeVol
}

export function grainVolumeCalc (grainWeight) {
  const grainVolume = grainWeight * 1.5 / 1000
  return grainVolume
}

export function mashVolumeCalc (grainWeight, strikeVol) {
        /* 1l water+ 500g grain = 1.325 l to saturate grain. After saturation add water vol. */
  const satGrain = grainWeight * 2 / 1000
  const volSat = satGrain * 1.325
  const waterAfterSat = strikeVol - satGrain
  const mashVolume = volSat + waterAfterSat
  return mashVolume
}

export function mashVolumeLastStepCalc (mashVolumeStrike, strikeVol, mashVol) {
  const mashVolumeLastStep = mashVolumeStrike + mashVol - strikeVol
  return mashVolumeLastStep
}

export function checkBiab (steps) {
  let infusionSteps = 0
  let i
  for (i = 0; i < steps.length; i += 1) {
    if (steps[i].type === 'Infusion') {
      infusionSteps += 1
    }
  }
  if (infusionSteps > 1) {
    return false
  } else {
    return true
  }
}

export function biabCalc (preBoilVol, grainWeight, config, target) {
  const strikeVol = preBoilVol + grainRetentionCalc(config.GrainRetention, grainWeight)
  const biabRatio = strikeVol / (grainWeight / 1000)
  const biabTemp = strikeTempCalc(parseFloat(config.FudgeFactor), parseFloat(config.GrainTemp), target, biabRatio)
  return { targetTemp: target, strikeVol: strikeVol, ratio: biabRatio, temp: biabTemp }
}

export function scaleIngredients (ratio, fermentables, hops, miscs) {
  fermentables = fermentables.map(function (item) {
    item.amount *= ratio
    return item
  })
  hops = hops.map(function (item) {
    item.amount *= ratio
    return item
  })
  miscs = miscs.map(function (item) {
    item.amount *= ratio
    return item
  })
}

export function ingRatio (ingredients, amount) {
  let weight = 0
  ingredients.forEach(function (ingredient) {
    weight += ingredient.amount
  })
  const ratio = amount / weight
  return ratio
}

export function colorHtml (ebc) {
  let colorId
  const srm = Math.round(parseFloat(ebc) / 1.97)
  if (srm <= 1) {
    colorId = '#' + _colorArray()[0]
  } else if (srm >= 30) {
    colorId = '#' + _colorArray()[30]
  } else {
    colorId = '#' + _colorArray()[srm - 1]
  }

  return colorId
}
