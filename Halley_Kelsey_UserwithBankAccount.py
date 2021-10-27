class User:
    def __init__(self, name):
        self.name= name
        self.account={
            "checking":BankAccount(10000, 0.05),
            "savings":BankAccount(200,0.09)
        }
        #BankAccount(self, balance=0, interest_rate=0.05)
#    def make_withdrawl(self, amount):
#        self.balance-=amount
#    def make_deposits(self):
#        self.account.deposit()
    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.account.display_account_info()}.")
        return self
#    def transer_money(self, other_person, amount):
#        self.balance-=amount
#        other_person.balance+=amount
#        return self

class BankAccount:
    accounts= []
    name="user"

    def __init__(self, balance, interest_rate):
        self.balance=balance
        self.interest_rate=interest_rate
        BankAccount.accounts.append(self)

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

drew=User("Drew")
drew.account["savings"].deposit(100)
drew.account["savings"].display_account_info()