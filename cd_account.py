"""Import the Account class from the Account.py file."""
from Accounts import Account

class CDAccount(Account):
    """CD Account class that inherits from Account class"""
    pass

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.
    
    Args"
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the Account class and pass in the balance and interest parameters.
    # Hint: You need to add the interest as a value, i.e, 0.
    # cd = CDAccount(balance, interest_rate)
    cd = CDAccount(balance, 0) # better way to start the initial balance with $0 interest rate, but the same result as above

    # Calculate interest earned (APR to monthly rate)
    interest_earned = balance * (interest_rate/100 * months/12)

    # Calculate updated balance
    new_balance = balance + interest_earned

    # Update account balance and interest
    cd.set_balance(new_balance)
    cd.set_interest(interest_earned)

    return new_balance, interest_earned

"""END"""