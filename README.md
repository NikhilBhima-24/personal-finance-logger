# Personal Finance Expense Logger (CLI)

A lightweight, interactive Command Line Interface (CLI) application built in Python for tracking daily expenses. This project demonstrates core programming concepts including standard I/O operations, persistent data storage using JSON, and robust error handling.

## Features
* **Interactive Menu System:** Provides a user-friendly terminal interface for easy navigation between adding and viewing expenses.
* **Persistent Local Storage:** Automatically creates and updates an `expenses.json` file in the root directory to store financial data permanently across sessions.
* **Data Serialization:** Utilizes Python's built-in `json` library to convert Python dictionaries into formatted JSON strings and vice-versa.
* **Input Validation:** Implements `try-except` blocks to prevent the application from crashing if a user inputs non-numeric characters for financial amounts.
* **Zero Dependencies:** Built entirely with the Python Standard Library, meaning no virtual environments or complex `pip` installations are required to run the tool.

## Tech Stack
* **Python 3.x**
* **JSON** (Data Storage Format)

## Installation & Setup

1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/NikhilBhima-24/personal-finance-logger.git](https://github.com/NikhilBhima-24/personal-finance-logger.git)
   cd personal-finance-logger
   ```

2. Verify you have Python installed:
   ```bash
   python --version
   ```

## Usage

Execute the script directly from your terminal. The program will launch the interactive main menu.

```bash
python expense_logger.py
```

### Example Workflow
1. Select option `1` to add an expense.
2. Enter the amount (e.g., `12.50`), category (e.g., `Food`), and description (e.g., `Lunch at cafe`).
3. Select option `2` to view your dynamically generated financial summary and total expenditure.
