Feature: Target Help UI Verification

  Scenario: Verify UI elements on Target Help page
    Given I am on the Target Help page
    Then I should see the following UI elements:
      | element      |
      | search_box   |
      | help_topics  |
      | contact_link |
#