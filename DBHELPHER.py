import mysql.connector as connector
import datetime as date
import logging

class DBHelpher :

    dates1 = date.datetime.now()

    Bank_name = "Rev Bank "
    conres = []
    def __init__(self):

        self.con = connector.connect(host='localhost',
                                     user='root',
                                     password='123456',
                                     database='banking')

    def create(self,name ,phone ,DOB , Address, opening_bal,password ):
        query = "insert into customers(name,phone,DOB,Address,Balance,password)values('{}',{},'{}','{}',{},'{}')".format(name,phone,DOB,Address,opening_bal,password)
        # print(query)
        curr = self.con.cursor()
        curr.execute(query)
        self.con.commit()
        print("Account created  successfully at  " , self.dates1)
        self.cus_list = [name , password]
    def find_customer(self,account_no):
        query = "select * from customers where account_no={}".format(account_no)
        cur = self.con.cursor()
        cur.execute(query)
        res = cur.fetchall()
        if res :
         for row in res:
            print("Account number  : ", row[0])
            print("name  : ", row[1])
            print("phone number  : ", row[2])
            print("DOB  : ", row[3])
            print("Address  : ", row[4])
            print(" balance   : ", row[5])
            print()
            print()
        else:
            print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT ")
    def delete_customer(self,account_no):
        q = "select * from customers where account_no = {}".format(account_no)
        curr = self.con.cursor()
        curr.execute(q)
        res = curr.fetchall()
        if res :
          query = "delete from customers where account_no = {}".format(account_no)
          cur = self.con.cursor()
          cur.execute(query)
          res = cur.fetchone()
          self.con.commit()
          print("Your Account is deleted Successfully at  " , self.dates1)
          print()
        else:
            print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT")

    def update_customer(self,account_no):
        q = "select * from customers where account_no = {}".format(account_no)
        curr = self.con.cursor()
        curr.execute(q)
        res = curr.fetchall()
        if res  :
            newName = input("enter newname : ").capitalize()
            while True:
                newphone = int(input('enter your phone number : '))
                if len(str(newphone)) > 10 or len(str(newphone)) < 10:
                    print("Invalid phone number ! please enter 10 digit only ")
                else:
                    break
            newaddress = input("enter newaddress : ").capitalize()
            query = "update customers set name = '{}' , phone = {} , Address = '{}' where account_no = {} ".format(
                newName, newphone, newaddress, account_no)
            cur = self.con.cursor()
            cur.execute(query)
            self.con.commit()
            print("Account details updated successfully  at ", self.dates1)
        else:
            print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT")





    def deposit(self, acc_no):
        q = 'select Balance from customers where account_no = {}'.format(acc_no)
        curr = self.con.cursor()
        curr.execute(q)
        res = curr.fetchone()
        if res :
            amount = int(input("please enter amount you want to enter : "))
            if amount <= 0 :
                print("please deposit more than 0 ")
            elif amount >= 15000 :
                print("deposit limit exceeded ! Deposit between 0 to 15000 ")
            else :
              total = int(res[0]) + amount
              query = 'update customers set Balance = {}  where account_no = {}'.format(total , acc_no)
              curr = self.con.cursor()
              curr.execute(query)
              self.con.commit()
              print("Amount deposited successfully  "  , " at " , self.dates1)
        else :
            print("DEPOSIT FAILED  ! PLEASE CHECK YOUR CREDENTIALS  ")

    def withdrawn(self,acc_no):
        with_lim = 15001
        q = 'select Balance from customers where account_no = {}'.format(acc_no)
        curr = self.con.cursor()
        curr.execute(q)
        res = curr.fetchone()
        if res :
          total = 0
          amount = int(input("enter amount you want to Withdrawn : "))
          if int(res[0]) <= amount:
            print("you dont have sufficient balance ")
          elif int(res[0]) >= with_lim:
              print("WITHDRAWN LIMIT EXCEEDED ! PLEASE WITHDRAWN BETWEEN 1 TO 15000 ")
          else :
            total = int(res[0]) - amount
            query = 'update customers set Balance = {}  where account_no = {}'.format(total, acc_no)
            curr = self.con.cursor()
            curr.execute(query)
            self.con.commit()
            print("Amount withdrawn  successfully " ,  "at" , self.dates1)
        else:
            print("WITHDRAWN FAILED ! PLEASE ENTER CORRECT ACCOUNT NO ")
    def checkuser(self,account_no):
        q = "select name from customers where account_no = {}".format(account_no)
        cur = self.con.cursor()
        cur.execute(q)
        res = cur.fetchone()
        conres = list(res)
        if not res :
            print("INCORRECT ACCOUNT NUMBER ! CANT PERFORM ANY TRANSACTIONS ")
            # print("WELCOME BACK  -- " , res[0])

        else :
            print("WELCOME BACK  -- ", res[0])
            # print("INCORRECT ACCOUNT NUMBER ! CANT PERFORM ANY TRANSACTIONS ")


