import requests
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    url = 'https://api.openweathermap.org/data/2.5/weather?q{}&appid=4b186ad071f8db7ed997cee6933da4d2'
    city = 'Lagos'

    res = requests.get(url.format(city)).json()
    print(res)

    return render_template('weather.html')




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)