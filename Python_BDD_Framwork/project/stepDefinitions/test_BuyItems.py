from pytest_bdd import scenario, given, when, then
from pytest_bdd.parsers import cfparse

from Python_BDD_Framwork.project.funcSupport.PerformAddToCart import PerformAddToCart
from Python_BDD_Framwork.project.funcSupport.loginPage import PerformLogin



@scenario('../features/eComWebsite.feature','Buy multiple Items')
def test_eComWebsite():
    pass


@given(cfparse('Login into saucedemo website {testDataNum}'))
def given_LoginToWebsite(setupDriver, testDataNum):

    login = PerformLogin(setupDriver)
    login.loginToSauceDemo()
    print("Swag Labs Home page is available")

@when('Add required items in cart')
def when_AddItemsToCart(setupDriver):

    addToCart = PerformAddToCart(setupDriver)
    addToCart.searchItem()
    addToCart.perfromAddToCart()
    addToCart.backToHome()
    print('Adding items to cart')

@when('Open cart and check all the items')
def when_OpenCartAndCheckItems(setupDriver):
    print('Opening cart and checking items')

@when('Add delivery address')
def when_AddDeliveryAddress(setupDriver):
    print('Adding delivery address')

@then('Make pament and perform checkout')
def then_MakePaymentAndCheckout(setupDriver):
    print('Making payment and checking out')