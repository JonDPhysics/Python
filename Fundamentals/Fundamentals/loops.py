for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

for x in 'Hello':
    print(x)
# output: 'H', 'e', 'l', 'l', 'o'

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz

# OR 
for v in my_list:
    print(v)
# output: abc, 123, xyz

dog = ("Poodle", "Lab", "Great Dane", "Black Lab")
for data in dog:
    print(data)

my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

my_dict = { "name": "Jonathan", "language": "Japanese" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
    print(val)
#output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

for count in range(0,5):
    print("looping =", count)

count = 0
while count <= 5:
    print("looping - ", count)
    count += 1

count = 0
stop = True
while stop == True:
    for x in range(0, 102, 2):
        print(x)
        if x == 100:
            stop = False
        else:
            count += 1
print(count)
# do something, including progress towards making the expression False. Otherwise we'll never get out of here!

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1

