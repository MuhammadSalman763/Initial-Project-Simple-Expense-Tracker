from helpers import (
    add_expense,
    view_expenses,
    total_expense,
    average_expense,
    generate_fake_data
)


def menu():

    while True:

        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Total Expense")
        print("4. Average Expense")
        print("5. Generate 100 Fake Records")
        print("6. Exit")

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
            generate_fake_data()

        elif choice == "6":
            print("Good Bye")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()