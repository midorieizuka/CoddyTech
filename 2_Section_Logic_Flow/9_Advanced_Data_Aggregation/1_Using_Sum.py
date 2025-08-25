"""
The sum() function is a built-in function that allows you to quickly calculate the sum of elements in an iterable, such as a list or a tuple.
It provides a concise way to add up numeric values.

Basic Usage:

numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)
# Output: 15

In this example, the sum() function calculates the sum of all elements in the numbers list.

Using a Starting Value:

You can also provide a second argument to sum(), which serves as the starting value for the sum.
This is useful when you want to add the elements of an iterable to an initial value.

numbers = [1, 2, 3, 4, 5]
total = sum(numbers, 10)
print(total)
# Output: 25

In this case, the sum() function starts with the value 10 and adds all elements from the numbers list to it.

Write a program that gets a list of sales amounts and starting cash in the register and calculates the total sales, including the starting cash.
Print the result.
"""

sales = eval(input())
starting_cash = eval(input())

# Write code here
total_sales = sum(sales, starting_cash)
print(total_sales)