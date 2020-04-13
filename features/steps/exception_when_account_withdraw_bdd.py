import behave

from app.account import InsufficientBalance


@behave.when('I withdraw $3000 from my account')
def withdraw_usd_3000(context):
    try:
        context.account.withdraw_cash(amount=3000)
    except InsufficientBalance as ex:
        context.exc = ex


@behave.then('It raises InsufficientBalance exception with message Not enough available balance to withdraw 3000')
def check_for_exception_type_and_exception_message(context):
    assert isinstance(context.exc, InsufficientBalance)
    assert str(context.exc) == 'Not enough available balance to withdraw 3000'


"""
# This can also be used instead of the above one. Both produces same result. 
# But, don't use this one and the above one at a time, it'll raise error. 
@behave.then('It raises {exception_type} exception with message {exception_message}')
def check_for_exception_type_and_exception_message(context, exception_type, exception_message):
    assert isinstance(context.exc, eval(exception_type))
    assert str(context.exc) == exception_message
"""
