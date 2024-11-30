class BankSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder, initial_balance=0):
        if account_holder not in self.accounts:
            self.accounts[account_holder] = {"balance": initial_balance}
            print(f"Account created for {account_holder} with an initial balance of {initial_balance}.")
        else:
            print(f"Account for {account_holder} already exists.")

    def deposit(self, account_holder, amount):
        if account_holder in self.accounts:
            if amount > 0:
                self.accounts[account_holder]["balance"] += amount
                print(f"Deposited {amount} to {account_holder}'s account. New balance: {self.accounts[account_holder]['balance']}")
            else:
                print("Deposit amount must be greater than zero.")
        else:
            print(f"Account for {account_holder} does not exist.")

    def withdraw(self, account_holder, amount):
        if account_holder in self.accounts:
            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")
            elif amount > self.accounts[account_holder]["balance"]:
                print("Insufficient balance to withdraw.")
            else:
                self.accounts[account_holder]["balance"] -= amount
                print(f"Withdrew {amount} from {account_holder}'s account. New balance: {self.accounts[account_holder]['balance']}")
        else:
            print(f"Account for {account_holder} does not exist.")

    def check_balance(self, account_holder):
        if account_holder in self.accounts:
            print(f"Current balance for {account_holder}: {self.accounts[account_holder]['balance']}")
        else:
            print(f"Account for {account_holder} does not exist.")

    def show_all_accounts(self):
        if not self.accounts:
            print("No accounts available.")
        else:
            print("\n--- List of Accounts ---")
            for account_holder, details in self.accounts.items():
                print(f"{account_holder}: {details['balance']}")


def show_menu():
    print("\n--- Banking System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Show All Accounts")
    print("6. Exit")


def main():
    bank = BankSystem()

    while True:
        show_menu()
        choice = input("Please choose an option (1-6): ")

        if choice == '1':
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance (default 0): "))
            bank.create_account(account_holder, initial_balance)
        elif choice == '2':
            account_holder = input("Enter account holder name: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(account_holder, amount)
        elif choice == '3':
            account_holder = input("Enter account holder name: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(account_holder, amount)
        elif choice == '4':
            account_holder = input("Enter account holder name: ")
            bank.check_balance(account_holder)
        elif choice == '5':
            bank.show_all_accounts()
        elif choice == '6':
            print("Thank you for using the banking system!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
