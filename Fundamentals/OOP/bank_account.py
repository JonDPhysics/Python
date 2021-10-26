class BankAccount:
    
    account_info = []

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.account_info.append(self)
    
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
        print(f"Balance: ${self.balance} Interest rate: {self.int_rate}%")

    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
        else:
            print("No interest")
        return self.int_rate
    @classmethod
    def log_account_info(cls):
        sum = 0
        for val in cls.account_info:
            sum += val.balance
        return sum

account1 = BankAccount(0.05, 100)
account2 = BankAccount(0.005, 1000)

account1.deposit(500).deposit(5).deposit(50).withdraw(700)
account2.deposit(600).deposit(60).withdraw(6).withdraw(54).withdraw(100).withdraw(200)

account1.display_account_info()
account2.display_account_info()
print(f"Total: {BankAccount.log_account_info()}")
