import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database= 'flight_game',
    user='root',
    password='Kangas1234',
    autocommit=True
)

def hae_lentokentta_icao_koodilla(icao):
    sql = f"SELECT * FROM airport WHERE ident = '{icao}'"
    print(sql)
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()
    print(tulos)
hae_lentokentta_icao_koodilla('EFHK')