Feature: Target Product Search

  Scenario: Search for a product on Target
    Given I am on the Target homepage
    When I search for "laptop"
    Then I should see the results for "laptop"
