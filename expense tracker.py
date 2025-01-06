import os
import json
from datetime import datetime

DATA_FILE = "expenses.json"

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    try:
        date = input("Enter date (YYYY-MM-DD, default is today): ") or datetime.now().strftime("%Y-%m-%d")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        category = input("Enter category (e.g., food, transportation, entertainment): ")

        expense = {
            "date": date,
            "amount": amount,
            "description": description,
            "category": category
        }
        expenses.append(expense)
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Error: Invalid input. Please try again.")

def view_summary(expenses):
    try:
        print("\n--- Expense Summary ---")
        monthly_totals = {}
        category_totals = {}

        for expense in expenses:
            month = expense["date"][:7]  
            monthly_totals[month] = monthly_totals.get(month, 0) + expense["amount"]
            category = expense["category"]
            category_totals[category] = category_totals.get(category, 0) + expense["amount"]

        print("\nMonthly Totals:")
        for month, total in monthly_totals.items():
            print(f"{month}: ${total:.2f}")

        print("\nCategory-wise Totals:")
        for category, total in category_totals.items():
            print(f"{category}: ${total:.2f}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    expenses = load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_summary(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
