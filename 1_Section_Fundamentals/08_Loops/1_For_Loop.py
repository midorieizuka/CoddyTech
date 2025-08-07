"""
Sometimes when programming, it's necessary to perform the same or almost the same operation a couple of times.

To prevent writing the same thing over and over again, we can use loops.

The for loop has the following syntax:

for i in range(start, end):
    code

The range(start, end) determines what is the start value and what is the end value. The i will receive all values from start to end (not including end) sequentially. For example:

for i in range(0, 5):
    print(i)

It will execute the print statement 5 times:
0
1
2
3
4

We can simplify the range(0, 5) to range(5):

for i in range(5):
    print(i)

Loops have many use cases. For example, let's sum all the numbers from 1 to 100:

sum_numbers = 0
for i in range(1, 101):
    sum_numbers += i
print(sum_numbers)

This will first loop through all numbers between 1 and 101 (not including 101) and sum all of them. Then it will print the sum_numbers variable.
"""
# Write a program that prints "Hello Coddy: " and the i value from 3 to 27 (including, 25 times in total), do it using a for loop.

for i in range(3, 28):
    print(f"Hello Coddy: {i}")


# Challenge
"""
Write a program that counts the number of even numbers between 10 and 50 (inclusive).

Use a for loop and an if statement to check if each number is even.

Store the count in a variable called count_even.

Remember, you can check if a number is even by using the modulo operator: number % 2 == 0
"""

count_even = 0
for i in range(10, 51):
    if i % 2 == 0:
        count_even += 1
print(f"count_even = {count_even}")