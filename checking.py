import mysql.connector
import mysql.connector.errors

def check_connection(connection):
    try:
        connection.ping()
        print("Terhubung.")
    except mysql.connector.errors.Error as err:
        print("Gagal terhubung. Error: ", err)

def using_database(cursor, database):
    try:
        cursor.execute(f"USE {database}")
        print(f"Menggunakan {database} berhasil")
    except mysql.connector.Error as err:
        print("Gagal menggunakan database. Error: ", err)

def check_table_exist(cursor, tb_names):
    try:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        table_names = [tb[0] for tb in tables]

        for tb_name in tb_names:
            if tb_name in table_names:
                print(f"Tabel {tb_name} sudah ada.")
            else:
                print(f"Tabel {tb_name} tidak ada.")
    except mysql.connector.Error as err:
        print("Error:", err)