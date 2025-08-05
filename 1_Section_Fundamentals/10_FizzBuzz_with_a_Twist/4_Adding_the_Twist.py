"""
Add a small twist to the game:

Numbers that contain the digit "3" but aren't divisible by 3 or 7 will output Almost Fizz

To check if a string contains a char use in for instance, "a" in word, note that you must cast the number to string for it work use str(num)
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
        elif "3" in str(i):
            print("Almost Fizz")
        else:
            print(str(i))

fizzbuzz(number)