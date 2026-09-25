def show_menu():
    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Show Total Expenses")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            print("Add Expense selected.")

        elif choice == "2":
            print("View Expenses selected.")

        elif choice == "3":
            print("Delete Expense selected.")

        elif choice == "4":
            print("Show Total Expenses selected.")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()