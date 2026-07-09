import csv
import os

FILE_NAME = "expenses.csv"

# Create CSV file with header if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Amount", "Date"])

# Function to add an expense
def add_expense():
    category = input("Enter Category: ")
    amount = input("Enter Amount: ")
    date = input("Enter Date (DD-MM-YYYY): ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount, date])

    print("Expense Added Successfully!")

# Function to display all expenses
def view_expenses():
    print("\nExpense List")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)

# Function to calculate total expense
def total_expense():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        for row in reader:
            total += float(row[1])

    print("Total Expense =", total)

# Function to calculate average expense
def average_expense():
    total = 0
    count = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[1])
            count += 1

    if count == 0:
        print("No Expenses Found")
    else:
        print("Average Expense =", total / count)

# Main menu
while True:

    print("\n========== Expense Tracker ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Average Expense")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        average_expense()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")