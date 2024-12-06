# customer-banking
Python Challenge AI Bootcamp due 12/17/2024

1. Starter files:
    a. Accounts.py - contains Account classes
    b. savings_account.py
    c. cd_account.py
    d. customer_banking.py
    e. Account.py - contains the class with methods to set the balance and interest


## Project Overview
1. Create a customer banking system that allows users to calculate and track interest earned on Savings and CD accounts
2. Run Python program where users can:
    a. Enter their savings and CD original balance info
    b. Enter the interest rate (%APR)
    c. Enter the term in months. Note: if months entered is not integer it will discard any decimals from data entry
    d. The customer_banking,py program will calculate the new balances with the parameters entered above and provide summary
    e. Validations are placed if numbers are not positive or include special characters

## How I did my work
1. Downloaded the homework starter file
2. Created pseudo code by outlining what needs to be done
3. Received help from ChatGPT, Google, and Claude.AI, modified things that needed to be done to comply with instructions
4. Debug and test multiple times
5. Added better print output for better results (this is extra work but will improve user experience) 

## Output Examples, copy paste from the terminal after the program was run

```
=== Savings Account ===
Enter initial savings balance: $5250.81
Enter savings interest rate (APR %): 4.23%
Please enter a valid number without special characters.
Please enter a positive number.
Enter savings interest rate (APR %): 4.23
Enter term (months): 28.5

Savings Account Summary:
Starting balance: $5,250.81
Interest earned: $518.25
For 28 months at 4.23% APR
Updated balance: $5,769.06

=== CD Account ===
Enter initial CD balance: $10178.29
Enter CD interest rate (APR %): 6.21
Enter term (months): 3.7

CD Account Summary:
Starting balance: $10,178.29
Interest earned: $158.02
For 3 months at 6.21% APR
Updated balance: $10,336.31

```



