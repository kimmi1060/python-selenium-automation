Feature: Verify Sign In functionality

  Scenario: Verify logged-out user can access Sign In
    Given Open target main page
    When Click Sign In from header
    And From right-side navigation menu, click Sign In
    Then Verify Sign In form opened
