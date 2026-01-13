class Account:
    def __init__(self, owner, account_number, account_balance,
                 max_daily_turnove=1500):
        self.owner = owner
        self.account_number = account_number
        self.account_balance = account_balance
        self.max_daily_turnove = max_daily_turnove

    def money_transfer(self, destination, amount):
        pass

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def show(self):
        pass
