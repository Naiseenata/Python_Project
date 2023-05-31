
import random
import maskpass
class banking_system:
    def __init__(self,acc_no,name,phone_number,pin,balance):
        self.acc_no=acc_no
        self.name=name
        self.phone_number=phone_number
        self.pin=pin
        self.balance=balance

    def deposit(self,amount):
            self.balance = self.balance+amount
            print("Rs.",amount," credted to your A/C\n your current balance is Rs.",self.balance)
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance=self.balance-amount
            print("Rs.", amount, "debited from your A/C\n your current balance is  Rs.", self.balance)
    def check_balance(self):
         print("account number:",self.acc_no,"\nname:",self.name,"\ncurrent balance:",self.balance)


    def close_account(self):
        self.balance=0
        print("!!!account closed sucessfully!!!")


account_holders_details=[]
def create_account():
    while True:
        name=input("enter your name:")
        phone_number=(input("enter your mobile number:"))
        pin = maskpass.askpass(prompt="enter your 4 digit pin:", mask='*')
        balance=int(input("enter starting balance:"))
        acc_no = random.randrange(1000000000, 9999999999)
        account=banking_system(acc_no,name,phone_number,pin,balance)
        account_holders_details.append(account)
        print("\n!!!account created successfully!!!")
        print("account number:",account.acc_no, "\nname:",
              account.name,"\nphone number:",account.phone_number,"\npin:",account.pin,
              "\ncurrent balance:", account.balance)
        break


def login():
    acc_no=int(input("enter your account number:"))
    pin = maskpass.askpass(prompt="enter your 4 digit pin:", mask='*')
    for account in account_holders_details:
        if account.acc_no==acc_no:
              print("!!!welcome to federal bank!!!",account.name)
              while True:
                  print("1.deposit\n2.withdraw\n3.check balance\n4.close account\n5.log out")
                  choice=input("enter your choice:")
                  if choice=='1':
                      amount=float(input("enter the amount:"))
                      account.deposit(amount)
                  elif choice=='2':
                      amount = float(input("enter the amount:"))
                      account.withdraw(amount)
                  elif choice=='3':
                      account.check_balance()
                  elif choice=='4':
                      account.close_account()
                      account_holders_details.remove(account)
                      break
                  elif choice=='5':
                      print("successfully logged out")
                      break

    else:

       print("???invalid account number???")


     #main
print("welcome to federal bank")
while True:
       print ("1. login\n2. create account\n3.exit")
       choice=input("enter your choice:")
       if choice=='1':
          login()
       elif choice=='2':
            create_account()
       elif choice=='3':
           print("Thank you")
           break



































