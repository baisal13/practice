from datetime import datetime

class Amount:
    """Represents a transaction amount."""
    def __init__(self, amount: float, transaction_type: str):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type.upper()

    def __str__(self):
        return f"{self.timestamp} - {self.transaction_type}: ${self.amount:.2f}"


class PersonalAccount:
    """Represents a personal bank account."""
    def __init__(self, account_number: int, account_holder: str):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount: float):
        """Deposits money into the account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        transaction = Amount(amount, "DEPOSIT")
        self.transactions.append(transaction)
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount: float):
        """Withdraws money from the account, ensuring sufficient balance."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        transaction = Amount(amount, "WITHDRAWAL")
        self.transactions.append(transaction)
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def print_transaction_history(self):
        """Prints the transaction history of the account."""
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)
        print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        """Returns the current balance."""
        return self.balance

    def get_account_number(self):
        """Returns the account number."""
        return self.account_number

    def set_account_number(self, account_number: int):
        """Sets a new account number."""
        self.account_number = account_number

    def get_account_holder(self):
        """Returns the account holder's name."""
        return self.account_holder

    def set_account_holder(self, account_holder: str):
        """Sets a new account holder's name."""
        self.account_holder = account_holder

    def __str__(self):
        return f"Account {self.account_number} - {self.account_holder}, Balance: ${self.balance:.2f}"

    def __add__(self, amount: float):
        """Allows adding a deposit using the + operator."""
        self.deposit(amount)
        return self

    def __sub__(self, amount: float):
        """Allows withdrawing money using the - operator."""
        self.withdraw(amount)
        return self

if __name__ == "__main__":
    account = PersonalAccount(1001, "John Doe")

    account.deposit(500)
    account.withdraw(200)

    account + 300  # Same as account.deposit(300)
    account - 100  # Same as account.withdraw(100)

    account.print_transaction_history()

    print(account)

