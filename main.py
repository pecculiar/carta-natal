from flask import Flask, render_template, request
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const
import os

app = Flask(__name__, static_url_path='/public', static_folder='public')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carta', methods=['POST'])
def carta():
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    city = request.form['city']
    lat = request.form['lat']
    lon = request.form['lon']

    datetime = Datetime(f"{date}", f"{time}", '+00:00')
    pos = GeoPos(lat, lon)
    chart = Chart(datetime, pos)

    planets = [const.SUN, const.MOON, const.MERCURY, const.VENUS, const.MARS,
               const.JUPITER, const.SATURN, const.URANUS, const.NEPTUNE, const.PLUTO]

    results = []
    for planet in planets:
        obj = chart.get(planet)
        results.append({
            'planet': obj.name,
            'sign': obj.sign,
            'house': obj.house,
            'lon': f"{obj.lon:.2f}°"
        })

    return render_template('result.html', name=name, date=date, time=time, city=city, results=results)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)