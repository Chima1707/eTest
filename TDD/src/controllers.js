
var inventoryServices = angular.module('inventory', ['ngRoute']);
// Set up mappings between URLs, templates, and controllers
function inventoryRouteConfig($routeProvider) {
$routeProvider.
when('/', {
controller: ListController,
templateUrl: 'templates/list.html'
}).

when('/view/:id', {
controller: DetailController,
templateUrl: 'templates/detail.html'
}).
otherwise({
redirectTo: '/'
});
}

inventoryServices.config(inventoryRouteConfig);
// Some fake inventories
 var inventories = [{
id: 0, title: 'Chair', description: 'office chairs',
date: '13-06-2014', quantity: 8}, {
id: 1, title: 'Table', description: 'office tables',
date: '11-06-2014', quantity: 2
}, {
id: 2, title: 'Stationary', description: 'office stationaries',
date: '12-06-2014', quantity: 5
}, ];



function ListController($scope) {
$scope.inventories = inventories;
}


function DetailController($scope, $routeParams) {
$scope.inventory = inventories[$routeParams.id];
}

