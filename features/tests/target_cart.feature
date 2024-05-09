# Created by Kait Kait at 4/4/2024
Feature: Target cart tests

  Scenario: User checks cart is empty
    Given Open Target main page
    When Click cart icon
    Then Verify cart is empty message shows

  @smoke
  Scenario: User adds item to cart, verify item is in cart
    Given Open Target main page
    When Search for 'tea'
    Then Add any 'tea' item to cart
    Then Click Add to Cart on side menu
    Then Open Target Cart Page
    Then Verify 'tea' has been added to cart