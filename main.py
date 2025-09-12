from bank import Bank
from customer import Customer

def main():
    # Create a bank
    my_bank = Bank("Python OOP")
    
    # Create customers
    customer1 = Customer(1, "Alice Johnson", "alice@email.com", "555-1234")
    customer2 = Customer(2, "Bob Smith", "bob@email.com", "555-5678")
    
    # Add customers to the bank
    my_bank.add_customer(customer1)
    my_bank.add_customer(customer2)
    
    # Create accounts for customers
    alice_savings = my_bank.create_savings_account(1, 1000, 0.03)
    alice_checking = my_bank.create_checking_account(1, 500, 200)
    
    bob_savings = my_bank.create_savings_account(2, 2000, 0.025)
    bob_checking = my_bank.create_checking_account(2, 300, 100)
    
    print("=== Bank Management System ===")
    print(my_bank)
    print()
    
    # Perform transactions
    print("=== Initial Account Balances ===")
    print(f"{customer1.name}: Savings - ${alice_savings.balance}, Checking - ${alice_checking.balance}")
    print(f"{customer2.name}: Savings - ${bob_savings.balance}, Checking - ${bob_checking.balance}")
    print()
    
    # Deposit money
    print("=== Deposits ===")
    print(alice_savings.deposit(200))
    print(bob_checking.deposit(150))
    print()
    
    # Withdraw money
    print("=== Withdrawals ===")
    print(alice_checking.withdraw(100))
    print(bob_savings.withdraw(250))
    print()
    
    # Try to withdraw more than balance (should fail for savings, work for checking with overdraft)
    print("=== Withdrawal Tests ===")
    try:
        print(alice_savings.withdraw(2000))  # Should fail
    except Exception as e:
        print(f"Failed withdrawal: {e}")
    
    print(alice_checking.withdraw(600))  # Should work with overdraft
    print()
    
    # Transfer funds
    print("=== Fund Transfer ===")
    transfer = my_bank.transfer_funds(
        alice_savings.account_number, 
        bob_savings.account_number, 
        100, 
        "Gift"
    )
    print(transfer)
    print()
    
    # Calculate interest
    print("=== Interest Calculation ===")
    print(alice_savings.calculate_interest())
    print(bob_savings.calculate_interest())
    print()
    
    # Show final balances
    print("=== Final Account Balances ===")
    print(f"{customer1.name}: Savings - ${alice_savings.balance:.2f}, Checking - ${alice_checking.balance:.2f}")
    print(f"{customer2.name}: Savings - ${bob_savings.balance:.2f}, Checking - ${bob_checking.balance:.2f}")
    print()
    
    # Show transaction history
    print("=== Transaction History for Alice's Savings ===")
    for transaction in alice_savings.get_transaction_history():
        print(f"  - {transaction}")

if __name__ == "__main__":
    main()