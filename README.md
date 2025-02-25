1. Class Amount:
Purpose: Represents a transaction (either deposit or withdrawal).
-Attributes:
Amount: The transaction amount.
Timestamp: The time when the transaction was made.
Transaction_type: Either "DEPOSIT" or "WITHDRAWAL".
-Method:
__str__: Returns a formatted string of the transaction details for easy printing.
2. Class PersonalAccount:
-Purpose: Manages a personal bank account.
-Attributes:
account_number: The account's unique number.
account_holder: The name of the account owner.
balance: Current account balance (initially 0).
transactions: A list to store all transaction history.
-Methods:
deposit(amount):
Adds money to the account.
Validates that the amount is positive.
Records the transaction using Amount class.
withdraw(amount):
Withdraws money if sufficient funds are available.
Validates that the amount is positive and checks for sufficient balance.
Records the transaction using Amount class.
print_transaction_history():
Prints all transactions along with the current balance.
get_balance(): Returns the current balance.
get_account_number() & set_account_number(): Get and set the account number.
get_account_holder() & set_account_holder(): Get and set the account holder's name.
__str__: Provides a string representation of the account details.
__add__(amount): Enables using the + operator for deposits.
__sub__(amount): Enables using the - operator for withdrawals.
3. Operator Overloading:
__add__: Overloads + operator to deposit money (account + 300 is the same as account.deposit(300)).
__sub__: Overloads - operator to withdraw money (account - 100 is the same as account.withdraw(100)).
