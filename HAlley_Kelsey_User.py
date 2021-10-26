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
kelsey.make_deposits(1000)
kelsey.make_deposits(250)
kelsey.make_deposits(750)
kelsey.make_withdrawl(500)
kelsey.display_user_balance()

andrew=User("Andrew")
andrew.make_deposits(20)
andrew.make_deposits(200)
andrew.make_withdrawl(100)
andrew.make_withdrawl(100)
andrew.display_user_balance()

thomas=User("Thomas")
thomas.make_deposits(500)
thomas.make_withdrawl(100)
thomas.make_withdrawl(600)
thomas.make_withdrawl(50)
thomas.display_user_balance()

kelsey.transer_money(thomas,500)
kelsey.display_user_balance()
thomas.display_user_balance()
