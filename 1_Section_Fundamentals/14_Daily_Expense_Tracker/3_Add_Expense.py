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
    elif choice == "1":
        value = int(input())
        expense_list.append(value)
        print("Expense added successfully!")
        print(expense_list)