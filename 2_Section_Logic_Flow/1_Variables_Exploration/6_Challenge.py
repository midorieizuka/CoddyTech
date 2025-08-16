"""
Create a function named calculate_discount that takes two parameters:

price: The original price of an item (float)
discount_percentage: The discount percentage (float)
The function should:

Calculate the discount amount
Subtract the discount amount from the original price
Round the result to 2 decimal places
Return the final discounted price
For example, if the original price is $100 and the discount is 20%, the function should return $80.00.
"""

def calculate_discount(price, discount_percentage):
    # Write code here
    discount_amount = price * (discount_percentage / 100)
    discounted_price = price - discount_amount
    final_price = round(discounted_price, 2)
    return final_price

price = float(input())
discount_percentage = float(input())
calculate_discount(price, discount_percentage)
print(calculate_discount(price, discount_percentage))