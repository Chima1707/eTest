describe("ListController Test", function () {

    var mockScope, controller

    beforeEach(angular.mock.module("inventory"));


    beforeEach(angular.mock.inject(function ($controller, $rootScope) {
        mockScope = $rootScope.$new();

        controller =  $controller("ListController", {
            $scope: mockScope
        });

    }));

    it("Tests the inventories List size", function () {
        expect(mockScope.inventories.length).toEqual(3);
    })
  
    it("Tests the first inventory item  to have id 0", function () {
        expect(mockScope.inventories[0].id).toEqual(0);
    })

  it("Tests the third inventory item to be 5 in stock", function () {
        expect(mockScope.inventories[2].quantity).toEqual(5);
    })
  
  

});
