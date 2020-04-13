import behave

from app.account import Account

transaction_mapper = {
    'add': 'add_cash',
    'withdraw': 'withdraw_cash'
}


@behave.given('I have an initial amount of {initial:d} in my account')
def setup_initial_amount(context, initial):
    context.account = Account(initial_amount=initial)


@behave.when('I {transaction} {amount:d} to/from my account')
def make_transaction(context, transaction, amount):
    getattr(context.account, transaction_mapper[transaction])(amount=amount)


@behave.then('It becomes {total:d} in my account')
def check_total(context, total):
    assert context.account.current_cash == total
