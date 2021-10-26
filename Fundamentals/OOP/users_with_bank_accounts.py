class BankAccount:
    
    # account_info = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # BankAccount.account_info.append(self)
    
    def current_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.amount = amount
        if self.balance >= self.amount:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

    def display_account_info(self):
        print(f"Balance: ${self.balance} and Interest rate: {self.int_rate}%")

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
        else:
            print("No interest")
        return self.int_rate
    # @classmethod
    # def log_account_info(cls):
    #     sum = 0
    #     for val in cls.account_info:
    #         sum += val.balance
    #     return sum

class User:
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.account_balance = account 

    def make_deposit(self,amount):
        self.account_balance.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account_balance.display_account_info()
        return f"User: {self.name}, Balance: ${self.account_balance}"
    
    #def transfer_money(self, user, transfer):
    #    self.user = user
    #    self.account_balance -= transfer

account1 = BankAccount(0.05, 100)
account2 = BankAccount(0.005, 1000)

user1 = User("Jonathan Smith","jonathan.smith722@gmail.com", account1)
user2 = User("Meghan Smith", "meghan.smith227@gmail.com", account2)

user1.make_deposit(500).make_deposit(5).make_deposit(50).make_withdrawal(700)
user2.make_deposit(600).make_deposit(60).make_withdrawal(6).make_withdrawal(54).make_withdrawal(100).make_withdrawal(200)

user1.display_user_balance()
user2.display_user_balance()
# print(f"Total: {BankAccount.log_account_info()}")

