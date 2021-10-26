# class CheckingAccount:
#     def __init__(self, int_rate, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#     def deposit(self, amount):
#         pass# code
#     def withdraw(self, amount):
#         pass# code
#     def write_check(self, amount):
#         pass# code
#     def display_account_info(self):
#         pass# code

# class RetirementAccount:
#     def __init__(self, int_rate, is_roth, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#         self.is_roth = is_roth
#     def deposit(self, amount):
#         pass# code - assess tax if necessary
#     def withdraw(self, amount):
#         pass# code - assess penalty if necessary
#     def display_account_info(self):
#         pass# code

# class CheckingAccount(BankAccount):
#     pass    

# class RetirementAccount(BankAccount):
#     pass

# class RetirementAccount(BankAccount):
#     def __init__(self, int_rate, is_roth, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance
#         self.is_roth = is_roth  

# class BankAccount:
#     def __init__(self, int_rate, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance

# class BankAccount:
#     def __init__(self, int_rate, balance=0):
#         self.int_rate = int_rate
#         self.balance = balance

# class RetirementAccount(BankAccount):
#     def __init__(self, int_rate, is_roth, balance=0):
#         super().__init__(int_rate, balance)	
#         self.is_roth = is_roth	

# class BankAccount:
#     def withdraw(self, amount):
#         if (self.balance - amount) > 0:
#             self.balance -= amount
#         else:
#             print("INSUFFICIENT FUNDS")
#             return self

# class RetirementAccount(BankAccount):
#     def withdraw(self, amount, is_early):
#         if is_early:
#             amount = amount * 1.10
#         if (self.balance - amount) > 0:
#             self.balance -= amount
#         else:
#             print("INSUFFICIENT FUNDS")
#             return self

# class BankAccount:
#     def withdraw(self, amount):
#         if (self.balance - amount) > 0:
#             self.balance -= amount
#         else:
#             print("INSUFFICIENT FUNDS")
#             return self

# class RetirementAccount(BankAccount):
#     def withdraw(self, amount, is_early):
#         if is_early:
#             amount = amount * 1.10
#             super().withdraw(amount)
#             return self