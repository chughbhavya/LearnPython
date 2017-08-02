# Author : Bhavya Chugh
# This program makes a connection with MySql database and inserts data into it.
# Importing the MySQL connector
import mysql.connector

# Setting up a connection
conn = mysql.connector.connect(user = "root", password = "*******", host = "localhost"
                               ,database = "university")
mycursor = conn.cursor()

# Creating a table customer in databse university 
mycursor.execute("""Create table if not exists Customer
(
id int primary key,
name varchar(30),
email varchar(30),
city varchar(30),
age int,
gender char(1)
)""")

# Execute the insert statament
mycursor.execute(""" Insert into Customer values
(11, "Bhavya", "chugh.bhavya@gmail.com", "Plano", 25, "F")""")
mycursor.execute(""" Insert into Customer values
(2, "Milind", "chugh.bhavya@gmail.com", "Plano", 25, "F")""")
mycursor.execute(""" Insert into Customer values
(3, "Mansi", "chugh.bhavya@gmail.com", "Plano", 25, "F")""")
conn.commit()
mycursor.execute("Select * from Customer")
mylist = mycursor.fetchall()
for i in mylist:
    print(i)
