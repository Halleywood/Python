"""
Add a make_withdrawal method to the User class

Add a display_user_balance method to the User class

Create 3 instances of the User class

Have the first user make 3 deposits and 1 withdrawal and then display their balance

Have the second user make 2 deposits and 2 withdrawals and then display their balance

Have the third user make 1 deposits and 3 withdrawals and then display their balance

BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances


"""
class User:
    def __init__(self, name):
        self.balance=0
        self.name= name
    def make_withdrawl(self, amount):
        self.balance-= amount  
    def make_deposits(self, amount):
        self.balance+=amount
    def display_user_balance(self):
        print(f"User:{self.name}, Balance:{self.balance}.")
    def transer_money(self, other_person, amount):
        self.balance-=amount
        other_person.balance+=amount

kelsey=User("Kelsey")
kelsey.make_deposits(1000).make_deposits(250).make_deposits(750).make_withdrawl(500).display_user_balance()



andrew=User("Andrew")
andrew.make_deposits(20).make_deposits(200).make_withdrawl(100).make_withdrawl(100).display_user_balance()

thomas=User("Thomas")
thomas.make_deposits(500).make_withdrawl(100).make_withdrawl(600).make_withdrawl(50).display_user_balance()

kelsey.transer_money(thomas,500)
kelsey.display_user_balance()
thomas.display_user_balance()
