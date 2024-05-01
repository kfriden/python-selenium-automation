# Created by Kait Kait at 4/28/2024
Feature: Tests for the Target App Page

  Scenario: User is Able to Open Privacy Policy Page
    Given Open Target App Page
    And Store original window
    Then Click Privacy Policy link
    Then Switch to new window
    Then Verify Privacy Policy page is opened
    And Close current page
    Then Return to original window