import mysql.connector
import checking

def conn():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="pos_system",
    )

    return connection

def get_cursor(connection):
    return connection.cursor()

tb_name = ["kasir", "inventory", "purchases"]