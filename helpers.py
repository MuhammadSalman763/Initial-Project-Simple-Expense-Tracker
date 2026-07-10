import csv
import os
import random

from faker import Faker

from config import FILE_NAME, HEADER
from validators import (
    validate_category,
    validate_amount,
    validate_date,
)

fake = Faker()


if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(HEADER)


def generate_fake_data():

    categories = [
        "Food",
        "Shopping",
        "Medical",
        "Transport",
        "Travel",
        "Bills",
        "Education",
        "Entertainment"
    ]

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        for _ in range(100):

            writer.writerow([
                random.choice(categories),
                round(random.uniform(100, 10000), 2),
                fake.date_between(
                    start_date="-2y",
                    end_date="today"
                ).strftime("%d-%m-%Y")
            ])

    print("100 Fake Records Added Successfully.")


def add_expense():

    category = validate_category()
    amount = validate_amount()
    date = validate_date()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount, date])

    print("Expense Added Successfully.")


def view_expenses():

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            print(row)


def total_expense():

    total = 0

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:
            total += float(row[1])

    print("Total Expense =", total)


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
        print("No Expense Found")
    else:
        print("Average =", round(total / count, 2))