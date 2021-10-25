"""
1.Update Values in Dictionaries and Lists
    Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
    Change the last_name of the first student from 'Jordan' to 'Bryant'
    In the sports_directory, change 'Messi' to 'Andres'
    Change the value 20 in z to 30"""

print("Challenge 1")
print("--------------------------------------------")
x = [ [5,2,3], [10,8,9] ]
def changeValue(x):
    x[1][0] = 15

changeValue(x)
print(x)

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}]
def changeLastName(jack):
    jack[0]['last_name'] = 'Bryant'

changeLastName(students)
print(students[0]['last_name'])

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']}
def change(jill):
    jill['soccer'][0] = 'Andres'

change(sports_directory)
print(sports_directory['soccer'][0])

z = [ {'x': 10, 'y': 20} ]
def changeTheValue(duck):
    duck[0]['y'] = 30

changeTheValue(z)
print(z[0]['y'])

"""
2.Iterate Through a List of Dictionaries
    Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
    the function loops through each dictionary in the list and prints each key 
    and the associated value. For example, given the following list:"""

print("--------------------------------------------")
print("Challenge 2")
print("--------------------------------------------")
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}]

def iterateDictionary(some_list):
    dict_values = []
    for i in range(len(some_list)):
        for key in some_list[i]:
            dict_values.append(some_list[i][key])

    print(f'first_name - {dict_values[0]}, last_name - {dict_values[1]}')
    print(f'first_name - {dict_values[2]}, last_name - {dict_values[3]}')
    print(f'first_name - {dict_values[4]}, last_name - {dict_values[5]}')
    print(f'first_name - {dict_values[6]}, last_name - {dict_values[7]}')

iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
#bonus to get them to appear exactly as below!)
"""
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
"""

"""
3.Get Values From a List of Dictionaries
    Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries
    and a key name, the function prints the value stored in that key for each dictionary.
    For example, iterateDictionary2('first_name', students) should output:"""

print("--------------------------------------------")
print("Challenge 3")
print("--------------------------------------------")
def iterateDictionary2(key_name,some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2('first_name',students)
print("-------------------------")
iterateDictionary2('last_name',students)

"""
4.Iterate Through a Dictionary with List Values
    Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
    prints the name of each key along with the size of its list,
    and then prints the associated values within each key's list.
        For example:
                    7 LOCATIONS     8 INSTRUCTORS
                    San Jose        Michael
                    Seattle         Amy
                    Dallas          Eduardo
                    Chicago         Josh
                    Tulsa           Graham
                    DC              Patrick
                    Burbank         Minh
                                    Devon"""

print("--------------------------------------------")
print("Challeng 4")
print("--------------------------------------------")
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}

def printInfo(some_dict):
    for key in some_dict:
        print(f" {len(some_dict[key])} {key.upper()} ")
        for i in range(len(some_dict[key])):
            print(some_dict[key][i])
        print("-------------------------")

printInfo(dojo)