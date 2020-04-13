class InsufficientBalance(Exception):
    pass


class Account:
    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def withdraw_cash(self, amount):
        if self.balance < amount:
            raise InsufficientBalance('Not enough available balance to withdraw {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount

    @property
    def current_cash(self):
        return self.balance
