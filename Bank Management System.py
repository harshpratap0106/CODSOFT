## BANK MANAGEMENT SYSTEM 
## BY HARSH P. S. PARIHAR 

from datetime import datetime
import math

class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        name = input("Enter account holder name: ")
        acc_type = input("Enter account type (Savings/Current): ").capitalize()
        balance = float(input("Enter initial deposit: "))
        account_number = len(self.accounts) + 1
        creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if acc_type == "Current" and balance < 5000:
            print("Minimum balance for Current Account is ₹5000.")
            return

        account = {
            'account_number': account_number,
            'name': name,
            'type': acc_type,
            'balance': balance,
            'creation_date': creation_date
        }
        self.accounts.append(account)
        print(f"{acc_type} account created for {name} with Account No: {account_number}")

    def deposit(self):
        acc_no = int(input("Enter account number: "))
        amount = float(input("Enter amount to deposit: "))
        for acc in self.accounts:
            if acc['account_number'] == acc_no:
                acc['balance'] += amount
                print(f"₹{amount} deposited. New balance: ₹{acc['balance']}")
                return
        print("Account not found.")

    def withdraw(self):
        acc_no = int(input("Enter account number: "))
        amount = float(input("Enter amount to withdraw: "))
        for acc in self.accounts:
            if acc['account_number'] == acc_no:
                if acc['type'] == "Current" and acc['balance'] - amount < 5000:
                    print("Cannot withdraw. Minimum balance of ₹5000 must be maintained.")
                elif amount > acc['balance']:
                    print("Insufficient funds.")
                else:
                    acc['balance'] -= amount
                    print(f"₹{amount} withdrawn. Remaining balance: ₹{acc['balance']}")
                return
        print("Account not found.")

    def view_accounts(self):
        if not self.accounts:
            print("No accounts in the bank.")
        else:
            for acc in self.accounts:
                print(f"Account No: {acc['account_number']}, Name: {acc['name']}, Type: {acc['type']}, "
                      f"Balance: ₹{acc['balance']}, Created on: {acc['creation_date']}")

    def apply_interest(self):
        rate = 0.05  # 5% annual interest
        time = float(input("Enter time in years for interest calculation: "))
        for acc in self.accounts:
            if acc['type'] == "Savings":
                ci = acc['balance'] * (math.pow((1 + rate), time) - 1)
                acc['balance'] += ci
                print(f"Compound interest of ₹{ci:.2f} added to account {acc['account_number']}.")

# Menu-driven interface
bank = Bank()

while True:
    print("\nBank Management System")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Accounts")
    print("5. Apply Interest to Savings Accounts")
    print("6. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        bank.create_account()
    elif choice == 2:
        bank.deposit()
    elif choice == 3:
        bank.withdraw()
    elif choice == 4:
        bank.view_accounts()
    elif choice == 5:
        bank.apply_interest()
    elif choice == 6:
        print("Thank you for using Bank Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
