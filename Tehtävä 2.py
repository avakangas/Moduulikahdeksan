import mysql.connector

def maakoodi(koodi):
    sql = f"SELECT name,type FROM airport where maakoodi='{koodi}'"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Kangas1234',
         autocommit=True
         )\

koodi= input("Anna maakoodi: ")
maakoodi(koodi)
