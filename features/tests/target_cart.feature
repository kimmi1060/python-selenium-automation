# Created by kkdad at 9/13/2024
Feature: Verify Cart is Empty Message

  Scenario: User sees "Your cart is empty" message on target.com
    Given I open the Target homepage
    When I click on the Cart icon
    Then I should see "Your cart is empty" message
  # Enter feature description here

