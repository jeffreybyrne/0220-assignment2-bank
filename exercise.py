# Part 1: Bank Account
# 1. Create a class called BankAccount.

class BankAccount:

# 2. Add a class variable called interest_rate that is a float representing the interest rate for all the accounts in the bank.
#   This is a class variable because it is the same value for all accounts.
    interest_rate = 1

# 3. Add another class variable called accounts that starts as an empty list. This will eventually store the collection of all
#   bank accounts in the bank.
    accounts = []

# 4. Add an __init__() instance method that sets the bank account's balance to zero. Balance is stored in an instance variable
#   because the value needs to be different from account to account.

    def __init__(self):
        self.balance = 0

# 5. Add an instance method called deposit that accepts a number as an argument and adds that amount to the account's balance.
#   This needs to be an instance method because it pertains to a single, specific account.

    def deposit(self,amount):
        self.balance += amount
# 6. Add an instance method called withdraw that accepts a number as an argument and subtracts that amount from the account's
#   balance.

    def withdraw(self,amount):
        if amount > self.balance:
            print("You cannot withdraw ${:.2f}, the current balance is only ${:.2f}.".format(amount,self.balance))
        else:
            self.balance -= amount
# 7. Add a class method called create that makes a new instance using BankAccount() and adds the new object to the accounts
#   class variable so that we can find it again in the future. This method should return the new account object. This needs
#   to be a class method because at the time we run it there is no single, specific account object that we are working on.

    @classmethod
    def create(cls):
        account = BankAccount()
        cls.accounts.append(account)
        return account
# 8. Add a class method called total_funds that returns the sum of all balances across all accounts in the accounts class variable.
#   This needs to be a class method because it does not pertain to any single, specific account.

    @classmethod
    def total_funds(cls):
        total = 0
        for num in range(0,len(cls.accounts)):
            total += cls.accounts[num].balance
        return total
# 9. Add a class method called interest_time that iterates through all accounts and increases their balances according to the
#   class interest_rate. This needs to be a class method because it operates on all bank accounts, not a single, specific
#   account.

    @classmethod
    def interest_time(cls):
        for num in range(0,len(cls.accounts)):
            curr_account = cls.accounts[num]
            curr_account.balance = curr_account.balance * (1 + curr_account.interest_rate / 100)

my_account = BankAccount.create()
your_account = BankAccount.create()
print(my_account.balance) # 0
print(BankAccount.total_funds()) # 0
my_account.deposit(200)
your_account.deposit(1000)
print(my_account.balance) # 200
print(your_account.balance) # 1000
print(BankAccount.total_funds()) # 1200
BankAccount.interest_time()
print(my_account.balance) # 202.0
print(your_account.balance) # 1010.0
print(BankAccount.total_funds()) # 1212.0
my_account.withdraw(50)
print(my_account.balance) # 152.0
print(BankAccount.total_funds()) # 1162.0
