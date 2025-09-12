from abc import ABC, abstractmethod
from exceptions import InsufficientFundsError

class Account(ABC):
    """Abstract base class for all account types"""
    
    _account_counter = 1000  # Class variable for generating account numbers
    
    def __init__(self, owner, initial_balance=0):
        self._account_number = Account._generate_account_number()
        self._owner = owner
        self._balance = initial_balance
        self._transactions = []
    
    @classmethod
    def _generate_account_number(cls):
        """Class method to generate unique account numbers"""
        cls._account_counter += 1
        return cls._account_counter
    
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def owner(self):
        return self._owner
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
        self._transactions.append(f"Deposit: +${amount}")
        return f"Deposited ${amount}. New balance: ${self._balance}"
    
    def withdraw(self, amount):
        """Withdraw money from account - abstract method to be implemented by subclasses"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal")
        self._balance -= amount
        self._transactions.append(f"Withdrawal: -${amount}")
        return f"Withdrew ${amount}. New balance: ${self._balance}"
    
    @abstractmethod
    def calculate_interest(self):
        """Abstract method to calculate interest - to be implemented by subclasses"""
        pass
    
    def get_transaction_history(self):
        """Return transaction history"""
        return self._transactions
    
    def __str__(self):
        return f"Account #{self._account_number} - Balance: ${self._balance}"


class SavingsAccount(Account):
    """Savings account with interest calculation"""
    
    def __init__(self, owner, initial_balance=0, interest_rate=0.02):
        super().__init__(owner, initial_balance)
        self._interest_rate = interest_rate
    
    def calculate_interest(self):
        """Calculate and add interest to balance"""
        interest = self._balance * self._interest_rate
        self._balance += interest
        self._transactions.append(f"Interest: +${interest:.2f}")
        return f"Interest of ${interest:.2f} added. New balance: ${self._balance:.2f}"
    
    def __str__(self):
        return f"Savings Account #{self.account_number} - Balance: ${self.balance:.2f}"


class CheckingAccount(Account):
    """Checking account with overdraft protection"""
    
    def __init__(self, owner, initial_balance=0, overdraft_limit=100):
        super().__init__(owner, initial_balance)
        self._overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        """Withdraw money with overdraft protection"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > (self._balance + self._overdraft_limit):
            raise InsufficientFundsError("Exceeds overdraft limit")
        
        self._balance -= amount
        self._transactions.append(f"Withdrawal: -${amount}")
        return f"Withdrew ${amount}. New balance: ${self._balance}"
    
    def calculate_interest(self):
        """Checking accounts typically don't earn interest"""
        return "No interest earned on checking accounts"
    
    def __str__(self):
        return f"Checking Account #{self.account_number} - Balance: ${self.balance:.2f}"