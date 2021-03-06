# ---- Tableized test ----
Feature: As a client of this software,
  I want to check if the transactions
  work properly or not using tablized test

  Scenario Outline: Check valid transactions
    Given I have an initial amount of $<initial> in my account
    When I <transaction> $<amount> to/from my account
    Then It becomes $<total> in my account

    Examples: Valid transactions
      | initial | transaction | amount | total |
      | 100     | add         | 10     | 110   |
      | 100     | withdraw    | 10     | 90    |

  Scenario Outline: Check invalid transactions
    Given I have an initial amount of $<initial> in my account
    When I withdraw $<withdraw_amount> from my account
    Then It raises <exception> exception when withdrawing $<withdraw_amount> from $<initial>

    Examples: Invalid transactions
      | initial | withdraw_amount | exception           |
      | 100     | 110             | InsufficientBalance |
      | 100     | 101             | InsufficientBalance |
