# 1. Basic: Print all integers from 0 to 150.
for x in range(0, 151, 1):
    print(x)

#2. Multiples of Five: Print all multipuls from 5 to 1000.
for x in range(5, 1001, 5):
    print(x)

"""
3.Counting, The Dojo Way: 
Print integers 1 to 100.
If divisible by 5, print "Coding" instead.
If divisble by 10, print "Coding Dojo".
"""
for i in range(1,101,1):
    if i % 10 == 0 and i % 5 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

#4.Whoa. That Sucker's Huge: Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
# total = 0
for Jon in range(0,500000, 1):
    # total += Jon
    if Jon % 2 == 1:
        sum += Jon
# print(total)
print(sum)

#5.Countdown by Fours: Print positive numbers starting at 2018, counting down by fours. 
for finalCountDown in range(2018,0,-4):
    print(finalCountDown)

"""
6.Flexible Counter:
Set three variables: lowNum, highNum, mult. 
Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
For example, if lowNum = 2, highNum = 9, and mult=3, the loop should print,3,6,9(on successive lines)
"""
lowNum = 3
highNum = 3333
mult = 9
for dude in range(lowNum,highNum,mult):
    if dude % 3 == 0 and dude % 12 == 0:
        print("sweet")
    elif dude % 3 == 0:
        print("dude")
    else:
        print(dude)