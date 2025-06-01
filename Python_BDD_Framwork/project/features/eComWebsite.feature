@ButItems
Feature: Purchase Required Items from Online
  @Purchase
  Scenario Outline: Buy multiple Items
    Given Login into saucedemo website <testDataNum>
    When Add required items in cart
    And Open cart and check all the items
    And Add delivery address
    Then Make pament and perform checkout

  Examples:
  | testDataNum |
  | Test 1  |
  