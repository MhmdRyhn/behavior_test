import behave


@behave.when('I withdraw $120 from my account')
def withdraw_usd_120(context):
    context.account.withdraw_cash(amount=120)


@behave.then('It remains $1880 in my account')
def check_for_remaining_usd_1880(context):
    assert context.account.current_cash == 1880
