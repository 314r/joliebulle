toolsApp.controller('JournalCtrl', ['$scope', '$http', '$filter', function ($scope, $http, $filter) {
    "use strict";

    $scope.entries = [];

    $scope.$watch($scope.newEntry, function () {
        $scope.newEntryRecipe = $scope.newEntry.recipe;
        $scope.newEntryDate = $filter('date')($scope.newEntry.date * 1000, "shortDate");
        $scope.newEntryEvent = $scope.newEntry.event;
    });


    $scope.$watch('dataJson', function () {
        $scope.entries = $scope.dataJson;
        $scope.entries = _.sortBy($scope.entries, 'date').reverse();
        return $scope.entries;
    });

    $scope.edit = function (entry) {
        entry.editing = !entry.editing;
        entry.date = $filter('date')(entry.date * 1000, "yyyy-MM-dd");
    };

    $scope.save = function (entry) {
        entry.editing = !entry.editing;
        entry.date = new Date(entry.date).getTime() / 1000 + (new Date().getHours() * 3600) + (new Date().getMinutes() * 60) + (new Date().getSeconds());;
        entry.date = entry.date.toString();
        $scope.entries = _.sortBy($scope.entries, 'date').reverse();
        main.dumpJournal(JSON.stringify($scope.entries, $scope.cleanJson));
        return entry;
    };

    $scope.saveNew = function (recipe, date, event) {
        var entry = {};
        entry.recipe = recipe;
        // On veut une date plus précise, histoire d'etre sur de respecter la chronologie des entrées
        entry.date = (new Date(date).getTime() / 1000) + (new Date().getHours() * 3600) + (new Date().getMinutes() * 60) + (new Date().getSeconds());
        entry.date = entry.date.toString();
        entry.event = event;
        $scope.entries.push(entry);
        // On trie avec Underscore
        $scope.entries = _.sortBy($scope.entries, 'date').reverse();
        // Il faut nettoyer le JSON produit des clés indésirables
        main.dumpJournal(JSON.stringify($scope.entries, $scope.cleanJson));
    };

    $scope.delete = function (entry) {
        /*attention delete est un mot réservé : à remplacer*/
        $scope.entries.splice($scope.entries.indexOf(entry), 1);
        main.dumpJournal(JSON.stringify($scope.entries, $scope.cleanJson));
    };

    $scope.newClicked = function (recipe, event) {
        $scope.newEntry.recipe = recipe;
        $scope.newEntry.event = event;
        var date = new Date();
        $scope.newEntry.date = date / 1000;

        $scope.newEntryRecipe = $scope.newEntry.recipe;
        $scope.newEntryEvent = $scope.newEntry.event;
        $scope.newEntryDate = $filter('date')($scope.newEntry.date * 1000, "yyyy-MM-dd");
    };

    $scope.cleanJson = function (key, value) {
        if (key === "$$hashKey" || key === "editing") {
            return undefined;
        } else {
            return value;
        }
    };
}]);
