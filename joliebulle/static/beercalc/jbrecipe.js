/*jslint nomen: true */
var jbrecipe = (function () {
    "use strict";
    var recipe;
    
    return {
        newRecipe : function () {
            recipe = {};
            recipe.path = "";
            recipe.name = "Nouvelle Recette";
            recipe.brewer = "auteur";
            recipe.volume = "0";
            recipe.style = "generic";
            recipe.type = "All Grain";
            recipe.boilTime = "60";
            recipe.efficiency = "70";
            recipe.hops = [];
            recipe.grains = [];
            recipe.miscs = [];
            recipe.yeasts = [];
            recipe.mashProfile = {};
            
            
            
            
        
        }
    
    
    
    };
    
}());