from datetime import datetime

class Transaction:
    """Transaction class to represent financial transactions"""
    
    def __init__(self, transaction_id, from_account, to_account, amount, description=""):
        self._transaction_id = transaction_id
        self._from_account = from_account
        self._to_account = to_account
        self._amount = amount
        self._description = description
        self._timestamp = datetime.now()
        self._status = "Pending"
    
    def execute(self):
        """Execute the transaction"""
        try:
            # Withdraw from source account
            self._from_account.withdraw(self._amount)
            
            # Deposit to target account
            self._to_account.deposit(self._amount)
            
            self._status = "Completed"
            return True
        except Exception as e:
            self._status = f"Failed: {str(e)}"
            return False
    
    @property
    def transaction_id(self):
        return self._transaction_id
    
    @property
    def status(self):
        return self._status
    
    @property
    def amount(self):
        return self._amount
    
    @property
    def timestamp(self):
        return self._timestamp
    
    def __str__(self):
        return (f"Transaction #{self._transaction_id}: "
                f"${self._amount} from {self._from_account.account_number} "
                f"to {self._to_account.account_number} - {self._status}")