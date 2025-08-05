"""
Write a function named sigma with one argument that represents a number n.

The function will return the sum of all the numbers from 1 to n (including).

For example, for sigma(5), the function will return 15, because 15 = 1 + 2 + 3 + 4 + 5.

Important! You don't need to call the function we do that for you behind the scenes in a function type challenges.
"""
n = int(input())
def sigma(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma
print(sigma(n))
