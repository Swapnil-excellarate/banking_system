from random import choice
import mysql.connector
from datetime import time, date, datetime
import prettytable
from database import *
from util import search_account

class loan:
    
    def path_for_loan(self):
        mysql=accessing_db()
        mycursor=mysql.cursor()
        while True:
            print("""
            1. Check your bank details 
            2. Loan approval
            3. back
            """)
            choice=int(input("Enter choise :- "))
            if choice==1:
                print("""
                1. current account 
                2. saving account 
                3. salary account
                """)

                choice=int(input("Select account type :- "))
                if choice==1:
                    search_account('current_account')

                elif choice==2:
                    search_account('savings_account')

                elif choice==3:
                    search_account('salary_account')
                else:
                    print('wrong input')
                    continue

            elif choice==2:
                pass 

            elif choice==3:
                break

