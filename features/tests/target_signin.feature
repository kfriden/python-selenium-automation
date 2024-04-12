# Created by Kait Kait at 4/4/2024
Feature: Signed out user can navigate to sign in page

  Scenario: Signed out user navigates to sign in page
    Given Open Target main page
    When Click sign in
    When Click sign in on side nav bar
    Then Verify sign in form opens