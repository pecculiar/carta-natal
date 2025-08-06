    from flatlib.chart import Chart
    from flatlib.datetime import Datetime
    from flatlib.geopos import GeoPos

    def generar_carta(fecha, hora, lat, lon):
        date = Datetime(f'{fecha}', f'{hora}', '+00:00')
        pos = GeoPos(lat, lon)
        chart = Chart(date, pos)

        resultado = []
        for obj in ['SUN', 'MOON', 'ASC', 'MC', 'VENUS', 'MERCURY', 'MARS', 'JUPITER', 'SATURN']:
            item = chart.get(obj)
            resultado.append(f"{obj}: {item.sign} {item.lon}")

        return resultado