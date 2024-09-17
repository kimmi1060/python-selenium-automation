Feature: Add product to cart

  Scenario: Add a product to the cart
    Given I am on the Target homepage
    When I add "laptop" to the cart
    Then the cart should contain the product
