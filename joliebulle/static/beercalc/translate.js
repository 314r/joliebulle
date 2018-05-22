/*jslint nomen: true */
/*global main, _*/
var translate = (function () {
	"use strict";
    var _locale_fr;
    
	_locale_fr = {
        "Grain" : "Grain",
        "Extract" : "Extrait",
        "Dry Extract" : "Extrait Sec",
        "Sugar" : "Sucre",
        "TRUE" : "Après Ebullition",
        "FALSE" : "Brassage",
        "Plug" : "Cône",
        "Leaf" : "Feuille",
        "Pellet" : "Pellet",
        "Boil" : "Ebullition",
        "Dry Hop" : "Dry Hop",
        "First Wort" : "Premier Moût",
        "Mash" : "Empâtage",
        "Aroma" : "Hors Flamme",
        "Spice" : "Epice",
        "Flavor" : "Arôme",
        "Water Agent" : "Traitement Eau",
        "Herb" : "Herbe",
        "Fining" : "Clarifiant",
        "Other" : "Autre",
        "Primary" : "Primaire",
        "Secondary" : "Secondaire",
        "Bottling" : "Embouteillage",
        "Liquid" : "Liquide",
        "Dry" : "Poudre",
        "Slant" : "Gélose",
        "Culture" : "Culture"
    };

	return {

		translate_fr : function (recipe) {
			recipe.hops.forEach(function (hop) {
            // If formView is in french (not undefined), we translate hop.form to english/beerxml. 
            // If formView is undefined, we translate hop.form to french.
                if (typeof hop.formView !== 'undefined') {
                    hop.form = (_.invert(_locale_fr))[hop.formView];
                } else {
                    hop.formView = _locale_fr[hop.form];
                }
                if (typeof hop.useView !== 'undefined') {
                    hop.use = (_.invert(_locale_fr))[hop.useView];
                } else {
                    hop.useView = _locale_fr[hop.use];
                }
            });

            recipe.fermentables.forEach(function (fermentable) {
                if (typeof fermentable.typeView !== 'undefined') {
                    fermentable.type = (_.invert(_locale_fr))[fermentable.typeView];
                } else {
                    fermentable.typeView = _locale_fr[fermentable.type];
                }
                if (typeof fermentable.afterBoilView !== 'undefined') {
                    fermentable.afterBoil = (_.invert(_locale_fr))[fermentable.afterBoilView];
                } else {
                    fermentable.afterBoilView = _locale_fr[fermentable.afterBoil];
                }
            });

            recipe.miscs.forEach(function (misc) {
                if (typeof misc.useView !== 'undefined') {
                    misc.use = (_.invert(_locale_fr))[misc.useView];
                } else {
                    misc.useView = _locale_fr[misc.use];
                }
                if (typeof misc.typeView !== 'undefined') {
                    misc.type = (_.invert(_locale_fr))[misc.typeView];
                } else {
                    misc.typeView = _locale_fr[misc.type];
                }

            });

            recipe.yeasts.forEach(function (yeast) {
                if (typeof yeast.formView !== 'undefined') {
                    yeast.form = (_.invert(_locale_fr))[yeast.formView];
                } else {
                    yeast.formView = _locale_fr[yeast.form];
                }
            });

            return recipe;

		}

	};



}());