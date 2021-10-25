"""
    1.Countdown:
Create a function that accepts a number as an input. 
Return a new list that counts down by one,
from the number (as the 0th element)
down to 0 (as the last element). 
    Example: countdown(5) should return [5,4,3,2,1,0]"""
def countDown(num):
    newList = []
    # for x in range(num,-1,-1):
    #     newList.append(x)
    newList = [x for x in range(num,-1,-1)]
    print(newList)
countDown(5)

"""
    2.Print and Return:
Create a function that will receive a list with two numbers. 
Print the first value and return the second.
    Example: print_and_return([1,2]) should print 1 and return 2"""
def printReturn(jack, jill):
    print(jack)
    return jill
print(printReturn(1,2))
printReturn(3,4)

"""
    3.First Plus Length:
Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
    Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)"""
list = [1,2,3,4,5]
def firstPlusLength(list):
    sum = list[0] + list[len(list)-1]
    return sum
print(firstPlusLength(list))

"""
    4.Values Greater than Second:
Write a function that accepts a list and creates a new list 
containing only the values from the original list that are greater than its 2nd value. 
Print how many values this is and then return the new list. 
If the list has less than 2 elements, have the function return False
    Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
    Example: values_greater_than_second([3]) should return False"""
firstList = [5,2,3,2,1,4]
secondList = [3]
anotherNewList = []
def valuesGreaterThanSecond(list):
    if len(list) < 2:
        return False
    else:
        count = 0
        for num in range(len(list)):
            if list[num] > list[1]:
                count += 1
                anotherNewList.append(list[num])
        print(count)
        return anotherNewList
#valuesGreaterThanSecond(firstList)
print(valuesGreaterThanSecond(firstList))
print(valuesGreaterThanSecond(secondList))

"""
    5.This Length, That Value:
Write a function that accepts two integers as parameters: size and value. 
The function should create and return a list whose length is equal to the given size, 
and whose values are all the given value.
    Example: length_and_value(4,7) should return [7,7,7,7]
    Example: length_and_value(6,2) should return [2,2,2,2,2,2]"""
def lengthValue(this,that):
    yettaNotherNewList = []
    for num in range(0,this):
        yettaNotherNewList.append(that)
    return yettaNotherNewList
print(lengthValue(4,7))
print(lengthValue(6,2))