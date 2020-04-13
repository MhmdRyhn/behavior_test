# ---- Simple hard-coded feature (withdraw from account) ----
Feature: As a client of this software,
  I want to check if after withdrawing money
  from account, whether it remains stable or not

  Scenario: Check money withdrawing operation
    Given I have an initial amount of $2000 in my account
    When I withdraw $120 from my account
    Then It remains $1880 in my account



