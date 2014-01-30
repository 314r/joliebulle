toolsApp.controller('JournalCtrl', ['$scope','$http', '$filter', function ($scope,$http,$filter) {
    "use strict";

    $scope.entries=[];

    $scope.$watch($scope.newEntry, function () {
        $scope.newEntryRecipe = $scope.newEntry.recipe;
        $scope.newEntryDate = $filter('date')($scope.newEntry.date*1000, "yyyy-MM-dd");
        $scope.newEntryEvent = $scope.newEntry.event;
    });


    $scope.$watch('dataJson', function () {
        $scope.entries = $scope.dataJson;
        return $scope.entries;
});

    $scope.edit = function(entry) {
        entry.editing = !entry.editing;
        entry.date = $filter('date')(entry.date*1000, "yyyy-MM-dd");
    };

    $scope.save = function(entry) {
        entry.editing = !entry.editing;
        entry.date = new Date(entry.date).getTime() / 1000;
        return entry;
    };

    $scope.saveNew = function(recipe, date, event) {
        var entry = {};
        entry.recipe = recipe;
        entry.date = new Date(date).getTime() / 1000;
        entry.event = event;
        $scope.entries.push(entry);
        $scope.entries = _.sortBy( $scope.entries, 'date' ).reverse();
        main.dumpJournal(JSON.stringify($scope.entries));

    };

    $scope.delete = function(entry) {
        $scope.entries.splice($scope.entries.indexOf(entry),1);
    };

    $scope.newClicked = function(recipe, event) {
        $scope.newEntry.recipe = recipe;
        $scope.newEntry.event = event;
        var date = new Date();
        $scope.newEntry.date = date / 1000;

        $scope.newEntryRecipe = $scope.newEntry.recipe;
        $scope.newEntryEvent = $scope.newEntry.event;
        $scope.newEntryDate = $filter('date')($scope.newEntry.date*1000, "yyyy-MM-dd");
    };



}]);
