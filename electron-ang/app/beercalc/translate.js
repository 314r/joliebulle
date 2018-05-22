/*jslint nomen: true */
/*global main, _*/
var translate = (function () {
	"use strict";
    var _locale_fr, _locale_en;

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

  _locale_en = {
				"Grain" : "Grain",
				"Extract" : "Extract",
				"Dry Extract" : "Dry Extract",
				"Sugar" : "Sugar",
				"TRUE" : "After Boil",
				"FALSE" : "Mash",
				"Plug" : "Plug",
				"Leaf" : "Leaf",
				"Pellet" : "Pellet",
				"Boil" : "Boil",
				"Dry Hop" : "Dry Hop",
				"First Wort" : "First Wort",
				"Mash" : "Mash",
				"Aroma" : "Flame Out",
				"Spice" : "Spice",
				"Flavor" : "Flavor",
				"Water Agent" : "Water Agent",
				"Herb" : "Herb",
				"Fining" : "Fining",
				"Other" : "Other",
				"Primary" : "Primary",
				"Secondary" : "Secondary",
				"Bottling" : "Bottling",
				"Liquid" : "Liquid",
				"Dry" : "Dry",
				"Slant" : "Slant",
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

		},

		translate_en: function (recipe) {

			recipe.hops.forEach(function (hop) {

                if (typeof hop.formView !== 'undefined') {
                    hop.form = (_.invert(_locale_en))[hop.formView];
                } else {
                    hop.formView = _locale_en[hop.form];
                }
                if (typeof hop.useView !== 'undefined') {
                    hop.use = (_.invert(_locale_en))[hop.useView];
                } else {
                    hop.useView = _locale_en[hop.use];
                }
        });


	    recipe.fermentables.forEach(function (fermentable) {
				if (typeof fermentable.typeView !== 'undefined') {
						fermentable.type = (_.invert(_locale_en))[fermentable.typeView];
				} else {
						fermentable.typeView = _locale_en[fermentable.type];
				}

	        if (typeof fermentable.afterBoilView !== 'undefined') {
	            fermentable.add_after_boil = (_.invert(_locale_en))[fermentable.afterBoilView];
	        } else {
	            fermentable.afterBoilView = _locale_en[fermentable.add_after_boil];
	        }
	    });

			recipe.miscs.forEach(function (misc) {
					if (typeof misc.useView !== 'undefined') {
							misc.use = (_.invert(_locale_en))[misc.useView];
					} else {
							misc.useView = _locale_en[misc.use];
					}
					if (typeof misc.typeView !== 'undefined') {
							misc.type = (_.invert(_locale_en))[misc.typeView];
					} else {
							misc.typeView = _locale_en[misc.type];
					}

			});

			recipe.yeasts.forEach(function (yeast) {
					if (typeof yeast.formView !== 'undefined') {
							yeast.form = (_.invert(_locale_en))[yeast.formView];
					} else {
							yeast.formView = _locale_en[yeast.form];
					}
			});


    return recipe;

		}



	};



}());
