import csv
from datetime import datetime
import os
import matplotlib.pyplot as plt
from typing import List, Dict

class Expense:
    def __init__(self, amount: float, category: str, date: str):
        self.amount = amount
        self.category = category
        self.date = date
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class ExpenseTracker:
    def __init__(self, filename: str = 'expenses.csv'):
        self.filename = filename
        self.expenses: List[Expense] = []
        self.load_expenses()

    def add_expense(self, amount: float, category: str, date: str = None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        
        expense = Expense(amount, category, date)
        self.expenses.append(expense)
        self._save_expense(expense)

    def _save_expense(self, expense: Expense):
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([
                expense.amount, 
                expense.category, 
                expense.date, 
                expense.timestamp
            ])

    def load_expenses(self):
        if not os.path.exists(self.filename):
            return

        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                expense = Expense(
                    amount=float(row[0]), 
                    category=row[1], 
                    date=row[2]
                )
                self.expenses.append(expense)

    def get_total_expenses(self) -> float:
        return sum(expense.amount for expense in self.expenses)

    def get_expenses_by_category(self) -> Dict[str, float]:
        category_totals = {}
        for expense in self.expenses:
            category_totals[expense.category] = category_totals.get(
                expense.category, 0) + expense.amount
        return category_totals

    def generate_category_pie_chart(self):
        category_totals = self.get_expenses_by_category()
        
        plt.figure(figsize=(10, 6))
        plt.pie(
            category_totals.values(), 
            labels=category_totals.keys(), 
            autopct='%1.1f%%'
        )
        plt.title('Expense Distribution by Category')
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig('expense_distribution.png')
        plt.close()

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Total Expenses")
        print("3. View Expenses by Category")
        print("4. Generate Expense Report")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter expense amount: $"))
            category = input("Enter expense category: ")
            tracker.add_expense(amount, category)
            print("Expense added successfully!")

        elif choice == '2':
            print(f"Total Expenses: ${tracker.get_total_expenses():.2f}")

        elif choice == '3':
            category_totals = tracker.get_expenses_by_category()
            for category, total in category_totals.items():
                print(f"{category}: ${total:.2f}")

        elif choice == '4':
            tracker.generate_category_pie_chart()
            print("Expense report generated as 'expense_distribution.png'")

        elif choice == '5':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()