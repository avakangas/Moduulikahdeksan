import mysql.connector
from mysql.connector import Error
from geopy.distance import great_circle

def luo_yhteys():
    try:
        yhteys = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='flight_game',
            user='root',
            password='Kangas1234'
        )
        return yhteys
    except Error as e:
        print(f"Virhe yhteyden luomisessa: {e}")
        return None

def hae_koordinaatit(yhteys, icao_koodi):
    try:
        cursor = yhteys.cursor()
        sql = "SELECT latitude, longitude FROM airport WHERE icao_code = %s"
        cursor.execute(sql, (icao_koodi,))
        tulos = cursor.fetchone()
        return tulos
    except Error as e:
        print(f"Virhe koordinaattien hakemisessa: {e}")
        return None

def laske_etaisyys(coord1, coord2):
    return great_circle(coord1, coord2).kilometers

yhteys = luo_yhteys()

if yhteys:
    icao1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ").strip().upper()
    icao2 = input("Anna toisen lentokentän ICAO-koodi: ").strip().upper()

    coords1 = hae_koordinaatit(yhteys, icao1)
    coords2 = hae_koordinaatit(yhteys, icao2)

    if coords1 and coords2:
        etaisyys = laske_etaisyys(coords1, coords2)
        print(f"Lentokenttien {icao1} ja {icao2} välinen etäisyys on {etaisyys:.2f} km.")

    yhteys.close()