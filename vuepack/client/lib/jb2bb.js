/*jslint nomen: true */
var jb2bb = (function () {
	"use strict";
	var string;
	return {

		exportString : function (recipe) {
			string = "[b]" + recipe.name + "\n";
			string += "[i]" + recipe.style + "[/i][/b] \n";
			string += "\n";

			string += "Densité initiale : " + recipe.og + "\n";
			string += "Densité finale : " + recipe.fg + "\n";
			string += "Teinte : " + recipe.ebc + " EBC \n";
			string += "Amertume : " + recipe.ibu + "IBU \n";
			string += "Alcool (vol) : " + recipe.alc + " % \n";
			string += "\n";

			string += "Rendement prévu : " + recipe.efficiency + " %" + "\n";
			string += "Ingrédients prévus pour un volume de " + recipe.volume + " litres" + "\n";
			string += "\n";

			string += "[b]Grains et sucres \n";
			string += "------------------------ [/b] \n";
			recipe.fermentables.forEach(function (fermentable) {
				string += fermentable.amount + " g " + fermentable.name + "\n";
			});
			string += "\n";

			string += "[b]Houblons \n";
			string += "------------------------ [/b] \n";
		        recipe.hops.forEach(function (hop) {
                            var unit_time = "min";
                            if (hop.use === 'Dry Hop') {
                                unit_time = "jours";
                            }
			    string += hop.amount + " g " + hop.name + " (α" + hop.alpha + "%, " + hop.formView + ") @ " + hop.time + " " + unit_time + " (" + hop.useView + ")" + "\n";
			});
			string += "\n";

			string += "[b]Divers \n";
			string += "------------------------ [/b] \n";
			recipe.miscs.forEach(function (misc) {
				string += misc.amount + " g " + misc.name + "@ " + misc.time + " min" + "\n";
			});
			string += "\n";

			string += "[b]Levures \n";
			string += "------------------------ [/b] \n";
			recipe.yeasts.forEach(function (yeast) {
				string += yeast.name + " " + yeast.labo + " — " + yeast.product_id + " (" + yeast.formView + ")" + "\n";
			});
			string += "\n";

			string += "[b]Brassage \n";
			string += "------------------------ [/b] \n";
			string += recipe.mashProfile.name + "\n";
			string += "pH : " + recipe.mashProfile.ph + "\n";
			string += "\n";
			string += "Étapes :" + "\n";
			recipe.mashProfile.steps.forEach(function (step) {
				string += step.name + " : palier de type " + step.type + " à " + step.temp + " °C pendant " + step.time + " minutes" + "\n";
			});
			string += "\n";
			string += "Rinçage : " + recipe.mashProfile.sparge + " °C \n";
			string += "\n";

			string += "[b]Notes \n";
			string += "------------------------ [/b] \n";
			string += recipe.notes;

	        return string;

		}





	};
}());
