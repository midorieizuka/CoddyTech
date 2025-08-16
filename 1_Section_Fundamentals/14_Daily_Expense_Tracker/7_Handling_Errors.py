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
        value = float(input())
        expense_list.append(value)
        print("Expense added successfully!")
    elif choice == "2":
        if len(expense_list) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for index, item in enumerate(expense_list):
                print(f"{index + 1}. {item}")
    elif choice == "3":
        if len(expense_list) == 0:
            print("No expenses recorded yet.")
        else:
            total = 0
            for item in expense_list:
                total += item
            print(f"Total expense: {total}")
            print(f"Average expense: {total / len(expense_list)}")
    elif choice == "4":
        expense_list.clear()
        print("All expenses cleared.")
    else:
        print("Invalid choice. Please try again.")