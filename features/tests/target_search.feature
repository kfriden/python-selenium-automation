# Created by Kait Kait at 4/4/2024
Feature: Search tests

  Scenario: User can search for coffee
    Given Open Target main page
    When Search for 'coffee'
    Then Verify search results are shown for coffee


  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for '<product>'
    Then Verify search results are shown for <expected_item>
    Examples:
    |product |expected_item    |
    |mug     |mug              |
    |tea     |tea              |