import behave

from app.account import InsufficientBalance


@behave.when('I withdraw $3000 from my account')
def withdraw_usd_3000(context):
    try:
        context.account.withdraw_cash(amount=3000)
    except InsufficientBalance as ex:
        context.exc = ex


@behave.then('It raises {exception_type} exception with message {exception_message}')
def check_for_exception_type_and_exception_message(context, exception_type, exception_message):
    assert isinstance(context.exc, eval(exception_type))
    assert str(context.exc) == exception_message
