import behave

from app.account import Account, InsufficientBalance

transaction_mapper = {
    'add': 'add_cash',
    'withdraw': 'withdraw_cash'
}


@behave.given('I have an initial amount of ${initial:d} in my account')
def setup_initial_amount(context, initial):
    context.account = Account(initial_amount=initial)


@behave.when('I {transaction} ${amount:d} to/from my account')
def make_transaction(context, transaction, amount):
    getattr(context.account, transaction_mapper[transaction])(amount=amount)


@behave.then('It becomes ${total:d} in my account')
def check_total(context, total):
    assert context.account.current_cash == total


@behave.when('I withdraw ${withdraw_amount:d} from my account')
def make_invalid_transaction(context, withdraw_amount):
    try:
        context.account.withdraw_cash(amount=withdraw_amount)
    except InsufficientBalance as ex:
        context.exc = ex


@behave.then('It raises {exception} exception when withdrawing ${withdraw_amount:d} from ${initial:d}')
def check_exception(context, exception, withdraw_amount, initial):
    assert isinstance(context.exc, eval(exception))
    assert str(context.exc) == f'Not enough available balance to withdraw {withdraw_amount}'
