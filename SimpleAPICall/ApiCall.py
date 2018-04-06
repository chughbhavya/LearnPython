"""
Accessing temperature from weatherapi using Flask in python and outputting it based on zipcode from user.
"""

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods = ['POST'])

#Function to access the APi and send the temparture to print on temperature webpage
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://samples.openweathermap.org/data/2.5/weather?zip=+zipcode+,us&appid=3a6eb028f243c17e534c9b4cdb7da188')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    temp_f = 1.8 * (temp_k - 273 ) + 32
    return render_template('temperature.html', temp = str(temp_f))

@app.route('/', methods = ['GET','POST'])

#Asking for zipcode from the user
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
