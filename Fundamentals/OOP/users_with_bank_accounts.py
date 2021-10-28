class BankAccount:
    
    # account_info = []

    def __init__(self, checking_balance, savings_balance, checking_int_rate = 0.005, savings_int_rate = 0.05): 
        self.checking_int_rate = checking_int_rate
        self.savings_int_rate = savings_int_rate
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
        # BankAccount.account_info.append(self)


    def deposit(self, amount, type):
        self.type = type
        if self.type.lower() == "checking":
            self.checking_balance += amount
            return self
        if self.type.lower() == "savings":
            self.savings_balance += amount
            return self

    def withdraw(self, amount, type):
        self.amount = amount
        self.type = type
        if self.type.lower() == "checking":
            if self.checking_balance >= self.amount:
                self.checking_balance -= amount
                return self
            else:
                print("Insufficient funds: Charging a $5 fee")
                self.checking_balance -= 5
                return self

        if self.type.lower() == "savings":
            if self.savings_balance >= self.amount:
                self.savings_balance -= amount
                return self
            else:
                print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
                print("Insufficient funds: Charging a $5 fee")
                print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")
                self.savings_balance -= 5
                return self

    def display_account_info(self):
        print(f"Your Checking Account balance is ${self.checking_balance} with an interest rate of {self.checking_int_rate}%")
        print(f"Your Savings Account balance is ${self.savings_balance} with an interest rate of {self.savings_int_rate}%")
        self.checking_balance += self.savings_balance
        print(f"Your total balance is ${self.checking_balance}")
        print("-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-")

    def checking_yield_interest(self):
        if self.checking_balance > 0:
            self.checking_balance *= self.checking_int_rate
        else:
            print("No interest earned")
        return self

    def savings_yield_interest(self):
        if self.savings_balance > 0:
            self.savings_balance *= self.savings_int_rate
        else:
            print("No interest earned")
        return self
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

    def make_deposit(self,amount,type):
        self.account_balance.deposit(amount,type)
        return self
    
    def make_withdrawal(self, amount,type):
        self.account_balance.withdraw(amount,type)
        return self

    def display_user_balance(self):
        print(f"Hello, {self.name}!")
        self.account_balance.display_account_info()
        return f"User: {self.name}, Balance: ${self.account_balance}"
    
    #def transfer_money(self, user, transfer):
    #    self.user = user
    #    self.account_balance -= transfer

# accounts1 = BankAccount()
# accounts2 = BankAccount()

user1 = User("Jonathan Smith","jonathan.smith722@gmail.com", BankAccount(100, 200))
user2 = User("Meghan Smith", "meghan.smith227@gmail.com", BankAccount(1000, 2000))

user1.make_deposit(500,"savings").make_deposit(5,"checking").make_deposit(50,"checking").make_withdrawal(700,"savings")
user2.make_deposit(600,"savings").make_deposit(60,"checking").make_withdrawal(6,"checking").make_withdrawal(54,"checking").make_withdrawal(100,"savings").make_withdrawal(200,"savings")

user1.display_user_balance()
user2.display_user_balance()
# print(f"Total: {BankAccount.log_account_info()}")

