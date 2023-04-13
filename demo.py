import mysql.connector
con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "library_db",
    autocommit=True)
c=con.cursor(buffered=True)
c.execute("create database if not exists library_db")
c.execute("use library_db")
c.execute("create table if not exists books(b_id varchar(5) primary key,b_name varchar(50),author varchar(50),available varchar(5) Default 'yes')")
c.execute("create table if not exists issue_details(b_id varchar(5),s_id varchar(10),s_name varchar(50) Not null,foreign key(b_id) references books(b_id))")
def add_book():
    bid=input("Enter Book Id : ")
    title=input("Enter Book Name : ")
    author=input("Enter Author Name : ")
    data=(bid,title,author)
    sql='insert into books(b_id,b_name,author) values(%s,%s,%s)'
    c.execute(sql,data)
    print("Data Inserted Successfully For Book Id ",bid)
def delete_book():
    bid=input("Enter Book Id : ")
    c.execute("delete from books where b_id=%s",(bid,))
    display_books()
def issue_book():
    s_name=input("Enter Your Name : ")
    s_id=input("Enter Your Registered Number : ")
    book=input("Enter Book Name : ")
    c.execute("select b_id from books where b_name= '" + book +"' and available='YES'")
    book_id=c.fetchone()
    bid=book_id[0]
    print(bid)
    a="insert into issue_details values(%s,%s,%s)"
    data=(bid,s_id,s_name)
    c.execute(a,data)
    c.execute("update books set available='no' where b_id= '"+bid+" '")
    print(book , "Book Issued to  ",s_name)
def return_book():
    name=input("Enter Your Name : ")
    bid=input("Enter Your Book Id : ")
    c.execute("update books set available='yes' where b_id='"+bid+"'")
    c.execute("delete from issue_details where b_id=%s",(bid,))
    print("Book Id : ",bid,"Book Returned By ",name)
def display_books():
    sql="select * from books"
    c.execute(sql)
    my_result=c.fetchall()
    print("Book Id\t Book Title\t\tAuthor\tAvailable")
    for i in my_result:
        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3])
def select_book():
    book=input("Enter The Name of Book : ")
    sql="select * from books where b_name= '" + book + "'"
    c.execute(sql)
    my_result=c.fetchall()
    print("Book Id\t Book Title\t\tAuthor\tAvailable")
    for i in my_result:
         print(i[0],"\t",i[1],"\t",i[2],"\t",i[3])
def display_issued_books():
    c.execute("select issue_details. *,books.b_name from issue_details,books where issue_details.b_id=books.b_id")
    my_result=c.fetchall()
    print("List of Issued Books : ")
    print("Book_Id    Book_Name   Reg_No   Student_Name")
    for i in my_result:
        print(i[0]," ",i[3]," ",i[1]," ",i[2])
user_name=input("Enter User Name : ")
password=input("Enter Password : ")
if user_name=="admin" and password=="library1303":
    print("**Welcome Admin**")
    while True:
        print("**LIBRARY MANAGEMENT SYSTEM**")
        print("1.Add Book\n2.Issue Book\n3.Return Book\n4.Display Books\n5.Delete Book\n6.Exit")
        ch=input("Enter Your Choice : ")
        if ch=='1':
            add_book()
        elif ch=='2':
            issue_book()
        elif ch=='3':
            return_book()
        elif ch=='4':
            print("1.All Books   2.Issued Books   3.Particular Books")
            ch=input("Enter Your Choice : ")
            if ch=='1':
                display_books()
            elif ch=='2':
                display_issued_books()
            elif ch=='3':
                select_book()
            else:
                print("Wrong Choice")
        elif ch=='5':
            delete_book()
        else:
            break
else:
    print("Wrong Username Or Password Try Again! ")