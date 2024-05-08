# Created by Kait Kait at 4/4/2024
Feature: Target Sign in Page

  Scenario: Signed out user navigates to sign in page
    Given Open Target main page
    When Click sign in
    When Click sign in on side nav bar
    Then Verify sign in form opens


  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target main page
    When Click sign in
    When Click sign in on side nav bar
    When Store original window
    And Click on Target terms and conditions link
    Then Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close current page
    Then Return to original window

  Scenario: Inputting incorrect username and password shows incorrect account message
    Given Open Target main page
    When Click sign in
    When Click sign in on side nav bar
    Then Input incorrect username unicorn45@gmail.com
    Then Input incorrect password 12345
    When Click login
    Then Verify We cannot find your account message shows
