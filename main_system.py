import mysql.connector 
import preparing

def display_products(cursor):
    cursor.execute("SELECT * FROM inventory")
    inventory = cursor.fetchall()

    for product in inventory:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}, Stock: {product[3]}")

def add_to_cart(cart, product_id, quantity):
    cart.append((product_id, quantity))

def calculate_total(cursor, cart):
    total = 0
    for item in cart:
        product_id, quantity = item
        cursor.execute("SELECT item_price FROM inventory WHERE item_code=%s", (product_id,))
        item_price = cursor.fetchone()[0]
        total += item_price * quantity 
    return total

def update_db_af_calculate_total(cursor, cart, total):
        for item in cart:
            product_id, quantity = item
            cursor.execute("UPDATE inventory SET item_total = item_total - %s WHERE item_code = %s", (quantity, product_id))
        
        # Simpan detail pembelian ke dalam database
        cursor.execute("INSERT INTO purchases (total) VALUES (%s)", (total,))
        purchase_id = cursor.lastrowid
        
        for item in cart:
            product_id, quantity = item
            cursor.execute("INSERT INTO purchase_items (purchase_id, product_id, quantity) VALUES (%s, %s, %s)",
                           (purchase_id, product_id, quantity))
        
        print("Pembelian berhasil.")
        a = preparing.conn()
        a.commit()

def complete_purchase(cursor, cart):
    total = calculate_total(cursor, cart)
    print(f'Total: {total}')
    payment = float(input('Masukkan jumlah pembayaran: '))

    if payment == total:
        update_db_af_calculate_total(cursor, cart, total)
        # for item in cart:
        #     product_id, quantity = item
        #     cursor.execute("UPDATE inventory SET item_total = item_total - %s WHERE item_code = %s", (quantity, product_id))
        
        # # Simpan detail pembelian ke dalam database
        # cursor.execute("INSERT INTO purchases (total) VALUES (%s)", (total,))
        # purchase_id = cursor.lastrowid
        
        # for item in cart:
        #     product_id, quantity = item
        #     cursor.execute("INSERT INTO purchase_items (purchase_id, product_id, quantity) VALUES (%s, %s, %s)",
        #                    (purchase_id, product_id, quantity))
        
        # print("Pembelian berhasil.")
        # a = preparing.conn()
        # a.commit()
    elif payment > total:
        update_db_af_calculate_total(cursor, cart, total)
        change = payment - total
        print(f"Kembalian {change}")
    else:
        print("Pembayaran tidak mencukupi.")
