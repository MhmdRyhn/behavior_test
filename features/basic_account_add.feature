# ---- Simple hard-coded feature (add to account) ----
Feature: As a client of this software,
  I want to check if after adding money to my
  account, whether it increases correctly or not

  Scenario: Check money adding operation
    Given I have an initial amount of $2000 in my account
    When I add $1200 to my account
    Then It becomes $3200 in my account

  # More than one scenario can be added under a single feature.
  # You can use the withdrawal scenario too with the add one.
  # For example: if you write the withdrawal scenario here like bellow
  # and remove the `basic_account_withdraw.feature` file, it will not
  # affect the tests at all and will produce same result as it is now
  """
  Scenario: Check money withdrawing operation
    Given I have an initial amount of $2000 in my account
    When I withdraw $120 from my account
    Then It remains $1880 in my account
  """