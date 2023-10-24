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

tb_name = ["kasir", "inventory"]

# cursor = conn.cursor()

# checking.check_connection(conn)
# checking.using_database(conn.cursor(), "pos_system")  # Perbaiki penggunaan fungsi
# checking.check_table_exist(conn.cursor(), tb_name)
