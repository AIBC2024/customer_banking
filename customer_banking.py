## RUN THIS FILE FOR RESULTS

"""Import required modules"""
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define input validator using lambda
## validate_number = lambda x: float(x) if float(x) > 0 else None

# Regular function instead
def validate_number(x): # this is Python keyword to define a function
    """
    Validates if the input is a positive number
    Args: x (str): The input to validate
    Returns: float or None: Returns float if positive, None otherwise
    """
    while True:
        try: # this is Python keyword for exception handling
            customer_input = float(x)
            if customer_input > 0:
                return customer_input
            return None
        except ValueError: # this is Python keyword for exception handling
            print("Please enter a valid number without special characters.")
            return None # return is Python keyword to send value back from function. None is Python built-in constant

def get_valid_input(prompt):
    """Helper function to get valid numerical input"""
    while True:
        try:
            customer_input_value = validate_number(input(prompt))
            if customer_input_value is not None:
                return customer_input_value
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid number without special characters.")

def main():
    """Main function for the banking application"""
    # Get savings account details
    print("\n=== Savings Account ===")
    savings_balance = get_valid_input("Enter initial savings balance: $")
    savings_interest = get_valid_input("Enter savings interest rate (APR %): ")
    savings_maturity = int(get_valid_input("Enter term (months): "))

    # Create savings account and display results
    updated_savings_balance, savings_interest_earned = create_savings_account(
        savings_balance, savings_interest, savings_maturity
    )
    print(f"\nSavings Account Summary:")
    print(f"Starting balance: ${savings_balance:,.2f}")
    print(f"Interest earned: ${savings_interest_earned:,.2f}")
    print(f"For {savings_maturity} months at {savings_interest}% APR")
    print(f"Updated balance: ${updated_savings_balance:,.2f}")

    # Get CD account details
    print("\n=== CD Account ===")
    cd_balance = get_valid_input("Enter initial CD balance: $")
    cd_interest = get_valid_input("Enter CD interest rate (APR %): ")
    cd_maturity = int(get_valid_input("Enter term (months): "))

    # Create CD account and display results
    updated_cd_balance, cd_interest_earned = create_cd_account(
        cd_balance, cd_interest, cd_maturity
    )
    print(f"\nCD Account Summary:")
    print(f"Starting balance: ${cd_balance:,.2f}")
    print(f"Interest earned: ${cd_interest_earned:,.2f}")
    print(f"For {cd_maturity} months at {cd_interest}% APR")
    print(f"Updated balance: ${updated_cd_balance:,.2f}")

if __name__ == "__main__":
    main()