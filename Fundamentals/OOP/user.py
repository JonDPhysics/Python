class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    
    #def transfer_money(self, user, transfer):
    #    self.user = user
    #    self.account_balance -= transfer



henry = User("Henry Smith", "henry.smith@python.com")
theo = User("Theo Smith", "theo.smith@python.com")
jonathan = User("Jonathan Smith", "jonathan.smith722@gmail.com")

henry.make_deposit(500.50)
henry.make_deposit(222.22)
henry.make_deposit(300.00)
henry.make_withdrawal(22.50)
henry.display_user_balance()

theo.make_deposit(117.14)
theo.make_deposit(5.75)
theo.make_withdrawal(17.00)
theo.make_withdrawal(5.00)
theo.display_user_balance()

jonathan.make_deposit(333.33)
jonathan.make_withdrawal(333.33)
jonathan.make_withdrawal(333.33)
jonathan.make_withdrawal(333.33)
jonathan.display_user_balance()
