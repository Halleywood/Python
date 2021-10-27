class BankAccount:
    accounts= []
    name="user"

    def __init__(self, balance, interest_rate):
        self.balance=balance
        self.interest_rate=interest_rate
        BankAccount.accounts.append()

    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdrawl(self, amount):
        if(self.balance-amount<0):
            print("insufficient funds in your account. a $5 penalty will be charged to your account")
            self.balance-5
        else:
            self.balance-=amount
            return self

    def display_account_info(self):
        print(self.balance)
        return self
    def yield_interest(self):
        if(self.balance>0):
            self.balance+=(self.balance* self.interest_rate)
        return self

@classmethod
def print_all_accounts(cls):
    for balance in cls.accounts:
        balance.display_account_info()

first_account=BankAccount(0, 0.05)
second_account=BankAccount(200, 0.05)
BankAccount.print_all_accounts()

first_account.deposit(100).deposit(200).deposit(300).withdrawl(200).yield_interest().display_account_info()
second_account.deposit(200).deposit(200).withdrawl(50).withdrawl(100).withdrawl(50).withdrawl(100).yield_interest().display_account_info()
