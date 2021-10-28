import mysql.connector as sql

def accessing_db():
    #x=input("Enter Username :")
    #y=input("Enter Password :")
    mysql= sql.connect(host='localhost', user="root", password="1234")
    creating_tables(mysql)
    print("connection is successfully")
    return mysql


def creating_tables(mysql):
    db=mysql.cursor()

    db.execute("create database if not exists bankDB")
    db.execute("use bankDB")

    
    # db.execute('create table if not exists savings_account(acno int not null auto_increment primary key, name char(30), address varchar(100), phone_no int not null unique, email varchar(80) unique, aadhar_no int not null unique, acc_type varchar(10), status varchar(10), balance int not null, branch varchar(20) not null)')
    # db.execute('create table if not exists salary_account(acno int not null auto_increment primary key, name char(30), address varchar(100), phone_no int not null unique, email varchar(80) unique, aadhar_no int not null unique, acc_type varchar(10), status varchar(10), balance int not null, branch varchar(20) not null)')
    # db.execute('create table if not exists current_account(acno int not null auto_increment primary key, name char(30), address varchar(100), phone_no int not null unique, email varchar(80) unique, aadhar_no int not null unique, acc_type varchar(10), status varchar(10), balance int not null, branch varchar(20) not null)')
    
    ##----updated code--------
    
    db.execute('create table if not exists master(acno int not null auto_increment primary key, name char(30), address varchar(100), phone_no int not null unique, email varchar(80) unique, aadhar_no int not null unique, acc_type varchar(50), status varchar(10), balance int not null, branch varchar(20) not null)')
    
    db.execute('create table if not exists Savings_account(transaction_id int not null auto_increment primary key, initial_amount int not null, Deposit_amount int DEFAULT NULL, withdrawal_amount int DEFAULT NULL, amount int DEFAULT NULL, acno int not null)')
    db.execute('create table if not exists Salary_account(transaction_id int not null auto_increment primary key, initial_amount int not null, Deposit_amount int, withdrawal_amount int, amount int, acno int not null)')
    db.execute('create table if not exists Current_account(transaction_id int not null auto_increment primary key, initial_amount int not null, Deposit_amount int, withdrawal_amount int, amount int, acno int not null)')

    db.execute('alter table Savings_account add foreign key(acno) references master(acno)')
    db.execute('alter table Salary_account add foreign key(acno) references master(acno)')
    db.execute('alter table Current_account add foreign key(acno) references master(acno)')
