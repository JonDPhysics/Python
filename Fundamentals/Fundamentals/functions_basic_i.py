#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())# log statement that prints the value of the function 'number_of_food_groups()'


#2
def number_of_military_branches():
    return 5
#print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# log statement that tries to access a function that does not exist yet.(caused an error)

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())#log statement that prints the first (return) value of the function 'number_of_books_on_hold()'
# prints the integer 5


#4
def number_of_fingers():
    return 5
    print(10)#log statement that prints the integer 10 when the function 'number_of_fingers()' is called.
print(number_of_fingers())# log statement that calls and prints the function 'number_of_fingers()' which has the value of 5


#5
def number_of_great_lakes():
    print(5)#log statement that prints the integer 5 when the function 'number_of_great_lakes()' is called.
x = number_of_great_lakes()# variable that calls the function 'number_of_great_lakes()
print(x)#log statement that tries to print the value of the function 'number_of_great_lakes()' but there is no value assigned to this fuction.


#6
def add(b,c):
    print(b+c)#log statement that prints the sum of two parameters when the function 'add(b,c)' is called
#print(add(1,2) + add(2,3))
"""
log statement that tries to print the sum of function 'add(b,c)' 
with two combinations of parameters (1,2) and (2,3)
however the function has no value assigned to it (caused an error)""" 


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))#log statement that prints the value of the function 'concatenate(b,c)' with the parameters of (2,5)
#the value printed is the string "25"


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)#log statement that prints the value of the variable b when the function 'number_of_oceans_or_fingers_or_continents()' is called.
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
"""log statement that prints the value assigned to the function 'number_of_oceans_or_fingers_or_continents()'
    the value 10"""


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
"""log statement that prints the value assigned to the function 'number_of_days_in_a_week_silicon_or_triangle_sides(b,c)'
    with the parameters of (2,3)
    prints the value 7"""
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
"""log statement that prints the value assigned to the function 'number_of_days_in_a_week_silicon_or_triangle_sides(b,c)'
    with the parameters of (5,3)
    prints the value of 14"""
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
"""log statement that prints the sum of the values assigned to the function 'number_of_days_in_a_week_silicon_or_triangle_sides(b,c)'
    with two combinations of parameters (2,3) and (5,3)
    prints the sum of 7 and 14 which is 21"""


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
"""log statement that prints the first value assigned to the function 'addition(b,c)'
    with the parameters (3,5)
    prints the value 8"""


#11
b = 500
print(b)#log statment that prints the value assigned to the variable 'b'... 500
def foobar():
    b = 300
    print(b)#log statment that prints the value assigned to the variable 'b' inside the function 'foobar()' when called... 300
print(b)#log statement that prints the value assigned to the variable 'b' outside the function 'foobar()'... 500
foobar()#calls the function 'foobar()'
print(b)#log statement that prints the value assigned to the variable 'b' outside the fuction 'foobar()'... 500


#12
b = 500
print(b)#log statment that prints the value assigned to the variable 'b'... 500
def foobar():
    b = 300
    print(b)#log statment that prints the value assigned to the variable 'b' inside the function 'foobar()' when called... 300
    return b
print(b)#log statement that prints the value assigned to the variable 'b' outside the function 'foobar()'... 500
foobar()#calls the function 'foobar()'
print(b)#log statement that prints the value assigned to the variable 'b' outside the fuction 'foobar()'... 500


#13
b = 500
print(b)#log statment that prints the value assigned to the variable 'b'... 500
def foobar():
    b = 300
    print(b)#log statment that prints the value assigned to the variable 'b' inside the function 'foobar()' when called... 300
    return b
print(b)#log statement that prints the value assigned to the variable 'b' outside the function 'foobar()'... 500
b=foobar()#variable 'b' is changed to the value assigned to the functio 'foobar()'... 300
print(b)#log statement that prints the value assigned to the variable 'b'... 300


#14
def foo():
    print(1)#log statement that prints the integer 1 when the fuction 'foo()' is called.
    bar()#tries to call the fuction'bar()' that does not exist yet. (actually called the function 'bar()')
    print(2)#log statment that prints the integer 2 when the function 'foo()' is called.
def bar():
    print(3)#log statement that prints the integer 3 when the function 'bar()' is called.
foo()#calls the fuciton 'foo('


#15
def foo():
    print(1)#log statement that prints the integer 1 when the fuction 'foo()' is called.
    x = bar()#variable 'x' that tries to assign the value of the function 'bar()' that does not exist yet.
    #(actually assigns the value of the function 'bar()')
    print(x)#log statement that tries to print the variable 'x'
    #(actually calls the function assigned to the variable 'x')
    return 10
def bar():
    print(3)#log statement that prints the integer 3 when the function 'bar()' is called.
    return 5
y = foo()#variable 'y' set to the function 'foo()' that has the value 10 assigned to it.
print(y)#log statement that calls the function 'foo()' and prints the value assigned to it... 10