class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
        print("Account Holder:",self.name)

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("Deposit Successful\n")
        else:
            print("Invalid amount\n")

    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print("Withdrawl Successful\n")

    def show_balance(self):
        print("Current Balance:",self.__balance)

c1=BankAccount("Ananya",10000)
c1.deposit(2000)
c1.withdraw(3000)
c1.withdraw(15000)
c1.show_balance()
