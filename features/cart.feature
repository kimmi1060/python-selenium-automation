Feature: Add a product to cart

  Scenario: Add a product to the cart
    Given Open target main page
    When Search for "AirPods"
    And Add the product to cart
    And Click on Cart icon
    Then Verify product is in the cart
