"""
Arithmetic operations can also be done on strings. For example:

str1 = "aaa" + "b"
str1 will hold "aaab"

This is the same as:

str1 = "aaa"
str1 += "b"
Also, we can use multiplications:

str1 = "a"*10
str1 will hold "aaaaaaaaaa"

Each test case has one input - an odd whole number (always odd, given).
Your task is to print n - pyramid using *, here are some examples:

1 - pyramid
*
5 - pyramid
*
***
*****
7 - pyramid
*
***
*****
*******
Input
odd integer n from user
1 <= n < 1000
Tips
Try starting from the small triangles
Check the hint if you are stuck ;)
n represents the number of  * in the bottom row
"""
n = int(input())
rows = int(n/2)+1
for i in range(rows):
    stars = "*" * (i * 2 + 1)
    print(stars)