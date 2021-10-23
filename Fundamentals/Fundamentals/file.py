# this is a single line comment

"""
This is 
a multiline
comment
"""

my_new_favorite_language = 'Python' # variable declaration, initialize string

num1 = 42 # - variable declaration - Numbers
num2 = 2.3 # - variable declaration - Float
boolean = True # - variable declaration - Boolean
string = 'Hello World' # - variable declaration - String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # - List - Initialize
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # - Dictionary - Initialize 
fruit = ('blueberry', 'strawberry', 'banana') # - Tuples - Initialize
print(type(fruit)) # - log statement - type check
print(pizza_toppings[1]) # - log statement - access value
pizza_toppings.append('Mushrooms') # - List - add value - string
print(person['name']) # - log statement - Dictionary - access value - key
person['name'] = 'George' # - Dictionary -  change Value - key - string
person['eye_color'] = 'blue' # - Dictionary - add value - key - value - string
print(fruit[2]) # - log statement - access value

if num1 > 45: # - conditional - if - boolean - Variable - Number
    print("It's greater") # - log statement - string 
else: # - conditional - else 
    print("It's lower") # - log statement - string

if len(string) < 5: # - conditional  - if - boolean - length check - variable - Number
    print("It's a short word!") # - log statement - string
elif len(string) > 15: # - conditional - elif - length check - boolean - Number
    print("It's a long word!") # - log statement - string
else: # - conditional - else 
    print("Just right!") # - log statement - string

for x in range(5): # - for loop - variable declaration - stop 
    print(x) # -log statement - variable
for x in range(2,5): # - for loop - variable declaration - start - stop
    print(x) # - log statement - variable
for x in range(2,10,3): # - for loop - variable declaration - start - stop - increment
    print(x) # - log statement - variable
x = 0 # - variable declaration
while(x < 5): # - while loop - variable - start - boolean - number - stop
    print(x) # - log statement - variable
    x += 1 # increment

pizza_toppings.pop() # - list - delete last value
pizza_toppings.pop(1) # - list - delete value at index 1

print(person) # - log statement - dictionary
person.pop('eye_color') # - dictionary - delete value
print(person) # - log statement - dictionary

for topping in pizza_toppings: # for loop - varible declaration - start - List - stop 
    if topping == 'Pepperoni': # - conditional - if - variable - boolean - string from list 
        continue # - for loop - continue
    print('After 1st if statement') # - log statement - string
    if topping == 'Olives': # - conditional - if - variable - boolean - string from list
        break # - for loop - break

def print_hello_ten_times(): # - function - function name - no parameter
    for num in range(10): # - argument - for loop - variable declaration - stop
        print('Hello') # - log statement - string 

print_hello_ten_times() # - call function

def print_hello_x_times(x): # - function - function name - paramenter
    for num in range(x): # - argument - variable declaration - start
        print('Hello') # - log statement - string

print_hello_x_times(4) # - call function - parameter - number

def print_hello_x_or_ten_times(x = 10): # - function - function name - parameter - variable declaration
    for num in range(x): # - for loop - variable declaration - stop
        print('Hello') # - log statement - string

print_hello_x_or_ten_times() # - call function
print_hello_x_or_ten_times(4) # - call function - parameter - number


""" - multiline comment
Bonus section
"""

# print(num3) - NameError: name <variable name> is not defined
# num3 = 72  - NameError: name <variable name> is not defined
# fruit[0] = 'cranberry' - TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) - KeyError: 'favorite_team'
# print(pizza_toppings[7]) - IndexError: list index out of range
#   print(boolean) - IndentationError: unexpected indent
# fruit.append('raspberry') - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'