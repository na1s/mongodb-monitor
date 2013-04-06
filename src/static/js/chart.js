'use strict';

/* Controllers */

function ChartListCntrl($scope, Chart) {
    $scope.charts = Chart.query();
    $scope.orderProp = 'age';
}


