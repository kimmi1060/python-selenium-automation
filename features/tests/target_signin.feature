Feature: Verify Sign In Navigation

  Scenario: Logged out user navigates to Sign In page on target.com
    Given I open the Target homepage
    When I click on the Sign In button
    And I click on the Sign In link in the right side navigation menu
    Then I should see the Sign In form
