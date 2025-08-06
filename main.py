from flask import Flask, render_template, request
from astro_calculator import generar_carta
import requests

app = Flask(__name__, static_url_path='/public', static_folder='public')

# Tu API key de Google Places
GOOGLE_

# Función para obtener latitud y longitud desde ciudad
def get_coords(city):
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={city}&key={GOOGLE_API_KEY}'
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None, None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    city = request.form['city']
    lat = request.form.get('lat') or None
    lon = request.form.get('lon') or None

    if not lat or not lon:
        lat, lon = get_coords(city)

    resultado = generar_carta(date, time, lat, lon)
    return render_template('result.html', resultado=resultado, name=name, date=date, time=time, city=city)

if __name__ == '__main__':
    app.run(debug=True)