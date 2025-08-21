"""
You are given a list of product names and a dictionary of product quantities for a grocery store.
Write a function named check_inventory that takes two parameters: products (a list) and quantities (a dictionary).
The function should perform the following checks:

Check if 'Apples' is in the product list.
Check if 'Oranges' is not in the product list.
Check if 'Bananas' is in the quantities dictionary.
Check if 'Grapes' is not in the quantities dictionary.
For each check, print an appropriate message as shown in the test cases.
"""

def check_inventory(products, quantities):
    # Write code here
    print("Apples are in stock.") if "Apples" in products else ""
    "" if "Oranges" in products else print("Oranges are not in stock.")
    print("Bananas quantity is tracked.") if "Bananas" in quantities else ""
    "" if "Grapes" in quantities else print("Grapes quantity is not tracked.")

products = ["Cherries","Oranges","Watermelons","Apples"]
quantities = {"Pears":15,"Cherries":40,"Apples":25}

check_inventory(products, quantities)