class Account:
    def __init__(self,acc,bal):
        self.Account_number = acc
        self.Balance = bal

    def debit(self,amount):
        self.Balance -= amount 
        print(f"Rs:{amount} was Debited ")
        print("TotalBalance = ",self.total_balance())

    def credit(self,amount):
        self.Balance += amount 
        print(f"Rs:{amount} was Credited ")
        print("TotalBalance = ",self.total_balance())
   
    def total_balance(self):
        return self.Balance
    

acc1 = Account(737535467,100000)
acc2 = Account(287687482,200000)

acc1.debit(10000)
acc1.credit(1000)

print("----------------------------")
acc2.debit(20000)
acc2.credit(1000)