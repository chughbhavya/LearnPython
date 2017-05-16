import mysql.connector

def connection():
    conn = mysql.connector.connect(user = "root", password = "bhavyaroot", host = "localhost"
                       ,database = "students")
    mycursor = conn.cursor()

    return mycursor, conn
