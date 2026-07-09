import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

# Create CSV file with header if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Amount", "Date"])


# ----------------------------
# Validation Functions
# ----------------------------

def validate_category():
    while True:
        category = input("Enter Category: ").strip()

        if category == "":
            print("Error: Category cannot be empty.")

        elif not category.replace(" ", "").isalpha():
            print("Error: Category should contain only letters.")

        else:
            return category


def validate_amount():
    while True:
        amount = input("Enter Amount: ").strip()

        try:
            amount = float(amount)

            if amount <= 0:
                print("Error: Amount must be greater than 0.")

            else:
                return amount

        except ValueError:
            print("Error: Enter a valid numeric amount.")


def validate_date():
    while True:
        date = input("Enter Date (DD-MM-YYYY): ").strip()

        try:
            datetime.strptime(date, "%d-%m-%Y")
            return date

        except ValueError:
            print("Error: Invalid date format. Use DD-MM-YYYY.")


# ----------------------------
# Add Expense
# ----------------------------

def add_expense():

    category = validate_category()
    amount = validate_amount()
    date = validate_date()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount, date])

    print("\nExpense Added Successfully!")


# ----------------------------
# View Expenses
# ----------------------------

def view_expenses():

    print("\n========== Expense List ==========")

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        for row in reader:
            print(row)


# ----------------------------
# Total Expense
# ----------------------------

def total_expense():

    total = 0

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            try:
                total += float(row[1])

            except ValueError:
                continue

    print("\nTotal Expense =", total)


# ----------------------------
# Average Expense
# ----------------------------

def average_expense():

    total = 0
    count = 0

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            try:
                total += float(row[1])
                count += 1

            except ValueError:
                continue

    if count == 0:

        print("No Expenses Found")

    else:

        average = total / count
        print("Average Expense =", round(average, 2))


# ----------------------------
# Main Menu
# ----------------------------

while True:

    print("\n========== Expense Tracker ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Average Expense")
    print("5. Exit")

    choice = input("Enter Choice: ").strip()

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

        print("Invalid Choice! Please enter a number between 1 and 5.")