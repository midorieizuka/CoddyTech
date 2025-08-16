"""
Now let's create the actual program!

Create an infinite while loop (refer the hint if not sure how to do so)
In each iteration of the loop, get input from the user, this will be the choice (1 - 5 from the menu)
Handle the first case, if the choice is equal to 5, exit the program (loop) and output:
Exiting the Daily Expense Tracker. Goodbye!
"""

print("Welcome to the Daily Expense Tracker!")
print()
print("Menu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")

expense_list = []
while True:
	# Code here
    choice = input()
    if choice == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break

