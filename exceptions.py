class InsufficientFundsError(Exception):
    """Exception raised when there are insufficient funds for a transaction"""
    pass

class AccountNotFoundError(Exception):
    """Exception raised when an account is not found"""
    pass

class CustomerNotFoundError(Exception):
    """Exception raised when a customer is not found"""
    pass