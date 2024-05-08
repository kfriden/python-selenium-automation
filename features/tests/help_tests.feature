# Created by kfrid at 5/5/2024
Feature: Tests for Help pages

  Scenario: User can select help topic Promotions & Coupons
    Given Open Help page for Returns
    Then Verify Returns page opened
    When Select Help topic Promotions & Coupons
    Then Verify current promotions page opened

  Scenario: User can select help topic Target Circle
    Given Open Help page for Returns
    Then Verify Returns page opened
    When Select Help topic Target Circle™
    Then Verify About Target Circle page opened

  Scenario: User can select help topic Target Account
    Given Open Help page for Returns
    Then Verify Returns page opened
    When Select Help topic Target Account
    Then Verify Create account page opened
