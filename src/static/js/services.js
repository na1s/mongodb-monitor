'use strict';

/* Services */

angular.module('chartServices', ['ngResource']).
    factory('Chart', function($resource){
        return $resource('charts/', {}, {
            query: {method:'GET', params:{}, isArray:true}
        });
    });