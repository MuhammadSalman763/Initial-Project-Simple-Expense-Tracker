from datetime import datetime


def validate_category():
    while True:
        category = input("Enter Category: ").strip()

        if not category:
            print("Category cannot be empty.")

        elif not category.replace(" ", "").isalpha():
            print("Only letters are allowed.")

        else:
            return category


def validate_amount():
    while True:
        amount = input("Enter Amount: ")

        try:
            amount = float(amount)

            if amount <= 0:
                print("Amount must be greater than zero.")

            return amount

        except ValueError:
            print("Enter a valid amount.")


def validate_date():
    while True:
        date = input("Enter Date (DD-MM-YYYY): ")

        try:
            datetime.strptime(date, "%d-%m-%Y")
            return date

        except ValueError:
            print("Invalid Date.")