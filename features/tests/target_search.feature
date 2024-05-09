# Created by Kait Kait at 4/4/2024
Feature: Search tests

  @smoke
  Scenario: User can search for coffee
    Given Open Target main page
    When Search for 'coffee'
    Then Verify search results are shown for coffee
    Then Verify that URL has coffee


  Scenario Outline: User can search for a product
    Given Open Target main page
    When Search for '<product>'
    Then Verify search results are shown for <expected_item>
    Examples:
    |product |expected_item    |
    |mug     |mug              |
    |tea     |tea              |


  Scenario: User can view favorites tooltip for search results
    Given Open Target main page
    When Search for 'tea'
    And Hover over favorites icon
    Then Verify favorites tooltip is shown