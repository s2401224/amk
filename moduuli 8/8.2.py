import os
from dotenv import load_dotenv
import mysql.connector
load_dotenv()

connection = mysql.connector.connect(
    host = os.getenv("HOST"),
    port = os.getenv("PORT"),
    database = os.getenv("DATABASE"),
    user = os.getenv("USER"),
    password = os.getenv("PASSWORD"),
    autocommit = True
)


def fetch_country_airport_info(Country_code):
    sql = f"SELECT airport.type , COUNT(*) FROM airport WHERE airport.iso_country = '{Country_code}' GROUP BY airport.type"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        print(f"In the area under the code of '{Country_code}' there are: ")
        for row in result:
            print(f"type: {row[0]} amount: {row[1]}")
    return

country_code = input("Please provide country code: ")
fetch_country_airport_info(country_code)