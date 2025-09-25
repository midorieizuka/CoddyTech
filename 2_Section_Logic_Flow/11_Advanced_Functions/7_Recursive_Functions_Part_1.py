"""
A recursive function calls itself to solve smaller instances of a problem. 
Each recursive call must bring the function closer to a base case, which stops the recursion.

Basic structure:

def recursive_function(parameter):
    if base_case_condition:  # Base case
        return base_value
    return recursive_step  # Recursive step

Example - summing numbers from 1 to n:

def sum_to_n(n):
    if n == 0:  # Base case
        return 0
    return n + sum_to_n(n - 1)  # Recursive step

print(sum_to_n(5))  # Output: 15
"""

def count_down(n):
    # Write code here
    if n < 0:  # Base case
        return
    print(n)
    count_down(n - 1)  # Recursive step

n = int(input())
print(count_down(n))
