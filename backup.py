# # # from DBHELPHER import DBHelpher
# # # from Admin import Admin
# # # from logging import exception, raiseExceptions
# # # import datetime as date
# # #
# # # def main() :
# # #       spl_char = ['.', '#''!', '@', '%', '^', '&', '/', '=', '?', '-', '$']
# # #       print()
# # #       print("  WELCOME TO  ", DBHelpher.Bank_name)
# # #       helpher = DBHelpher()
# # #       admin = Admin()
# # #       print()
# # #
# # #       inp = input("please enter ADMIN or USER :  ")
# # #       if inp == 'user' :
# # #
# # #         usr = input("please enter 1 for NEW CUSTOMER  or 2 for EXISTING CUSTOMER ")
# # #         if usr == '1':
# # #
# # #           while True:
# # #
# # #             print()
# # #             print("CREATE NEW ACCOUNT  ")
# # #
# # #             try :
# # #                   while True :
# # #                     try :
# # #                         spl_char = str(['.','#''!','@','%','^','&','/','=','?','-','$'])
# # #                         name = input('please enter your name : ').capitalize()
# # #                         if spl_char in name :
# # #                             raise TypeError
# # #                         break
# # #                     except TypeError as msg :
# # #                         print("special character are not allowed like .., * % # $ @",msg )
# # #
# # #
# # #                   while True :
# # #                     phone = int(input('enter your 10 digit  phone number : '))
# # #                     if len(str(phone)) > 10 or len(str(phone)) < 10 :
# # #                       print("Invalid phone number ! please enter 10 digit only ")
# # #                     else :
# # #                         break
# # #                   while True :
# # #                       try :
# # #                         DOB = input('please enter you date of birth in DD/MM/YYYY format ')
# # #                         DOB = date.datetime.strptime(DOB,"%d/%m/%y").date()
# # #                         break
# # #                       except ValueError:
# # #                           print("Please enter Date of birth in proper format !!! DD/MM/YYYY")
# # #
# # #                   Address = input('enter your address : ').capitalize()
# # #                   while True :
# # #                      opening_bal = int(input("please enter your opening balance : "))
# # #                      if opening_bal <= 0 :
# # #                          print('opening balance cant be zero ')
# # #                      elif opening_bal >= 15000 :
# # #                          print("OPENING BALANCE CANT BE MORE THAN 15000")
# # #                      else :
# # #                          break
# # #
# # #                   while True :
# # #                       try :
# # #                         password = input('please enter password ')
# # #                         if (len(password) < 6):
# # #                            raise ValueError(" Password should contain at least 6 character ")
# # #                         if not any(char.isdigit() for char in password):
# # #                            raise ValueError("Password should atleast a number")
# # #                         if not any(char.isupper() for char in password):
# # #                            raise KeyError()
# # #                         if not any(char.islower() for char in password):
# # #                            raise KeyError
# # #                         if not any(char in spl_char for char in password):
# # #                            raise KeyError
# # #                         break
# # #                       except ValueError:
# # #                           print(
# # #                              "Password should contain atleast 1 upper case, 1 Lower Case , 1 Special Character  and Password Must Contain atleast 7 character")
# # #                       except KeyError:
# # #                            print(
# # #                             "Password should contain atleast 1 upper case, 1 Lower Case , 1 Special Character  and Password Must Contain atleast 7 character")
# # #
# # #
# # #                   helpher.create(name,phone,DOB,Address,opening_bal,password)
# # #                   break
# # #             except Exception as e :
# # #               print(e)
# # #               print("INVALID DETAILS ! TRY AGAIN")
# # #         elif usr == '2' :
# # #            while True :
# # #                print()
# # #                print("Enter 1 to display your account details  ")
# # #                print("Enter 2 to delete your account  ")
# # #                print("Enter 3 to update  your account  account ")
# # #                print("Enter 4 to deposit to an account  ")
# # #                print("Enter 5 to withdrawn from   an  account ")
# # #                print("Enter 6 to complete an transactions ")
# # #                print()
# # #                try :
# # #                 choice = int(input("enter your choice to perform operations : "))
# # #
# # #                 if choice == 1 :
# # #                     cus = int(input("please enter your account number to fetch your  information : "))
# # #                     helpher.find_customer(cus)
# # #
# # #                 elif choice == 2 :
# # #                   cus = int(input("please enter an account number to delete your account : "))
# # #                   helpher.delete_customer(cus)
# # #
# # #
# # #                 elif choice == 3 :
# # #                   cid = int(input("please enter account number to update your details "))
# # #                   helpher.update_customer(cid)
# # #
# # #
# # #                 elif choice == 4 :
# # #                   acc_no = int(input("please enter your account number to deposit "))
# # #                   helpher.deposit(acc_no)
# # #
# # #                 elif choice == 5 :
# # #                   acc_no = int(input("please enter your account number to withdrawn "))
# # #                   helpher.withdrawn(acc_no)
# # #
# # #
# # #                 elif choice == 6 :
# # #                   print('Thank you for using Rev bank ! Welcome back ')
# # #                   break
# # #                 else :
# # #                   print("Invalid input ! try again  ")
# # #                except Exception as e :
# # #                 print(e)
# # #                 print('Invalid details ! Try again ')
# # #
# # #       elif inp == 'admin':
# # #         while True:
# # #           username = input('please enter username : ')
# # #           password = input('pleasse enter password')
# # #           if username != admin.admin and password != admin.password:
# # #               print("please enter correct credentials ")
# # #               break
# # #           else :
# # #
# # #            while True :
# # #              print()
# # #              print("Enter 1 to display  all customers  ")
# # #              print("Enter 2 to display a specific customer  ")
# # #              print("Enter 3 to delete an  account ")
# # #              print("Enter 4 to update  an  account ")
# # #              print("Enter 5 to delete all customers ")
# # #              print("Enter 6 to complete an transactions ")
# # #              print()
# # #              try :
# # #                 choice = int(input('please enter your choice to perform operations '))
# # #
# # #                 if choice == 1:
# # #                    admin.showall_customers()
# # #                 elif choice == 2 :
# # #                    inp = int(input("please enter account number to fetch customer details : "))
# # #                    admin.find_customer(inp)
# # #                 elif choice == 3 :
# # #                    inp = int(input("please enter account number to delete customer  : "))
# # #                    admin.delete_customer(inp)
# # #                 elif choice == 4 :
# # #                    cid = int(input("please enter account number to update your details "))
# # #                    admin.update_customer(cid)
# # #                 elif choice == 5:
# # #                    admin.deleteAllcustomers()
# # #                 elif choice == 6 :
# # #                    print("Thank you admin ! see you soon ")
# # #                    break
# # #                    break
# # #                 else :
# # #                    print("Invalid input ! try again ")
# # #              except Exception as e :
# # #                print(e)
# # #                print("invalid details ! try again ")
# # #       else :
# # #           print("invalid input please enter user or admin ")
# # #
# # # if __name__ == "__main__" :
# # #     main()
# #
# # import mysql.connector as connector
# # import datetime as date
# # import logging
# #
# # class DBHelpher :
# #
# #     dates1 = date.datetime.now()
# #
# #     Bank_name = "Rev Bank "
# #     def __init__(self):
# #
# #         self.con = connector.connect(host='localhost',
# #                                      user='root',
# #                                      password='123456',
# #                                      database='banking')
# #         self.cus_list = []
# #         self.loggedin = False
# #     def create(self,name ,phone ,DOB , Address, opening_bal,password ):
# #         query = "insert into customers(name,phone,DOB,Address,Balance,password)values('{}',{},'{}','{}',{},'{}')".format(name,phone,DOB,Address,opening_bal,password)
# #         # print(query)
# #         curr = self.con.cursor()
# #         curr.execute(query)
# #         self.con.commit()
# #         print("Account created  successfully at  " , self.dates1)
# #         self.cus_list = [name , password]
# #     def find_customer(self,account_no):
# #         query = "select * from customers where account_no={}".format(account_no)
# #         cur = self.con.cursor()
# #         cur.execute(query)
# #         res = cur.fetchall()
# #         if res :
# #          for row in res:
# #             print("Account number  : ", row[0])
# #             print("name  : ", row[1])
# #             print("phone number  : ", row[2])
# #             print("DOB  : ", row[3])
# #             print("Address  : ", row[4])
# #             print(" balance   : ", row[5])
# #             print()
# #             print()
# #         else:
# #             print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT ")
# #     def delete_customer(self,account_no):
# #         q = "select * from customers where account_no = {}".format(account_no)
# #         curr = self.con.cursor()
# #         curr.execute(q)
# #         res = curr.fetchall()
# #         if res :
# #           query = "delete from customers where account_no = {}".format(account_no)
# #           cur = self.con.cursor()
# #           cur.execute(query)
# #           res = cur.fetchone()
# #           self.con.commit()
# #           print("Your Account is deleted Successfully at  " , self.dates1)
# #           print()
# #         else:
# #             print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT")
# #
# #     def update_customer(self,account_no):
# #         q = "select * from customers where account_no = {}".format(account_no)
# #         curr = self.con.cursor()
# #         curr.execute(q)
# #         res = curr.fetchall()
# #         if res  :
# #             newName = input("enter newname : ").capitalize()
# #             while True:
# #                 newphone = int(input('enter your phone number : '))
# #                 if len(str(newphone)) > 10 or len(str(newphone)) < 10:
# #                     print("Invalid phone number ! please enter 10 digit only ")
# #                 else:
# #                     break
# #             newaddress = input("enter newaddress : ").capitalize()
# #             query = "update customers set name = '{}' , phone = {} , Address = '{}' where account_no = {} ".format(
# #                 newName, newphone, newaddress, account_no)
# #             cur = self.con.cursor()
# #             cur.execute(query)
# #             self.con.commit()
# #             print("Account details updated successfully  at ", self.dates1)
# #         else:
# #             print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT")
# #
# #
# #
# #
# #
# #     def deposit(self, acc_no):
# #         q = 'select Balance from customers where account_no = {}'.format(acc_no)
# #         curr = self.con.cursor()
# #         curr.execute(q)
# #         res = curr.fetchone()
# #         if res :
# #             amount = int(input("please enter amount you want to enter : "))
# #             if amount <= 0 :
# #                 print("please deposit more than 0 ")
# #             elif amount >= 15000 :
# #                 print("deposit limit exceeded ! Deposit between 0 to 15000 ")
# #             else :
# #               total = int(res[0]) + amount
# #               query = 'update customers set Balance = {}  where account_no = {}'.format(total , acc_no)
# #               curr = self.con.cursor()
# #               curr.execute(query)
# #               self.con.commit()
# #               print("Amount deposited successfully  "  , " at " , self.dates1)
# #         else :
# #             print("DEPOSIT FAILED  ! PLEASE CHECK YOUR CREDENTIALS  ")
# #
# #     def withdrawn(self,acc_no):
# #         with_lim = 15001
# #         q = 'select Balance from customers where account_no = {}'.format(acc_no)
# #         curr = self.con.cursor()
# #         curr.execute(q)
# #         res = curr.fetchone()
# #         if res :
# #           total = 0
# #           amount = int(input("enter amount you want to deposit : "))
# #           if int(res[0]) <= amount:
# #             print("you dont have sufficient balance ")
# #           elif int(res[0]) >= with_lim:
# #               print("WITHDRAWN LIMIT EXCEEDED ! PLEASE WITHDRAWN BETWEEN 1 TO 15000 ")
# #           else :
# #             total = int(res[0]) - amount
# #             query = 'update customers set Balance = {}  where account_no = {}'.format(total, acc_no)
# #             curr = self.con.cursor()
# #             curr.execute(query)
# #             self.con.commit()
# #             print("Amount withdrawn  successfully " ,  "at" , self.dates1)
# #         else:
# #             print("WITHDRAWN FAILED ! PLEASE ENTER CORRECT ACCOUNT NO ")
# #
#
# import mysql.connector as connector
# import datetime as date
# import logging
# class Admin :
#
#     dates1 = date.datetime.now()
#     admin = 'ADMIN'
#     password = 'admin12'
#     def __init__(self):
#         self.con = connector.connect(host='localhost',
#                                      user='root',
#                                      password='123456',
#                                      database='banking')
#
#     def showall_customers(self):
#             query = "select * from customers"
#             cur = self.con.cursor()
#             cur.execute(query)
#             for row in cur:
#                 print("Account number  : ", row[0])
#                 print("name  : ", row[1])
#                 print("phone number  : ", row[2])
#                 print("DOB  : ", row[3])
#                 print("Address  : ", row[4])
#                 print("balance   : ", row[5])
#                 print("Password   : ", row[6])
#                 print()
#                 print()
#
#     def find_customer(self, account_no):
#         query = "select * from customers where account_no={}".format(account_no)
#         cur = self.con.cursor()
#         cur.execute(query)
#         res = cur.fetchall()
#         if res:
#             for row in res:
#                 print("Account number  : ", row[0])
#                 print("name  : ", row[1])
#                 print("phone number  : ", row[2])
#                 print("DOB  : ", row[3])
#                 print("Address  : ", row[4])
#                 print(" balance   : ", row[5])
#                 print()
#                 print()
#         else:
#             print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT ")
#
#     def delete_customer(self, account_no):
#             q = "select * from customers where account_no = {}".format(account_no)
#             curr = self.con.cursor()
#             curr.execute(q)
#             res = curr.fetchone()
#             if res :
#              query = "delete from customers where account_no = {}".format(account_no)
#              cur = self.con.cursor()
#              cur.execute(query)
#              self.con.commit()
#              print("Customer Deleted successfully at  ", self.dates1)
#              print()
#             else:
#                 print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT")
#
#     def update_customer(self, account_no):
#         q = "select * from customers where account_no = {}".format(account_no)
#         curr = self.con.cursor()
#         curr.execute(q)
#         res = curr.fetchall()
#         if res:
#             newName = input("enter newname : ").capitalize()
#             while True:
#                 newphone = int(input('enter your phone number : '))
#                 if len(str(newphone)) > 10 or len(str(newphone)) < 10:
#                     print("Invalid phone number ! please enter 10 digit only ")
#                 else:
#                     break
#             newaddress = input("enter newaddress : ").capitalize()
#             query = "update customers set name = '{}' , phone = {} , Address = '{}' where account_no = {} ".format(
#                 newName, newphone, newaddress, account_no)
#             cur = self.con.cursor()
#             cur.execute(query)
#             self.con.commit()
#             print("Account details updated successfully  at ", self.dates1)
#         else:
#             print("ACCOUNT DOESNT EXIST ! PLEASE TRY WITH VALID ACCOUNT")
#
#     def deleteAllcustomers(self):
#             query = "delete from customers"
#             curr = self.con.cursor()
#             curr.execute(query)
#             self.con.commit()
#             print('All customers deleted at ', self.dates1)