"""
Add a function named fizzbuzz that gets one number (int) as an argument, and:

If the number is divisible by 3, return "Fizz".
If the number is divisible by 7, return "Buzz".
If the number is divisible by both 3 and 7, return "FizzBuzz".

If none of the above conditions are met, return the number itself in a string format.
After the function:

Get input and cast it to int
Call the function fizzbuzz with the input number
Print the output of the function
"""
print("Welcome to FizzBuzz!")
number = int(input())

def fizzbuzz(number):
    if number % 3 == 0:
        if number % 7 == 0:
            return "FizzBuzz"
        else:
            return "Fizz"
    elif number % 7 == 0:
        return "Buzz"
    else:
        return str(number)      
    
fizzbuzz(number)
print(fizzbuzz(number))