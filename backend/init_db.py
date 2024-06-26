from dotenv import dotenv_values
import sqlite3

"""
Module that is used to instanciate a new database and create a admin user
"""

connection: sqlite3.Connection = sqlite3.connect("./backend/users.db")
config_values = dotenv_values(".env")

with open("./backend/users.sql") as f:
    connection.executescript(f.read())

db_cursor: sqlite3.Cursor = connection.cursor()

db_cursor.execute(
    "INSERT INTO users (name, password, favorite_city) VALUES (?, ?, ?)",
    (
        config_values.get("ADMIN_USERNAME"),
        config_values.get("ADMIN_PASSWORD"),
        config_values.get("ADMIN_FAVORITE_CITY"),
    ),
)

connection.commit()
connection.close()
