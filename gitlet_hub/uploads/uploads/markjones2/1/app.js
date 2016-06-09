var noteApp = angular.module('noteApp', [
  'ngRoute',
  'noteControllers',
  'noteService'
]);

noteApp.config(['$routeProvider', function($routeProvider) {
  $routeProvider.
  when('/notes', {
    templateUrl: 'partials/list.html',
    controller: 'ListController'
  }).
  when('/details/:noteId', {
    templateUrl: 'partials/details.html',
    controller: 'DetailsController'
  }).
  when('/edit/:noteId', {
    templateUrl: 'partials/edit.html',
    controller: 'EditController'
  }).
  when('/add', {
    templateUrl: 'partials/edit.html',
    controller: 'EditController'
  }).
  otherwise({
    redirectTo: '/notes'
  });
}]);
