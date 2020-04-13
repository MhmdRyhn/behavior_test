import behave


@behave.when('I add $1200 to my account')
def add_usd_1200(context):
    context.account.add_cash(amount=1200)


@behave.then('It becomes $3200 in my account')
def check_for_increase_to_usd_1880(context):
    assert context.account.current_cash == 3200
