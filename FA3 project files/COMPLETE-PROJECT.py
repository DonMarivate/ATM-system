from datetime import datetime

# Define a custom exception for insufficient funds
class InsufficientFundsError(Exception):
    pass

# Define the ATM class
class ATM:
    def __init__(self):
        # Initialize balance and transactions list
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        # Add deposited amount to balance
        self.balance += amount
        # Record transaction
        self.transactions.append(f"Deposit {amount}")

    def withdraw(self, amount):
        # Check if sufficient funds are available
        if self.balance < amount:
            raise InsufficientFundsError("Insufficient funds")
        # Subtract withdrawn amount from balance
        self.balance -= amount
        # Record transaction
        self.transactions.append(f"Withdraw {amount}")

    def get_balance(self):
        # Return current balance
        return self.balance

    def process_transactions(self, filename):
        try:
            # Open file for reading
            with open(filename, 'r') as file:
                # Read each line from the file
                for line in file:
                    try:
                        # Split each line into action and amount
                        action, amount = line.strip().split()
                        print(f"Processing transaction: {action} {amount}")  # Debugging print statement
                        if action == 'deposit':
                            # Call deposit method if action is deposit
                            self.deposit(float(amount))
                        elif action == 'withdraw':
                            # Call withdraw method if action is withdraw
                            self.withdraw(float(amount))
                        else:
                            # Raise ValueError for invalid action
                            raise ValueError("Invalid action")
                    except (ValueError, InsufficientFundsError) as e:
                        # Print error message for invalid transactions or insufficient funds
                        print(f"Error processing transaction: {e}")
        except FileNotFoundError:
            # If file not found, create the file and inform the user
            print(f"File '{filename}' not found. Creating the file...")
            # Open file in write mode to create it
            with open(filename, 'w') as file:
                # File created, no need to process transactions
                print("File created successfully.")

    def save_transactions_to_file(self, filename):
        # Open file for writing
        with open(filename, 'w') as file:
            # Write each transaction to the file
            for transaction in self.transactions:
                # Add timestamp for each transaction
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp}: {transaction}\n")
                print(f"Transaction saved to file: {timestamp}: {transaction}")  # Debugging print statement

# Test the ATM class
def test_ATM():
    atm = ATM()
    atm.deposit(100)
    atm.withdraw(50)
    
    try:
        atm.withdraw(70)  # This should raise InsufficientFundsError
    except InsufficientFundsError as e:
        print(f"Expected exception caught: {e}")
    
    atm.process_transactions("transactions.txt")
    atm.save_transactions_to_file("saved_transactions.txt")

test_ATM()
