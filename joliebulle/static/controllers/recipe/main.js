var recipeApp = angular.module('recipe', []);

recipeApp.directive('linechart', function() {

    return {

        // required to make it work as an element
        restrict: 'E',
        template: '<div class="col-md-6" id="profile-graph" style="height:200px;"></div>',
        replace: true,
        // observe and manipulate the DOM
        link: function($scope, element, attrs) {

            var data = $scope[attrs.data],
                xkey = $scope[attrs.xkey],
                ykeys= $scope[attrs.ykeys],
                labels= $scope[attrs.labels];

            Morris.Line({
                    element: element,
                    data: data,
                    xkey: xkey,
                    ykeys: ykeys,
                    labels: ['Température'],
                    xLabelMargin: 10,
                    axes:false,
                    parseTime:false,
                    postUnits: '°C',
                    ymin:'45'
                });

        }

    };

});