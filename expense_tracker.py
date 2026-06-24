import json 
import os

def load_expenses():
    if os.path.exists("expense.json"):
        with open("expense.json", "r") as f:
            return json.load(f)
    return[]


def save_expenses(expenses):
    with open("expense.json", "w")as f:
        json.dump(expenses, f, indent=2)

def add_expense(expenses):
    amount = float(input("Enter the amount: "))
    category = input("Enter category: ")
    expenses.append({
        "amount":amount,
        "category":category
    })
    save_expenses(expenses)
    print(f"Expense of '{amount}' Added to '{category}'")


def view_expenses(expenses):
    if not expenses:
        print("No expenses!")

    else:
        for index, expense in enumerate(expenses):
            print(f" '{index+1}'. {expense['category']} - {expense['amount']}")


def show_total(expenses):
    total = 0
    for expense in expenses:
        total += expense['amount']
    print(f"Total Expense : {total}")


def main():
    expenses = load_expenses()

    while True:
        print("\n Expense Tracker")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Show Total Expenses")
        print("4. Exit")

        choice = input("Enter a choice: ")
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            print("Bye")
            return
        else:
            print("invalid choice!")
            
main()
