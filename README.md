# Personal Expense Tracker

A lightweight command-line application for tracking personal expenses, built with Python.

The application allows users to record daily expenses, organize them by category, review previous entries, delete records, and calculate total spending. Expense data is stored locally in a CSV file, keeping the project simple and easy to run without a database or external dependencies.

## Features

- Add expenses with an amount, category, and description
- Automatically record the date of each entry
- View all recorded expenses
- Delete expenses by selecting an entry
- Calculate total spending
- Validate numerical input
- Store data locally in CSV format

## Project Structure

personal-expense-tracker/
├── data/
│   └── expenses.csv
├── .gitignore
├── README.md
├── expense.py
└── main.py
## Requirements

- Python 3.x

No external packages are required.

## Getting Started

Clone the repository:

git clone YOUR_REPOSITORY_URL
Move into the project directory:

cd personal-expense-tracker
Run the program:

python main.py
## Usage

After starting the application, the following menu is displayed:

===== Personal Expense Tracker =====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Show Total Expenses
5. Exit
Select an option by entering its corresponding number. Expense records are saved in data/expenses.csv.

## Example Data

Date,Amount,Category,Description
2026-09-20,12.50,Food,Lunch
2026-09-21,8.00,Transport,Bus ticket
2026-09-22,25.00,Education,Programming book
## Possible Improvements

Some features that could be added in future versions include:

- Filtering expenses by date or category
- Monthly and yearly spending summaries
- Automated tests
- Data visualization
- Database support
