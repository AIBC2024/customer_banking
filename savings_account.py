"""Import the Account class from the Account.py file."""
from Accounts import Account

class SavingsAccount(Account):
    """Savings Account class that inherits from Account class"""
    pass

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.
    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        And returns the interest earned.   
    """
    # Create an instance of the Account class
    savings = Account(balance, 0)

    # Calculate interest earned (APR to monthly rate)
    interest_earned = balance * (interest_rate/100 * months/12)

    # Calculate updated balance
    new_balance = balance + interest_earned

    # Update account balance and interest
    savings.set_balance(new_balance)
    savings.set_interest(interest_earned)

    return new_balance, interest_earned