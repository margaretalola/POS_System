import mysql.connector
import preparing
import decimal

class Pilihan:
    def __init__(self, id, nama, harga, jumlah):
        self.id = id
        self.nama = nama
        self.harga = harga
        self.jumlah = jumlah

cart = []

def display_products(cursor):
    cursor.execute("SELECT * FROM inventory")
    inventory = cursor.fetchall()

    for product in inventory:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Stock: {product[3]}")

def add_to_cart(cart, product_id, quantity, cursor):
    # Check if the item is in the inventory
    cursor.execute("SELECT quantity FROM inventory WHERE item_code=%s", (product_id,))
    item_total = cursor.fetchone()[0]
    if item_total is not None:
        # Add the item to the cart
        cursor.execute("SELECT item_name, item_price FROM inventory WHERE item_code=%s", (product_id,))
        product_info = cursor.fetchone()
        nama, harga = product_info

        # Check if the quantity is valid
        if isinstance(quantity, int) and quantity > 0 and quantity <= item_total:
            pilihan = Pilihan(product_id, nama, harga, quantity)
            cart.append(pilihan.__dict__)
        else:
            print("Jumlah yang ingin dibeli tidak valid.")
    else:
        print("Stok tidak mencukupi.")


def display_cart(cart, cursor):
    print("Keranjang Belanja:")
    total_cart_price = 0

    for item in cart:
        product_id, nama, harga, quantity = item['id'], item['nama'], item['harga'], item['jumlah']

        total_item_price = harga * quantity
        total_cart_price += total_item_price

        print(f"ID: {product_id}, Name: {nama}, Price per unit: {harga}, Quantity: {quantity}, Total: {total_item_price}")

    print(f"Total Harga Keranjang: {total_cart_price}\n")

def calculate_total(cursor, cart):
    total = 0
    for item in cart:
        total += item['harga'] * item['jumlah'] 
    return total

def calculate_change(total, payment_amount):
    while payment_amount < total:
        print("Payment amount is less than total amount. Please try again.")
        payment_amount = int(input("Enter payment amount: "))
    
    change = payment_amount - total
    return change

def complete_purchase(cursor, cart):
    total = sum(item['harga'] * item['jumlah'] for item in cart)
    payment = float(input("Enter payment amount: ")) # Mengubah input menjadi float
    change = decimal.Decimal(payment - float(total))
    if change < 0:
        print("Insufficient payment, please add more!")
    else:
        for item in cart:
            item_id = item['id']
            quantity = item['jumlah']
            update_query = f"UPDATE inventory SET quantity = quantity - {quantity} WHERE item_code = {item_id}"
            cursor.execute(update_query)
        print("Pembelian berhasil.")
        preparing.conn().commit()


def insert_inventory(product_id, product_name, quantity):
    connection = create_connection()
    cursor = connection.cursor()

    cursor.execute("INSERT INTO inventory (item_code, item_name, quantity) VALUES (%s, %s, %s)", (product_id, product_name, quantity))
    connection.commit()

    cursor.execute("SELECT item_total FROM inventory WHERE item_code=%s", (product_id,))
    item_total = cursor.fetchone()[0]

    return item_total