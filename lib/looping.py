#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i>0 :
        print (i)
        i = i-1
    print ("Happy New Year!")

def square_integers(int_list):
    squared_list = [integer * integer for integer in int_list]
    print (squared_list)

def fizzbuzz():
    i=0
    while i <= 100 :

        divisible_by_three = i % 3
        divisible_by_five = i % 5

        if divisible_by_three == 0 and divisible_by_five == 0:
            print("Fizzbuzz")
        elif divisible_by_three == 0 and divisible_by_five != 0:
            print("Fizz")
        elif divisible_by_three != 0 and divisible_by_five == 0:
            print("Buzz")
        else:
            print(i)
        i = i+1

    

happy_new_year()
square_integers([1, 2, 3, 4, 5])
fizzbuzz()
