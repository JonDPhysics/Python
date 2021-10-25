class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    
    #def transfer_money(self, user, transfer):
    #    self.user = user
    #    self.account_balance -= transfer



henry = User("Henry Smith", "henry.smith@python.com")
theo = User("Theo Smith", "theo.smith@python.com")
jonathan = User("Jonathan Smith", "jonathan.smith722@gmail.com")

henry.make_deposit(500.50).make_deposit(222.22).make_deposit(300.00).make_withdrawal(22.50).display_user_balance()

theo.make_deposit(117.14).make_deposit(5.75).make_withdrawal(17.00).make_withdrawal(5.00).display_user_balance()

jonathan.make_deposit(333.33).make_withdrawal(333.33).make_withdrawal(333.33).make_withdrawal(333.33).display_user_balance()
