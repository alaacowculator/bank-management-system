class Customer:
    """Customer class representing a bank customer"""
    
    def __init__(self, customer_id, name, email, phone):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._phone = phone
        self._accounts = {}  # Dictionary to store accounts
    
    @property
    def customer_id(self):
        return self._customer_id
    
    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
    @property
    def phone(self):
        return self._phone
    
    def add_account(self, account):
        """Add an account to the customer"""
        self._accounts[account.account_number] = account
    
    def get_account(self, account_number):
        """Get a specific account by account number"""
        return self._accounts.get(account_number)
    
    def get_all_accounts(self):
        """Get all accounts of the customer"""
        return list(self._accounts.values())
    
    def get_total_balance(self):
        """Get the total balance across all accounts"""
        return sum(account.balance for account in self._accounts.values())
    
    def __str__(self):
        return f"Customer #{self._customer_id}: {self._name} ({self._email})"