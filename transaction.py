import mysql.connector
import prettytable
from database import accessing_db

class trasactions:
    def __init__(self) -> None:
        mysql=accessing_db()
        mycursor=mysql.cursor()
        mycursor.execute("show tables")
        print(prettytable.from_db_cursor(mycursor))
        
        self.ac_type=input("Select Table :- ")
        self.acno=int(input("Enter your account number :-"))
        
    def balance(self):
        mysql=accessing_db()
        mycursor=mysql.cursor()
        mycursor.execute('select balance from {0} where acno ={1}'.format(self.ac_type, self.acno))
        random=mycursor.fetchone()
        print('Balance :', list(random))
        return random

    def transaction(self):
        mysql=accessing_db()
        mycursor=mysql.cursor()
        mycursor.execute('select balance from {0} where acno ={1}'.format(self.ac_type, self.acno))
        random=mycursor.fetchone()
        A=list(random)
        # check money and then transfer money
        #for that you neet to think
        print("Fill trasaction account details")
        amount=int(input("Enter amount :- "))
        credits_ac=int(input("Enter customer acount number :- "))
        type_ac=input("Enter Bank account type :- ")
        mycursor.execute('select balance from {0} where acno ={1}'.format(type_ac, credits_ac))
        credits_balence=mycursor.fetchone()
        credits_balence=list(credits_balence)
        if A[0]<amount:
            print("did not have enough funds to transfer")
        else:
            debit=A[0]-amount
            mycursor.execute('update {0} set balance = {1} where acno = {2}'.format(self.ac_type, debit, self.acno))
            credits=credits_balence[0]+amount
            mycursor.execute('update {0} set balance = {1} where acno = {2}'.format(type_ac, credits, credits_ac))
            mycursor.execute('select balance from {0} where acno ={1}'.format(self.ac_type, self.acno))
            debit_amount=mycursor.fetchone()
            mycursor.execute('select balance from {0} where acno ={1}'.format(type_ac, credits_ac))
        
            print("debited amount is : ", amount)
            print("your balance is :", list(debit_amount))
            print("""To credited {} Rs. {}""".format(credits_ac, amount))



