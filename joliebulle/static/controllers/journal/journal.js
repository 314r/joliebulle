toolsApp.controller('JournalCtrl', ['$scope', '$http', '$filter', function ($scope, $http, $filter) {
    "use strict";

    $scope.entries = [];

    $scope.$watch($scope.newEntry, function () {
        $scope.newEntryRecipe = $scope.newEntry.recipe;
        $scope.newEntryDate = new Date(parseInt($scope.newEntry.date)*1000);
        $scope.newEntryEvent = $scope.newEntry.event;
    });

    $scope.$watch('dataJson', function () {
        $scope.entries = $scope.dataJson;
        $scope.entries = _.sortBy($scope.entries, 'date').reverse();
        _.each($scope.entries, $scope.convertDate);
        return $scope.entries;
    });

    $scope.edit = function (entry) {
        entry.editing = !entry.editing;
        // entry.date = $filter('date')(entry.date * 1000, "yyyy-MM-dd");
    };

    $scope.save = function (entry) {
        entry.editing = !entry.editing;
        // entry.date = $scope.formatDate(entry.date);
        _.each($scope.entries, $scope.convertToUnix);
        $scope.entries = _.sortBy($scope.entries, 'date').reverse();
        main.dumpJournal(JSON.stringify($scope.entries, $scope.cleanJson));
        _.each($scope.entries, $scope.convertDate);
        return entry;
    };

    $scope.saveNew = function (recipe, date, event) {
        var entry = {};
        entry.recipe = recipe;
        // entry.date = $scope.formatDate(date);
        entry.date= date;
        entry.event = event;
        $scope.entries.push(entry);
        _.each($scope.entries, $scope.convertToUnix);
        // On trie avec Underscore
        $scope.entries = _.sortBy($scope.entries, 'date').reverse();
        // Il faut nettoyer le JSON produit des clés indésirables
        main.dumpJournal(JSON.stringify($scope.entries, $scope.cleanJson));
         _.each($scope.entries, $scope.convertDate);
    };

    $scope.delete = function (entry) {
        // attention delete est un mot réservé : à remplacer
        $scope.entries.splice($scope.entries.indexOf(entry), 1);
        _.each($scope.entries, $scope.convertToUnix);
        main.dumpJournal(JSON.stringify($scope.entries, $scope.cleanJson));
         _.each($scope.entries, $scope.convertDate);
    };

    $scope.newClicked = function (recipe, event) {
        $scope.newEntry.recipe = recipe;
        $scope.newEntry.event = event;
        var date = new Date();
        $scope.newEntry.date = date;

        $scope.newEntryRecipe = $scope.newEntry.recipe;
        $scope.newEntryEvent = $scope.newEntry.event;
        $scope.newEntryDate = $scope.newEntry.date ;
    };

    $scope.cleanJson = function (key, value) {
        if (key === "$$hashKey" || key === "editing") {
            return undefined;
        } else {
            return value;
        }
    };

    // Deprecated
    // $scope.formatDate = function (date) {
    //     // On transforme la date pour contourner un bug sous Windows qui fait que le format yyyy-MM-dd ne passe pas.
    //     date = $filter('date')(date, 'longDate');
    //     // On veut une date plus précise, histoire d'etre sur de respecter la chronologie des entrées.
    //     date = (new Date(date).getTime() / 1000) + (new Date().getHours() * 3600) + (new Date().getMinutes() * 60) + (new Date().getSeconds());
    //     date = date.toString();
    //     return date;
    // };

    $scope.convertDate = function (entry, step, array) {
        entry.date = new Date(parseInt(entry.date)*1000)
    };

    $scope.convertToUnix = function (entry, step, array) {
        entry.date = new Date(entry.date).getTime() / 1000;
        entry.date.toString();
    };

    $scope.importRecipes = function () {
        return JSON.parse(main.dataRecipes().replace(/\bNaN\b/g, "null"));
    };

    $(document).ready(function(){
        $scope.recipes = $scope.importRecipes();
        var recipes_name = [];
        $scope.recipes.forEach(function(r){
            recipes_name.push(r.name);
        });
        $( "#new-entry-recipe" ).autocomplete({
            source: recipes_name,
            select: function( event, ui ) {
                if (ui.item.label != null) {
                    $scope.newEntryRecipe= ui.item.label;
                }
                return true;
            },
            change: function( event, ui ) {
                if (ui.item.label != null) {
                    $scope.newEntryRecipe= ui.item.label;
                }
                return true;
            },

        });
    });

    $(document).on("click", ".edit-entry-recipe", function() {
        var recipes_name = [];
        $scope.recipes.forEach(function(r){
            recipes_name.push(r.name);
        });
        $( ".edit-entry-recipe" ).autocomplete({
            source: recipes_name,
            select: function( event, ui ) {
                if (ui.item.label != null) {
                    $scope.entries.forEach(function(e){
                        if(e.editing){
                            e.recipe= ui.item.label;
                        }
                    });
                }
                return true;
            },
            change: function( event, ui ) {
                if (ui.item.label != null) {
                    $scope.entries.forEach(function(e){
                        if(e.editing){
                            e.recipe= ui.item.label;
                        }
                    });
                }
                return true;
            },

        });
    })

}]);
