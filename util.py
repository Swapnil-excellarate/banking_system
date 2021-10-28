from database import accessing_db
import prettytable
from transaction import * 
class customer:
    #auto increament customer id
    customer_id = 1130
    
    def __init__(self):
        customer.customer_id += 1
        self.customer_id = customer.customer_id

    def create_account(self):
        mysql=accessing_db()
        mycursor=mysql.cursor()
        mycursor.execute("use bankDB")
        mycursor.execute("show tables")
        tables=mycursor
        print(prettytable.from_db_cursor(tables))

        
        self.name=input("Enter Full Name :- ")
        self.add=input("Address :- ")
        self.phno=int(input("your phone number :- "))
        self.email=input("Email :- ")
        self.aadhar=int(input("Enter your aadhar number :-"))
        print("""
        -*-*-*-*-Here is the list of type of account-*-*-*-*- 
            1. Saving Account
            2. Current Accout
            3. Salary Account
        """)
        self.type_of_ac=int(input("Choose what type of account you want :- "))
        
        if self.type_of_ac==1:
            attribute='Saving Account'
        elif self.type_of_ac==2:
            attribute='Current Accout'
        elif self.type_of_ac==3:
            attribute='Salary Account'
        else:
            print('Wrong option selected try again')
        
        self.status=input("Status :- ")
        self.balence=int(input("Enter initial deposit (should be 1000 RS) :- "))
        self.branch=input(" At which branch you want to open your account :-")


        #<-- updated code -->>
        mycursor.execute(f"""INSERT INTO master(name, address, phone_no, email, aadhar_no, acc_type, status, balance, branch)
                VALUES ("{self.name}","{self.add}",{self.phno},"{self.email}",{self.aadhar}, "{attribute}", "{self.status}", {self.balence}, "{self.branch}")""")
        mysql.commit()
        print("""
            Data inserted successfully
            your Details are
            Name ={}
            Address = {}
            Aadhar = {}
            Initial balance = {}
        """.format(self.name, self.add, self.aadhar, self.balence))

        mycursor.execute('select acno from master')
        acount_number=mycursor.fetchall()
        acount_number=list(max(acount_number))
        print("your account number is ", acount_number)
        if self.type_of_ac==1:
            acno=int(input("Please confirm your account number :- "))
            #mycursor.execute('alter table Savings_account add foreign key(acno) references master(acno)')
            mycursor.execute('insert into Savings_account(initial_amount, acno) values({}, {})'.format(self.balence, acno))
            mysql.commit()
        elif self.type_of_ac==2:
            acno=int(input("Please confirm your account number :- "))
            #mycursor.execute('alter table Savings_account add foreign key(acno) references master(acno)')
            mycursor.execute('insert into Current_account(initial_amount, acno) values({}, {})'.format(self.balence, acno))
            mysql.commit()
        elif self.type_of_ac==3:
            acno=int(input("Please confirm your account number :- "))
            #mycursor.execute('alter table Savings_account add foreign key(acno) references master(acno)')
            mycursor.execute('insert into Salary_account(initial_amount, acno) values({}, {})'.format(self.balence, acno))
            mysql.commit()        
        
        else:
            print("some error occure")
                
        #<--end of updated code-->

        
        # if self.type_of_ac=='saving':
        #    mycursor.execute(f"""INSERT INTO savings_account(name, address, phone_no, email, aadhar_no, acc_type, status, balance, branch)
        #        VALUES ("{self.name}","{self.add}",{self.phno},"{self.email}",{self.aadhar}, "{self.type_of_ac}", "{self.status}", {self.balence}, "{self.branch}")""")
        #     print("""Data inserted successfully
        #     your Details are 
        #     Name= {}
        #     Address = {}
        #     Aadhar = {}
        #     Initial Balence = {}""".format(self.name, self.add, self.aadhar, self.balence))            
        #     mysql.commit()
        # elif self.type_of_ac=='salary':
        #     mycursor.execute(f"""INSERT INTO salary_account(name, address, phone_no, email, aadhar_no, acc_type, status, balance, branch)
        #         VALUES ("{self.name}","{self.add}",{self.phno},"{self.email}",{self.aadhar}, "{self.type_of_ac}", "{self.status}", {self.balence}, "{self.branch}")""")
        #     print("""Data inserted successfully
        #     your Details are 
        #     Name= {}
        #     Address = {}
        #     Aadhar = {}
        #     Initial Balence = {}""".format(self.name, self.add, self.aadhar, self.balence))
        #     mysql.commit()

        # elif self.type_of_ac=='current':
        #     mycursor.execute(f"""INSERT INTO current_account(name, address, phone_no, email, aadhar_no, acc_type, status, balance, branch)
        #         VALUES ("{self.name}","{self.add}",{self.phno},"{self.email}",{self.aadhar}, "{self.type_of_ac}", "{self.status}", {self.balence}, "{self.branch}")""")
        #     print("""Data inserted successfully
        #     your Details are 
        #     Name= {}
        #     Address = {}
        #     Aadhar = {}
        #     Initial Balence = {}""".format(self.name, self.add, self.aadhar, self.balence))
        #     mysql.commit()
        # else:
        #     print("Not inserted")

    def update_account(self):
        mysql=accessing_db()
        mycursor=mysql.cursor()
        mycursor.execute("use bankDB")
        mycursor.execute("show tables")
        tables=mycursor
        print(prettytable.from_db_cursor(tables))

        table=input("Select table :- ")
        mycursor.execute("select * from %s"%table)

        print(prettytable.from_db_cursor(mycursor))


        acno=int(input("Enter Account Number :- "))
        name=input("Enter Your Name :- ")
        phno=int(input("Enter your phone number :- "))
        aadhar=int(input("Enter your Correct Aadhar number :- "))
        mycursor.execute(" UPDATE {0} SET phone_no = {1}, aadhar_no = {2} WHERE acno = {3} AND name = '{4}'".format(table, phno, aadhar, acno, name))
        mysql.commit()
        mycursor.execute(' use bankDB')
        mycursor.execute(' select * from %s'%table)
        print(prettytable.from_db_cursor(mycursor))

    #deposit money
    def deposit_withdraw(self):
        mysql=accessing_db()
        mycursor=mysql.cursor()
        mycursor.execute("use bankDB")
        mycursor.execute("show tables")
        tables=mycursor
        print(prettytable.from_db_cursor(tables))
        
        table=input("select tables :- ")
        mycursor.execute("select * from %s"%table)
        print(prettytable.from_db_cursor(mycursor))
        
        while True:
            
            print("""
                1. For deposit cash 
                2. For withdraw cash
                3. back
            """)
            option=int(input("select option :- "))
        
            if option==1:
                acno=int(input("Enter your Account Number :- "))
                mycursor.execute(" select balance from {0} WHERE acno= {1}".format(table, acno))
                
                random= mycursor.fetchone()
                lst=list(random)
                print('This is your balence', lst)
                deposit=int(input("Enter deposit amount :- "))

                total_balence=lst[0]+deposit
 
                print('Deposit amount is', deposit)
                print('Balence is', total_balence)
                
                mycursor.execute(" UPDATE {0} SET balance = {1} WHERE acno = {2}".format(table,total_balence, acno))
                mysql.commit()
                mycursor.execute(' use bankDB')
                mycursor.execute(' select * from {0} where acno = {1}'.format(table, acno))
                mysql.commit()
                print(prettytable.from_db_cursor(mycursor))
            
            elif option==2:
                acno=int(input("Enter bank Account Number :- "))
                mycursor.execute(" select balance from {0} WHERE acno= {1}".format(table, acno))
                
                random= mycursor.fetchone()
                lst=list(random)
                print('Your balence', lst)
                withdraw=int(input("Enter withdraw amount :- "))

                total_balence=lst[0]-withdraw
                
                print('Deposit amount is', withdraw)
                print('Balence is', total_balence)
                
                mycursor.execute(" UPDATE {0} SET balance = {1} WHERE acno = {2}".format(table,total_balence, acno))
                mysql.commit()
                mycursor.execute(' use bankDB')
                mycursor.execute(' select * from {0} where acno = {1}'.format(table, acno))
                print(prettytable.from_db_cursor(mycursor))
            
            # elif option==3:
            #     t=trasactions()
            #     t.balance()

            elif option==3:
                break
            else:
                print("Wrong choise")
                continue     
            
def search_account(table_name):
    mysql=accessing_db()
    mycursor=mysql.cursor()
    while True:
        print('''
        --------Search By--------
        1. Account Number.
        2. Name.
        3. Aadhar Number.
        4. Phone Number.
        ''')
        choice=int(input('Enter The Number:- '))
        if choice == 1:
            attribute='acno'
            account_no = int(input('Enter Account Number:- '))
            mycursor.execute(f'''
            SELECT * FROM {table_name}
            WHERE {attribute} = {account_no}
            ''')
            print(prettytable.from_db_cursor(mycursor))
            return account_no,attribute
        elif choice == 2:
            attribute='name'
            name = input('Enter Name:- ')
            mycursor.execute(f'''
                SELECT * FROM {table_name}
                WHERE {attribute} = '{name}'
                ''')
            print(prettytable.from_db_cursor(mycursor))
            return name,attribute
        elif choice == 3:
            attribute='aadhar_no'
            aadhar_no = int(input('Enter Aadhar Number:- '))
            mycursor.execute(f'''
            SELECT * FROM {table_name}
            WHERE {attribute} = {aadhar_no}
            ''')
            print(prettytable.from_db_cursor(mycursor))
            return aadhar_no,attribute
        elif choice == 4:
            attribute='phone_no'
            phone_no = int(input('Enter phone number:- '))
            mycursor.execute(f'''
                SELECT * FROM {table_name}
                WHERE {attribute} = {phone_no}
                ''')
            print(prettytable.from_db_cursor(mycursor))
            return phone_no,attribute

