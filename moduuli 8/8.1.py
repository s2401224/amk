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


def fetch_info(USER_ICAO):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{USER_ICAO}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(f"Airport name {row[0]} and it is located in {row[1]}")
    return


Usr_Input = input("Please enter ICAO code: ")
fetch_info(Usr_Input)