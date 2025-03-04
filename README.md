# Project Overview: ATM Transaction System
This project is a simple ATM (Automated Teller Machine) transaction system implemented in Python. It allows users to deposit and withdraw money, track their balance, process transactions from a file, and save transaction records. It also includes error handling for insufficient funds and invalid transactions.

# Key Features:
Deposit and Withdraw Money

The deposit(amount) method adds funds to the account.
The withdraw(amount) method deducts funds, but raises an InsufficientFundsError if there are not enough funds.
Balance Inquiry

The get_balance() method returns the current account balance.
Transaction Processing from a File

The process_transactions(filename) method reads a file containing transactions (e.g., deposit 100, withdraw 50), executes them, and logs errors for invalid actions or insufficient funds.
Saving Transactions to a File

The save_transactions_to_file(filename) method records transactions with timestamps into a file for future reference.
Error Handling

The program handles invalid transaction actions (e.g., typos in the transaction file).
It raises a custom InsufficientFundsError if a withdrawal exceeds the balance.
If the specified transaction file is missing, it creates a new one.
Testing the ATM System

The test_ATM() function simulates deposits, withdrawals, and error handling.
It tests withdrawals beyond the available balance to ensure exceptions are properly raised.
It reads and processes transactions from "transactions.txt".
It saves all completed transactions to "saved_transactions.txt".
How It Works:
The program initializes an ATM instance with a balance of 0.0.
Transactions can be added manually (via function calls) or read from a text file.
Transactions are logged with timestamps when saved.
Errors are caught and displayed to prevent crashes.
