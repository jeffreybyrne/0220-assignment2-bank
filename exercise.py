# Part 1: Bank Account
# 1. Create a class called BankAccount.

class BankAccount:

# 2. Add a class variable called interest_rate that is a float representing the interest rate for all the accounts in the bank.
#   This is a class variable because it is the same value for all accounts.
    interest_rate = 2

# 3. Add another class variable called accounts that starts as an empty list. This will eventually store the collection of all
#   bank accounts in the bank.
    accounts = []
    
# 4. Add an __init__() instance method that sets the bank account's balance to zero. Balance is stored in an instance variable
#   because the value needs to be different from account to account.
# 5. Add an instance method called deposit that accepts a number as an argument and adds that amount to the account's balance.
#   This needs to be an instance method because it pertains to a single, specific account.
# 6. Add an instance method called withdraw that accepts a number as an argument and subtracts that amount from the account's
#   balance.
# 7. Add a class method called create that makes a new instance using BankAccount() and adds the new object to the accounts
#   class variable so that we can find it again in the future. This method should return the new account object. This needs
#   to be a class method because at the time we run it there is no single, specific account object that we are working on.
# 8. Add a class method called total_funds that returns the sum of all balances across all accounts in the accounts class variable.
#   This needs to be a class method because it does not pertain to any single, specific account.
# 9. Add a class method called interest_time that iterates through all accounts and increases their balances according to the
#   class interest_rate. This needs to be a class method because it operates on all bank accounts, not a single, specific
#   account.
