from loan import loan
from transaction import trasactions
from util import customer
from datetime import time, date, datetime

today=date.today()
d2=today.strftime("%A,%B %d, %Y")
t = datetime.time(datetime.now())
print("Todays Date:-\t", d2,"Time:-\t",t)

print("WELCOME TO BANK")

def main():

    while True:
        c1=customer()
        print("""
        1. To create account
        2. If you want to update your account
        3. Disposit your cash
        4. check balence 
        5. Transaction
        7. cancel
        """)

        choice=int(input("Enter your choice :- "))
        if choice==1:
            c1.create_account()

        elif choice==2:
            c1.update_account()

        elif choice==3:
            c1.deposit_withdraw()

        elif choice==4:
            t1=trasactions()
            t1.balance()

        elif choice==5:
            t1=trasactions()
            t1.transaction()
        
        elif choice==6:
            l1=loan()
            l1.path_for_loan()

        elif choice==7:
            print("Thank you for banking with us")
            break

        else:
            print("Wrong input, Try one more time")
            continue
            
if __name__=='__main__':
    

    main() 

