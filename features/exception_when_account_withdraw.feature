# ---- Simple hard-coded feature (withdraw from account) ----
Feature: As a client of this software,
  I want to check if withdrawing more money
  than available, whether it prevents it or not

  Scenario: Check money withdrawing operation
    Given I have an initial amount of $2000 in my account
    When I withdraw $3000 from my account
    Then It raises InsufficientBalance exception with message Not enough available balance to withdraw 3000



