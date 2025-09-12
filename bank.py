from customer import Customer
from account import SavingsAccount, CheckingAccount
from transaction import Transaction

class Bank:
    """Bank class to manage customers, accounts, and transactions"""
    
    def __init__(self, name):
        self._name = name
        self._customers = {}  # Dictionary of customers by ID
        self._accounts = {}   # Dictionary of accounts by account number
        self._transactions = []  # List of transactions
        self._transaction_counter = 10000  # Counter for transaction IDs
    
    @property
    def name(self):
        return self._name
    
    def add_customer(self, customer):
        """Add a customer to the bank"""
        self._customers[customer.customer_id] = customer
    
    def get_customer(self, customer_id):
        """Get a customer by ID"""
        return self._customers.get(customer_id)
    
    def create_savings_account(self, customer_id, initial_balance=0, interest_rate=0.02):
        """Create a savings account for a customer"""
        customer = self.get_customer(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        account = SavingsAccount(customer, initial_balance, interest_rate)
        customer.add_account(account)
        self._accounts[account.account_number] = account
        return account
    
    def create_checking_account(self, customer_id, initial_balance=0, overdraft_limit=100):
        """Create a checking account for a customer"""
        customer = self.get_customer(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        account = CheckingAccount(customer, initial_balance, overdraft_limit)
        customer.add_account(account)
        self._accounts[account.account_number] = account
        return account
    
    def get_account(self, account_number):
        """Get an account by account number"""
        return self._accounts.get(account_number)
    
    def transfer_funds(self, from_account_number, to_account_number, amount, description=""):
        """Transfer funds between accounts"""
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        
        if not from_account or not to_account:
            raise ValueError("One or both accounts not found")
        
        # Create and execute transaction
        transaction_id = self._generate_transaction_id()
        transaction = Transaction(transaction_id, from_account, to_account, amount, description)
        
        success = transaction.execute()
        self._transactions.append(transaction)
        
        return transaction
    
    def _generate_transaction_id(self):
        """Generate a unique transaction ID"""
        self._transaction_counter += 1
        return self._transaction_counter
    
    def get_customer_total_balance(self, customer_id):
        """Get the total balance of all accounts for a customer"""
        customer = self.get_customer(customer_id)
        if not customer:
            raise ValueError("Customer not found")
        
        return customer.get_total_balance()
    
    def get_transaction_history(self, account_number):
        """Get transaction history for an account"""
        account = self.get_account(account_number)
        if not account:
            raise ValueError("Account not found")
        
        return account.get_transaction_history()
    
    def __str__(self):
        return f"{self._name} Bank - {len(self._customers)} customers, {len(self._accounts)} accounts"