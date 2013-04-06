'use strict';

/* Services */

angular.module('phonecatServices', ['ngResource']).
    factory('Phone', function($resource){
        return $resource('charts/', {}, {
            query: {method:'GET', params:{}, isArray:true}
        });
    });