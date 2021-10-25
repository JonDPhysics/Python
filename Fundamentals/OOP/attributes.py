class User:
# class attributes get defined in the class 
    bank_name = "First National Dojo"
# now our method has 2 parameters!
    def __init__(self , name, email_address):
# we assign them accordingly
        self.name = name
        self.email = email_address
# the account balance is set to $0
        self.account_balance = 0
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
print(guido.name)# output: Guido van Rossum
print(monty.name)# output: Monty Python

