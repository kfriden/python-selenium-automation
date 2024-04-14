# Created by Kait Kait at 4/4/2024
Feature: Target cart tests

  Scenario: User checks cart is empty
    Given Open Target main page
    When Click cart icon
    Then Verify cart is empty message shows


  Scenario: User adds item to cart, verify item is in cart
    Given Open Target main page
    When Search for 'Mario'
    Then Add any 'Mario' item to cart
    Then Click Add to Cart on side menu
    Then Click decline coverage button
    When Click cart icon
    Then Verify 'Mario' has been added to cart