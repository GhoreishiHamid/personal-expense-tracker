import csv
import os
from datetime import datetime

FILE_NAME = "data/expenses.csv"
HEADERS = ["Date", "Amount", "Category", "Description"]


def ensure_data_file():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)


def add_expense():
    ensure_data_file()

    print("\n--- Add New Expense ---")

    while True:
        try:
            amount = float(input("Amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    category = input("Category: ").strip()
    description = input("Description: ").strip()
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, description])

    print("Expense added successfully!")


def view_expenses():
    ensure_data_file()

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = list(csv.reader(file))

    if len(reader) <= 1:
        print("\nNo expenses found.")
        return

    print("\n--- Expense History ---")

    for index, row in enumerate(reader[1:], start=1):
        print(
            f"{index}. Date: {row[0]} | "
            f"Amount: {row[1]} | "
            f"Category: {row[2]} | "
            f"Description: {row[3]}"
        )


def delete_expense():
    ensure_data_file()

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    if len(rows) <= 1:
        print("\nNo expenses found.")
        return

    view_expenses()

    try:
        choice = int(input("\nEnter the expense number to delete: "))

        if choice < 1 or choice > len(rows) - 1:
            print("Invalid expense number.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    deleted_expense = rows.pop(choice)

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print(
        f"Expense '{deleted_expense[3]}' deleted successfully!"
    )


def show_total():
    ensure_data_file()

    total = 0.0

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                total += float(row["Amount"])
            except (ValueError, KeyError):
                continue

    print(f"\nTotal expenses: {total:.2f}")