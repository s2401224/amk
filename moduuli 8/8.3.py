import os
from dotenv import load_dotenv
import mysql.connector
from geopy.distance import geodesic
load_dotenv()

connection = mysql.connector.connect(
    host = os.getenv("HOST"),
    port = os.getenv("PORT"),
    database = os.getenv("DATABASE"),
    user = os.getenv("USER"),
    password = os.getenv("PASSWORD"),
    autocommit = True
)


def fetch_cords(ICAO1, ICAO2):
    sql1 = f"SELECT airport.ident, airport.latitude_deg, airport.longitude_deg FROM airport WHERE ident = '{ICAO1}'"
    sql2 = f"SELECT airport.ident, airport.latitude_deg, airport.longitude_deg FROM airport WHERE ident = '{ICAO2}'"
    cursor = connection.cursor()
    cursor.execute(sql1)
    ICAO1_result = cursor.fetchall()

    cursor.execute(sql2)
    ICAO2_result = cursor.fetchall()
    if cursor.rowcount > 0:
        
            point_a = (ICAO1_result[0][1], ICAO1_result[0][2])
            point_b = (ICAO2_result[0][1], ICAO2_result[0][2])
            distance = geodesic(point_a, point_b)
            print(f"Distance between those two airports is {distance.km:.2f} kilometers!")
    
    return

usr_input1 = input("ICAO1 please: ")
usr_input2 = input("ICAO2 please: ")

fetch_cords(usr_input1, usr_input2)