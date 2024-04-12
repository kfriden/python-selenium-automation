# Created by Kait Kait at 4/4/2024
Feature: Target cart tests

  Scenario: User checks cart is empty
    Given Open Target main page
    When Click cart icon
    Then Verify cart is empty message shows