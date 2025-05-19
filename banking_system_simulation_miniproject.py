import random
class account:
    def __init__(self,id , holder_name):
        self.id=id
        self.holder_name=holder_name
        self._balance=0
    
    def check_balance(self):
        print(f"balance :{self._balance}")

    def deposit(self,amount):
        self._balance+=amount
        print(f"deposite sucessful . update balance : {self._balance}")

    def withdraw(self,amount):
        if self._balance<amount:
            print(f"your balance low {self._balance}")
        else:
            self._balance-=amount
            print(f"withdraw sucessful . update balance : {self._balance}")
class banK:
    def __init__(self,name,city):
        self.name=name
        self.city=city
        self.__account={}

    def create_account(self,id,holder_name,type):
        if type=="savings":
            new_account=savings_account(id,holder_name)
        elif type=="current":
            new_account=current_acount(id,holder_name)
        self.__account[id]=new_account
        return new_account
   
    def get_account(self,id):
        if id in self.__account:
            account= self.__account[id]
            print(f"\naccount number is : {account.id}\nholder name: {account.holder_name}")
            account.check_balance()
            return account
        else:
            print("account not found ")
            exit()
            return None
                  
class savings_account(account):
    def deposit(self,amount):
        self._balance+=amount
        interest_rate=0.0002
        interest=self._balance*interest_rate
        self._balance+=interest
        print(f"interst:{interest}")
        print(f"deposite sucessful . update balance : {self._balance}")   

class current_acount(account):  
    def withdraw(self, amount):
        over_draft=1000
        if self._balance+over_draft<amount:
            print(f"your limit upto {self._balance+over_draft}")
        else:
            self._balance-=amount
            print(f"withdraw sucessful . update balance : {self._balance}")


def choice_(account):
    while True:
        print("1. deposite ")
        print("2. withdraw ")
        print("3. check balance")
        print("4. exit....")
        choice=int(input("enter the your choice "))
        if choice==1:
            deposite(account)
        elif choice==2:
            withdrawn(account)
        elif choice==3:
            account.check_balance()
        elif choice==4:
            print("Thank you 😊")
            break
        else :
            print("choice correct option ")

def deposite(account):
    amount=float(input("enter the amount to deposite "))
    account.deposit(amount)
    

def withdrawn(account):
    amount=float(input("enter the amount you want to withdraw "))
    account.withdraw(amount)

def bank_account():
    print("1. savings account ")
    print("2. current account ")
    print("3. exiting.....")
    account_type=int(input("enter your choice "))

    if account_type==1:             
        id = random.randint(1000000,10000000)
        name=input("enter your name ")
        s1=dkt.create_account(id,name,"savings")
        
        print(f"Your account number  is {id}")
        print("successfully savings account created\nyou have a no overfdraft to withdrawn")
        choice_(s1)

                
    elif account_type==2:
        id = random.randint(100000,1000000)
        name=input("enter your name ")
        c1=dkt.create_account(id,name,"current")
        print(f"Your account number  is {id}")
        print("successfully current account created \nyou have upto 1000rs overfdraft to withdrawn")
        choice_(c1)
        
    elif account_type==3:
        print("Thank you for using our banking system .....")
        exit
                
    else:
        print("please choose correct choice ")
    

dkt=banK("DARSHAN NATIONAL BANK ","kudur")
print("welcome to darshan national bank , kudur ".upper())
while True:
    print("1. create a bank account \n2. login account \n3.exiting..... ")
    choice=int(input("enter your choice "))
    if choice==1:
        bank_account()
    elif choice==2:
            id=int(input("enter your account number  "))
            s1=dkt.get_account(id)
            choice_(s1)
        
    elif choice==3:
        print("thank you for using our banking system")
        break
    else:
        print("please enter correct choice ")
    

         