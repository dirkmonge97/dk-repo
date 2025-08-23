
class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    
    def add_money(self,amount):
        amount=float(amount)
        self.balance+=amount


    def reduce_balance(self,amount):
        amount=float(amount)
        self.balance-=amount



class SavingsAccount(BankAccount):
    def __init__(self,balance,min_balance):
        super().__init__(balance)
        self.min_balance=min_balance
    def withdraw_money(self,amount):
        amount=float(amount)
        if self.balance-amount>=self.min_balance:
            super().reduce_balance(amount)
        else:
            print("\n"f"your balance cannot be under {self.min_balance}")

        

    
