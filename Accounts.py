""" Create an Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        """Initialize the Account class with balance and interest attributes"""
        self.balance = balance
        self.interest = interest

    # This method gets the balance of the account.
    # Getter methods -- for initial balance
    def get_balance(self):
        """Returns the current balance"""
        return self.balance

    def get_interest(self):
        """Returns the current interest"""
        return self.interest

    #This method sets the balance of the account.
    # Setter methods -- for final balance after interest
    def set_balance(self, balance):
        """Sets the balance for the account"""
        self.balance = balance

    def set_interest(self, interest):
        """Sets the interest gained for the account"""
        self.interest = interest