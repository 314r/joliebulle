/*jslint nomen: true */
var jb2xml = (function () {
	"use strict";
	var parser, string, xml;
	return {

		exportString : function (recipe) {
			parser = new DOMParser();
	        string = "<RECIPES><RECIPE>";
	        string += "<NAME>" + recipe.name + "</NAME>";
	        string += "<VERSION>1</VERSION>";
	        string += "<TYPE>" + recipe.type + "</TYPE>";
	        string += "<BREWER>" + recipe.brewer + "</BREWER>";
	        string += "<STYLE><NAME>" + recipe.style + "</NAME><VERSION>1</VERSION><CATEGORY /><CATEGORY_NUMBER /><STYLE_LETTER /><STYLE_GUIDE /><TYPE /><OG_MIN /><OG_MAX /><FG_MIN /><FG_MAX /><IBU_MIN /><IBU_MAX /><COLOR_MIN /><COLOR_MAX /></STYLE>";
	        string += "<BATCH_SIZE>" + recipe.volume + "</BATCH_SIZE>";
	        string += "<BOIL_SIZE />";
	        string += "<BOIL_TIME>" + recipe.boilTime + "</BOIL_TIME>";
	        string += "<EFFICIENCY>" + recipe.efficiency + "</EFFICIENCY>";
	        string += "<OG>" + recipe.og + "</OG><FG>" + recipe.fg + "</FG>";
	        string += "<FERMENTABLES>";
	        recipe.fermentables.forEach(function (fermentable) {
	            string += "<FERMENTABLE>";
	            string += "<NAME>" + fermentable.name + "</NAME>";
	            string += "<VERSION>1</VERSION>";
	            string += "<AMOUNT>" + fermentable.amount / 1000 + "</AMOUNT>";
	            string += "<TYPE>" + fermentable.type + "</TYPE>";
	            string += "<YIELD>" + fermentable.fyield + "</YIELD>";
	            string += "<RECOMMEND_MASH>" + fermentable.recoMash + "</RECOMMEND_MASH>";
	            string += "<ADD_AFTER_BOIL>" + fermentable.afterBoil + "</ADD_AFTER_BOIL>";
	            string += "<COLOR>" + fermentable.color / 1.97 + "</COLOR>";
	            string += "</FERMENTABLE>";
	        });
	        string += "</FERMENTABLES>";
	        string += "<HOPS>";
	        recipe.hops.forEach(function (hop) {
	            string += "<HOP>";
	            string += "<NAME>" + hop.name + "</NAME>";
	            string += "<VERSION>1</VERSION>";
	            string += "<AMOUNT>" + hop.amount / 1000 + "</AMOUNT>";
	            if (hop.form === 0 || hop.form === 'Pellet') {
	                string += "<FORM>Pellet</FORM>";
	            } else if (hop.form === 1 || hop.form === 'Leaf') {
	                string += "<FORM>Leaf</FORM>";
	            } else if (hop.form === 2 || hop.form === 'Plug') {
	                string += "<FORM>Plug</FORM>";
	            }
	            string += "<TIME>" + hop.time + "</TIME>";
	            string += "<ALPHA>" + hop.alpha + "</ALPHA>";
	            string += "<USE>" + hop.use + "</USE>";
	            string += "</HOP>";

	        });
	        string += "</HOPS>";
	        string += "<YEASTS>";
	        recipe.yeasts.forEach(function (yeast) {
	            string += "<YEAST>";
	            string += "<NAME>" + yeast.name + "</NAME>";
	            string += "<VERSION>1</VERSION>";
	            string += "<TYPE />";
	            string += "<FORM>" + yeast.form + "</FORM>";
	            string += "<LABORATORY>" + yeast.labo + "</LABORATORY>";
	            string += "<PRODUCT_ID>" + yeast.product_id + "</PRODUCT_ID>";
	            string += "<ATTENUATION>" + yeast.attenuation + "</ATTENUATION>";
	            string += "</YEAST>";
	        });
	        string += "</YEASTS>";
	        string += "<MISCS>";
	        recipe.miscs.forEach(function (misc) {
	            string += "<MISC>";
	            string += "<NAME>" + misc.name + "</NAME>";
	            string += "<VERSION>1</VERSION>";
	            string += "<AMOUNT>" + misc.amount / 1000 + "</AMOUNT>";
	            string += "<TYPE>" + misc.type + "</TYPE>";
	            string += "<TIME>" + misc.time + "</TIME>";
	            string += "<USE>" + misc.use + "</USE>";
	            string += "</MISC>";
	        });
	        string += "</MISCS>";
	        string += "<WATERS/>";
	        string += "<MASH>";
	        string += "<NAME>" + recipe.mashProfile.name + "</NAME>";
	        string += "<VERSION>1</VERSION>";
	        string += "<GRAIN_TEMP>" + recipe.grainTemp + "</GRAIN_TEMP>";
	        string += "<TUN_TEMP>" + recipe.mashProfile.tunTemp + "</TUN_TEMP>";
	        string += "<SPARGE_TEMP>" + recipe.mashProfile.sparge + "</SPARGE_TEMP>";
	        string += "<PH>" + recipe.mashProfile.ph + "</PH>";
	        string += "<MASH_STEPS>";
	        recipe.mashProfile.steps.forEach(function (step) {
	            string += "<MASH_STEP>";
	            string += "<NAME>" + step.name + "</NAME>";
	            string += "<VERSION>1</VERSION>";
	            string += "<TYPE>" + step.type + "</TYPE>";
	            string += "<STEP_TIME>" + step.time + "</STEP_TIME>";
	            string += "<STEP_TEMP>" + step.temp + "</STEP_TEMP>";
	            string += "<INFUSE_AMOUNT>0</INFUSE_AMOUNT>";
	            string += "</MASH_STEP>";
	        });
	        string += "</MASH_STEPS>";
	        string += "</MASH>";
	        string += "<NOTES>" + recipe.notes + "</NOTES>";
	        string += "</RECIPE></RECIPES>";

	        xml = parser.parseFromString(string, "application/xml");
	        console.log(xml);
	        return string;

		}





	};
}());
