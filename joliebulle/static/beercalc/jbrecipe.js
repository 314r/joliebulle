/*jslint nomen: true */
/*global main */
var jbrecipe = (function () {
    "use strict";
    var recipe;
    
    return {
        newRecipe : function () {
            recipe = {};
            recipe.path = main.createPath();
            recipe.name = "Nouvelle Recette";
            recipe.brewer = "auteur";
            recipe.volume = 10;
            recipe.style = "generic";
            recipe.type = "All Grain";
            recipe.boilTime = 60;
            recipe.efficiency = 70;
            recipe.hops = [];
            recipe.fermentables = [];
            recipe.miscs = [];
            recipe.yeasts = [];
            recipe.mashProfile = {"name": "Infusion simple, corps moyen", "sparge": "78.0", "ph": "5.4", "tunTemp": "20", "steps": [{"name": "Emp\u00e2tage", "type_view": "Infusion", "type": "Infusion", "temp": "67.0", "time": "60"}, {"name": "Mash Out", "type_view": "Temp\u00e9rature", "type": "Temperature", "temp": "75.0", "time": "10"}]};
            recipe.notes = "";
            
            return recipe;
        }
    
    
    
    };
    
}());