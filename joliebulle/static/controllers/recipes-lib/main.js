var recipesApp = angular.module('recipes-lib', []);

// recipesApp.filter('searchFor', function(){


// 	return function(arr, searchText){
// 		if(!searchText){
// 			return arr;
// 		}

// 		var result = [];

// 		searchText = searchText.toLowerCase();

// 		angular.forEach(arr, function(recipe){
// 			if(recipe.name.toLowerCase().indexOf(searchText) !== -1 | recipe.author.toLowerCase().indexOf(searchText) !== -1){
// 				result.push(recipe);
// 			}
// 		});

// 		return result;
// 	};

// });

recipesApp.directive('bsPopover', function() {
    return function(scope, element, attrs) {
        element.find("a[rel=popover]").popover({ placement: 'bottom', html: 'true', trigger:'hover'});
    };
});
