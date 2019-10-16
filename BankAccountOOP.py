class Account:

    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Account Owner: %s\nAccount balance: %s$" %(self.owner, self.balance)

    def deposit(self,amount):
        self.balance += amount
        print("Deposit Accepted")

    def withdraw(self,amount):
        if self.balance < amount:
            print("Funds Unavailable!")
        else:
            self.balance -= amount
            print("Withdrawal Accepted")


# 1. Instantiate the class
acct1 = Account('Jose',100)

# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
print(acct1.owner)

# 4. Show the account balance attribute
print(acct1.balance)

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)
acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)