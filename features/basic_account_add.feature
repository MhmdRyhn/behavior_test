# ---- Simple hard-coded feature (add to account) ----
Feature: As a client of this software,
  I want to check if after adding money to my
  account, whether it increases correctly or not

  Scenario: Check money adding operation
    Given I have an initial amount of $2000 in my account
    When I add $1200 to my account
    Then It becomes $3200 in my account