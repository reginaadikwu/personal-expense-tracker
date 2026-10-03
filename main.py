import csv
from datetime import datetime

FILENAME = "expenses.csv"

def initialize_file():
    try:
        with open(FILENAME, 'x', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass

def add_expense():
    category = input("Enter category (e.g., Food, Transport, Rent): ").strip()
    try:
        amount = float(input("Enter amount ($): "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    desc = input("Enter description: ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    with open(FILENAME, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([date, category, amount, desc])
    print("Expense added successfully!")

def view_summary():
    try:
        with open(FILENAME, 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skip header
            total = 0
            categories = {}
            
            print("\n--- Expense History ---")
            for row in reader:
                if not row: continue
                date, cat, amt, desc = row
                amt = float(amt)
                total += amt
                categories[cat] = categories.get(cat, 0) + amt
                print(f"[{date}] {cat}: ${amt:.2f} - {desc}")
            
            print(f"\nTotal Spent: ${total:.2f}")
            print("Breakdown by Category:")
            for cat, amt in categories.items():
                print(f" - {cat}: ${amt:.2f}")
    except FileNotFoundError:
        print("No expenses recorded yet.")

def main():
    initialize_file()
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Summary & History")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
