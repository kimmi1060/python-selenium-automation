Feature: Color selection on Target product page
  Scenario: Verify product color selection
    Given I am on the Target product page "https://www.target.com/p/A-91511634"
    When I select each available product color
    Then the selected color should be visibly highlighted

    Scenario: Verify product color selection
    Given I am on the Target product page "https://www.target.com/p/A-54551690"
    When I select each available product color
    Then the selected color should be visibly highlighted