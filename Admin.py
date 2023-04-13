
import mysql.connector as connector
import datetime as date
import logging
class Admin :

    dates1 = date.datetime.now()
    admin = 'ADMIN'
    password = 'admin12'
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     user='root',
                                     password='123456',
                                     database='banking')

    def showall_customers(self):
            query = "select * from customers"
            cur = self.con.cursor()
            cur.execute(query)
            for row in cur:
                print("Account number  : ", row[0])
                print("name  : ", row[1])
                print("phone number  : ", row[2])
                print("DOB  : ", row[3])
                print("Address  : ", row[4])
                print("balance   : ", row[5])
                print("Password   : ", row[6])
                print()
                print()

    def find_customer(self, account_no):
        query = "select * from customers where account_no={}".format(account_no)
        cur = self.con.cursor()
        cur.execute(query)
        res = cur.fetchall()
        if res:
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

    def delete_customer(self, account_no):
            q = "select * from customers where account_no = {}".format(account_no)
            curr = self.con.cursor()
            curr.execute(q)
            res = curr.fetchone()
            if res :
             query = "delete from customers where account_no = {}".format(account_no)
             cur = self.con.cursor()
             cur.execute(query)
             self.con.commit()
             print("Customer Deleted successfully at  ", self.dates1)
             print()
            else:
                print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT")

    def update_customer(self, account_no):
        q = "select * from customers where account_no = {}".format(account_no)
        curr = self.con.cursor()
        curr.execute(q)
        res = curr.fetchall()
        if res:
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

    def deleteAllcustomers(self):
            query = "delete from customers"
            curr = self.con.cursor()
            curr.execute(query)
            self.con.commit()
            print('All customers deleted at ', self.dates1)
    def checkadmin(self,username , password):
        usrname = 'admin'
        passwrd = 'admin@12'
        if username == usrname and password == passwrd :
            print("WELCOME BACK ADMIN ")
        else:
            print("INCORRECT ADMIN USERNAME OR PASSWORD ! Access DENEID YOU CANT PERFORM BANKING OPERATION ")
