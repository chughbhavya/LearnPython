# Author : Bhavya Chugh
# Created on : 05/20/2017

import mysql.connector

# Making a connection with database and returning cursor and connection object
def connection():
    conn = mysql.connector.connect(user = "root", password = "******", host = "localhost"
                       ,database = "students")
    mycursor = conn.cursor()

    return mycursor, conn
