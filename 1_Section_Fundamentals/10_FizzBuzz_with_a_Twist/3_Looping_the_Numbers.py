"""
Loop over the numbers from 1 to the number that the user entered, and each time use the function you created to calculate the FizzBuzz result and output it.

For example, for input of 7 output:

Welcome to FizzBuzz!
1
2
Fizz
4
5
Fizz
Buzz
"""
print("Welcome to FizzBuzz!")
number = int(input())

def fizzbuzz(number):
    for i in range(1, number + 1):
        if i % 3 == 0:
            if i % 7 == 0:
                print("FizzBuzz") 
            else:
                print("Fizz")
        elif i % 7 == 0:
            print("Buzz")
        else:
            print(str(i))

fizzbuzz(number)


