#Author : Bhavya Chugh
# Using flask run a web application and insert data from web to database

from flask import Flask, render_template, request
from dbconnect import connection
app = Flask(__name__)


@app.route('/')
def student():
   return render_template('index.html')

@app.route('/studentregister')
def studentregister():
    try:
        #return render_template('register.html')
        mycursor, conn = connection()
        return "Connected"
    except Exception:
        return "Wrong"

if __name__ == '__main__':
   app.run(debug = True)
