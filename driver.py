from DBHELPHER import DBHelpher
from Admin import Admin
from logging import exception, raiseExceptions
import datetime as date

def main() :
      spl_char = ['.', '#''!', '@', '%', '^', '&', '/', '=', '?', '-', '$']
      print()
      print("  WELCOME TO  ", DBHelpher.Bank_name)
      helpher = DBHelpher()
      admin = Admin()
      print()
      # while True :
      inp = int(input("please enter 1 for USER AND  2 for ADMIN  :  "))
      if inp == 1 :

        usr = input("please enter 1 for NEW CUSTOMER  or 2 for EXISTING CUSTOMER ")
        if usr == '1':

          # while True:

            print()
            print("CREATE NEW ACCOUNT  ")

            try :
                  while True :
                    try :
                        spl_char = str(['.','#''!','@','%','^','&','/','=','?','-','$'])
                        name = input('please enter your name : ').capitalize()
                        if spl_char in name :
                            raise TypeError
                        break
                    except TypeError as msg :
                        print("special character are not allowed like .., * % # $ @",msg )


                  while True :
                    phone = int(input('enter your 10 digit  phone number : '))
                    if len(str(phone)) > 10 or len(str(phone)) < 10 :
                      print("Invalid phone number ! please enter 10 digit only ")
                    else :
                        break
                  while True :
                      try :
                        DOB = input('please enter you date of birth in DD/MM/YYYY format ')
                        DOB = date.datetime.strptime(DOB,"%d/%m/%y").date()
                        break
                      except ValueError:
                          print("Please enter Date of birth in proper format !!! DD/MM/YYYY")

                  Address = input('enter your address : ').capitalize()
                  while True :
                     opening_bal = int(input("please enter your opening balance : "))
                     if opening_bal <= 0 :
                         print('opening balance cant be zero ')
                     elif opening_bal >= 15000 :
                         print("OPENING BALANCE CANT BE MORE THAN 15000")
                     else :
                         break

                  while True :
                      try :
                        password = input('please enter password ')
                        if (len(password) < 6):
                           raise ValueError(" Password should contain at least 6 character ")
                        if not any(char.isdigit() for char in password):
                           raise ValueError("Password should atleast a number")
                        if not any(char.isupper() for char in password):
                           raise KeyError()
                        if not any(char.islower() for char in password):
                           raise KeyError
                        if not any(char in spl_char for char in password):
                           raise KeyError
                        break
                      except ValueError:
                          print(
                             "Password should contain atleast 1 upper case, 1 Lower Case , 1 Special Character  and Password Must Contain atleast 7 character")
                      except KeyError:
                           print(
                            "Password should contain atleast 1 upper case, 1 Lower Case , 1 Special Character  and Password Must Contain atleast 7 character")


                  helpher.create(name,phone,DOB,Address,opening_bal,password)
                  # break
            except Exception as e :
              print(e)
              print("INVALID DETAILS ! TRY AGAIN")
        elif usr == '2' :
           while True :

                print()
                print("Enter 1 to display your account details  ")
                print("Enter 2 to delete your account  ")
                print("Enter 3 to update  your account  account ")
                print("Enter 4 to deposit to an account  ")
                print("Enter 5 to withdrawn from   an  account ")
                print("Enter 6 to complete an transactions ")
                print()
                try :
                 choice = int(input("enter your choice to perform operations : "))

                 if choice == 1 :
                    i = 0
                    while True :
                      cus = int(input("please enter your account number to fetch your  information : "))
                      helpher.find_customer(cus)
                      break

                 elif choice == 2 :
                  cus = int(input("please enter an account number to delete your account : "))
                  helpher.delete_customer(cus)


                 elif choice == 3 :
                  cid = int(input("please enter account number to update your details "))
                  helpher.update_customer(cid)


                 elif choice == 4 :
                  acc_no = int(input("please enter your account number to deposit "))
                  helpher.deposit(acc_no)

                 elif choice == 5 :
                  acc_no = int(input("please enter your account number to withdrawn "))
                  helpher.withdrawn(acc_no)


                 elif choice == 6 :
                  print('Thank you for using Rev bank ! Welcome back ')
                  break
                 elif choice >= 7 :
                  print("Invalid input ! try again  ")
                 else:
                     print("Try Again ")
                except Exception as e :
                 print(e)
                 print('Invalid details ! Try again ')
      elif inp == 2:
        # while True:
          username = input('please enter username : ')
          password = input('pleasse enter password')
          if username != admin.admin and password != admin.password:
              print("please enter correct credentials ")
          else :
           while True :
             print()
             print("Enter 1 to display  all customers  ")
             print("Enter 2 to display a specific customer  ")
             print("Enter 3 to delete an  account ")
             print("Enter 4 to update  an  account ")
             print("Enter 5 to delete all customers ")
             print("Enter 6 to complete an transactions ")
             print()
             try :
                choice = int(input('please enter your choice to perform operations '))

                if choice == 1:
                   admin.showall_customers()
                elif choice == 2 :
                   inp = int(input("please enter account number to fetch customer details : "))
                   admin.find_customer(inp)
                elif choice == 3 :
                   inp = int(input("please enter account number to delete customer  : "))
                   admin.delete_customer(inp)
                elif choice == 4 :
                   cid = int(input("please enter account number to update your details "))
                   admin.update_customer(cid)
                elif choice == 5:
                   admin.deleteAllcustomers()
                elif choice == 6 :
                   print("Thank you admin ! see you soon ")
                   break
                else :
                   print("Invalid input ! try again ")
             except Exception as e :
               print(e)
               print("invalid details ! try again ")
      else :
          print("invalid input !  PLEASE ENTER 1 FOR USER AND 2 FOR ADMIN  ")

if __name__ == "__main__" :
    main()