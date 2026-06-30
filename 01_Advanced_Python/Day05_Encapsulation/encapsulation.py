# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self. __balance=balance

#     def deposit(self,amount):
#         if(amount>0):
#             self. __balance+=amount
#             print("Amount deposited Successfully")
#         else:
#             print("Invalid Input")

#     def withdraw(self,amount):
#         if(amount>0 and amount<=self.__balance):
#             self.__balance-=amount
#             print("Amount withdrawl successfully")
#         else:
#             print("Invalid Input")

#     def display_balance(self):
#         print("Holder's Current balance is",self.__balance)
    
# acc=BankAccount("Surya",20000)
# acc.deposit(500)
# acc.withdraw(1000)
# acc.display_balance()