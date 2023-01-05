# NotaBanc Bank

import mysql.connector   #Sql connector
from tabulate import tabulate #Table Module

def New_Account():    #Creating a new Account
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="2611",database="bank123",
    auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    acno=int(input("enter account no.:"))
    Name=input("enter account name:")
    amt=int(input("enter opening balance:"))
    tel=int(input("enter telephone no.:"))
    query="insert into bank(Accno,AccName,Telno,Balanceamt) values(%s,%s,%s,%s)"
    record=(acno,Name,tel,amt)
    mycursor.execute(query,record)
    mydb.commit()
    mycursor.execute("select * from bank where AccNo={}".format(acno))
    result=mycursor.fetchall()
    L=[]
    for k in result:
                L.append(k)
    print(tabulate(L,headers=['AccNo','AccName','Telno','Balanceamt'],tablefmt='fancy_grid'))
    print("record has been saved")

def Search_Accno():    #Searching a Account in the database
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="2611",database="bank123")
    mycursor=mydb.cursor()
    acno=int(input("enter account no.:"))
    L=[]
    mycursor.execute("select * from bank where AccNo={}".format(acno))
    result=mycursor.fetchall()
    for k in result:
                L.append(k)
    print(tabulate(L,headers=['AccNo','AccName','Telno','Balanceamt'],tablefmt='fancy_grid'))
        

def Deposit():    #Deposit Amount 
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="2611",database="bank123",
    auth_plugin='mysql_native_password')
    mycursor=mydb.cursor()
    acno=int(input("enter account no. to deposit amt:"))
    mycursor.execute("select * from bank where AccNo={}".format(acno))
    result=mycursor.fetchall()
    T=[]
    for k in result:
                T.append(k)
    print(tabulate(T,headers=['AccNo','AccName','Telno','Balanceamt'],tablefmt='fancy_grid'))
    amt=int(input("enter amt to be deposited:"))
    L=[]
    mycursor.execute("update bank set Balanceamt=Balanceamt+{} where AccNo={}".format(amt,acno))
    mydb.commit()
    mycursor.execute("select * from bank where AccNo={}".format(acno))
    result=mycursor.fetchall()
    for i in result:
                L.append(i)
    print(tabulate(L,headers=['AccNo','AccName','Telno','Balanceamt'],tablefmt='fancy_grid'))

def Withdrawal():    #Amount Withdrawal
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="2611",database="bank123")
    mycursor=mydb.cursor()
    acno=int(input("enter account no. for withdrawal"))
    mycursor.execute("select * from bank where AccNo={}".format(acno))
    result=mycursor.fetchall()
    for k in result:
        Bamt=k[3]
    print("balance amt:",Bamt)
    T=[]
    for k in result:
                T.append(k)
    print(tabulate(T,headers=['AccNo','AccName','Telno','Balanceamt'],tablefmt='fancy_grid'))
    amt=int(input("enter amt to be withdrawn:"))
    if amt<Bamt:    #Check if balance amt< withdrawal amt
        mycursor.execute("update bank set Balanceamt=Balanceamt-{} where AccNo={}".format(amt,acno))
        mydb.commit()
        mycursor.execute("select * from bank where AccNo={}".format(acno))
        result=mycursor.fetchall()
        L=[]
        for i in result:
                L.append(i)
        print(tabulate(L,headers=['AccNo','AccName','Telno','Balanceamt'],tablefmt='fancy_grid'))
    else:
        print("Cannot withdraw amt...Insufficient Balance")

def Transactions():    #Required transactions
    while True:
        print("================================================")
        print("1:Deposit")
        print("2:Withdraw")
        print("3:Back to main menu")
        print("================================================")
        choice=int(input("enter your choice:"))
        if choice==1:
            Deposit()
        elif choice==2:
            Withdrawal()
        elif choice==3:
            return
        else:
            print("invalid choice...try again")


def UpdateAccName(): #Update Customer Account Name
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="2611",database="bank123")
    mycursor=mydb.cursor()
    acno=int(input("enter the account no. to be modified:"))
    mycursor.execute("select * from bank where AccNo={}".format(acno))
    result=mycursor.fetchall()
    T=[]
    for k in result:
                T.append(k)
    print(tabulate(T,headers=['AccNo','AccName','Telno','Balanceamt'],tablefmt='fancy_grid'))
    m=input("Do you want to change AccName.(y/n):")
    if m in "Yy":
        newaccname=input("Enter new Account Name: ")
        query="update bank set AccName={} where AccNo={}".format(newaccname,acno)
        mycursor.execute(query)
        mydb.commit()
        mycursor.execute("select * from bank where AccNo={}".format(acno))
        result=mycursor.fetchall()
        L=[]
        for i in result:
                L.append(i)
        print(tabulate(L,headers=['AccNo','AccName','Telno','Balanceamt'],tablefmt='fancy_grid'))
    else:
        print("you may try again later")
        return

def UpdateTelNo(): #Update Customer's Telno
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="2611",database="bank123")
    mycursor=mydb.cursor()
    acno=int(input("enter the account no. to be modified:"))
    mycursor.execute("select * from bank where AccNo={}".format(acno))
    result=mycursor.fetchall()
    T=[]
    for k in result:
                T.append(k)
    print(tabulate(T,headers=['AccNo','AccName','Telno','Balanceamt'],tablefmt='fancy_grid'))
    m=input("do you want to change telno.(y/n):")
    if m in "Yy":
        newtelno=int(input("enter new telephone no:"))
        query="update bank set Telno={} where AccNo={}".format(newtelno,acno)
        mycursor.execute(query)
        mydb.commit()
        mycursor.execute("select * from bank where AccNo={}".format(acno))
        result=mycursor.fetchall()
        L=[]
        for i in result:
                L.append(i)
        print(tabulate(L,headers=['AccNo','AccName','Telno','Balanceamt'],tablefmt='fancy_grid'))
    else:
        print("you may try again later")
        return

 
def DeleteCustomer():  #Delete Cusotmer Account
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="2611",database="bank123")
    mycursor=mydb.cursor()
    acno=int(input("enter the account no. to be deleted:"))
    mycursor.execute("select * from bank where AccNo={}".format(acno))
    result=mycursor.fetchall()
    T=[]
    for k in result:
                T.append(k)
    print(tabulate(T,headers=['AccNo','AccName','Telno','Balanceamt'],tablefmt='fancy_grid'))
    m=input("do you want to delete this customer account(y/n):")
    if m in "Yy":
        query="delete from bank where AccNo={}".format(acno)
        mycursor.execute(query)
        mydb.commit()
    else:
        print("you may try later")
        return
    mycursor.execute("select * from bank ")
    result=mycursor.fetchall()
    L=[]
    for i in result:
                L.append(i)
    print(tabulate(L,headers=['AccNo','AccName','Telno','Balanceamt'],tablefmt='fancy_grid'))


def Modify():   #Modify Details
    while True:
        print("================================================")
        print("1:Update Account Name:")
        print("2:Update telephone no:")
        print("3:Back to main menu")
        choice=int(input("enter your choice:"))
        if choice==1:
            UpdateAccName()
        elif choice==2:
            UpdateTelNo()
        elif choice==3:
            return
        else:
            print("invalid choice...try again")



while True:   #Main Menu
    
    print("============================================")
    print("$$$$$$$$ NOTABANC BANK $$$$$$$$")
    print(                                 )
    print("$$$$$$$$$$ MAIN MENU $$$$$$$$$$")
    print("1: Open Account")
    print("2: Search for customer")
    print("3: Transactions")
    print("4: Modify customer details")
    print("5: Cancel acoount")
    print("6: Show Details of all Customers")
    print("7: Exit")
    print("============================================")
    choice=int(input("enter your choice:"))
    if choice==1:
        New_Account()
            
    elif choice==2:
        Search_Accno()
            
    elif choice==3:
        Transactions()
    elif choice==4:
        Modify()
            
    elif choice==5:
        DeleteCustomer()
    elif choice==6:  #Display data from database
        L=[]
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="2611",database="bank123",
        auth_plugin='mysql_native_password')
        mycursor=mydb.cursor()
        mycursor.execute("select * from bank ")
        result=mycursor.fetchall()
        for k in result:
                L.append(k)
        print(tabulate(L,headers=['AccNo','AccName','Telno','Balanceamt'],tablefmt='fancy_grid'))
    elif choice==7:
        break
    else:
        print("invalid choice...try again")



