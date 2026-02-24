import json
import os
from datetime import datetime

# Define the local storage file
DATA_FILE = 'expenses.json'

def load_expenses():
    """Loads existing expenses from the JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_expenses(expenses):
    """Saves the expenses list to the JSON file."""
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    """Prompts the user to add a new expense record."""
    print("\n--- Add New Expense ---")
    try:
        amount = float(input("Enter amount: $"))
        category = input("Enter category (e.g., Food, Transport, Utilities): ").strip()
        description = input("Enter a brief description: ").strip()
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        expense = {
            "id": len(load_expenses()) + 1,
            "date": date_str,
            "amount": amount,
            "category": category.capitalize(),
            "description": description
        }

        expenses = load_expenses()
        expenses.append(expense)
        save_expenses(expenses)
        
        print("\n✅ Expense logged successfully!\n")
    except ValueError:
        print("\n❌ Invalid input: Amount must be a number. Please try again.\n")

def view_summary():
    """Displays all logged expenses and the total amount spent."""
    expenses = load_expenses()
    
    if not expenses:
        print("\nNo expenses recorded yet. Start by adding one!\n")
        return

    print("\n--- Expense Summary ---")
    total_spent = 0.0
    
    for exp in expenses:
        print(f"[{exp['date']}] {exp['category']}: ${exp['amount']:.2f} - {exp['description']}")
        total_spent += exp['amount']
        
    print("-" * 25)
    print(f"💰 Total Spent: ${total_spent:.2f}\n")

def main():
    """Main application loop."""
    print("Welcome to the Personal Finance Logger CLI")
    
    while True:
        print("Main Menu:")
        print("1. Add an Expense")
        print("2. View Expense Summary")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("\nExiting logger. Have a great day!")
            break
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
