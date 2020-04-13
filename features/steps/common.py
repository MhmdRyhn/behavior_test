import behave

from app.account import Account


@behave.given('I have an initial amount of $2000 in my account')
def setup_initial_amount_of_usd_2000(context):
    context.account = Account(initial_amount=2000)
