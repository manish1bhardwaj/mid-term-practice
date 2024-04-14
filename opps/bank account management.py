class bankACC:
    def __init__(self,account_number,owner,balance = 0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
    def deposit(self,deposit_amount):
        if deposit_amount<=0:
            raise ValueError("Amount must be positive!")
        self.balance+=deposit_amount
    
    def withdraw(self,withdrawal_amount):
        if withdrawal_amount<=0:
            raise ValueError("Amount  must be positive!")
        elif withdrawal_amount>=self.balance:
            raise ValueError("Not enough money in acoount!")
        else:
            self.balance-=withdrawal_amount
            print("Amount withdrawn successfully!")
    def check_balance(self):
        return f'''
Owner Name :{self.owner}
Account Number:{self.account_number} 
Current Balance:{self.balance}
'''
#maincode
Account_holder = input("Enter the Account Holder Name : ")

Account1=bankACC('12345677973','Manish Bhardwaj',100000)
print()



#main code 
class SavingsAccount(bankACC):
    def __init__ (self,account_number,Account_holder,balance=0, interest_rate=0.02):
        super().__init__(account_number , Account_holder,balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest  = self.balance = self.interest_rate
        self.balance += interest
        print(f"interest added:{interest}, New balance:{self.balance}")

if __name__ == '__main__':
    savings_account = SavingsAccount(account_number=123,Account_holder='ravi',balance = 1000)
    checking_account = CheckingAccount(account_number=456,Account_holder = 'saket',balance=500,overdraft = 200)

    #Deposit and display for both accounts
    savings_account.deposit(200)
    savings_account