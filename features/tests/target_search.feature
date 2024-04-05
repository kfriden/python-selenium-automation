# Created by Kait Kait at 4/4/2024
Feature: Search tests

  Scenario: User can search for a product
    Given Open Target main page practice
    When Search for 'coffee'
    Then Verify search results are shown


