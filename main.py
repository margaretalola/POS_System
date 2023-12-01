import preparing
import main_system

conn = preparing.conn()
cursor = preparing.get_cursor(conn)

def display():
    cart = []
    while True:
        print("""
        1. Tampilkan produk
        2. Tambahkan ke keranjang
        3. Hitung total
        4. Selesaikan pembelian
        5. Keluar""")

        choice = input("Masukkan pilihan Anda: \n")
        
        if choice == "1":
            print("")
            main_system.display_products(cursor)
            print("")
        elif choice == "2":
            product_id = int(input("Masukkan ID Produk: "))
            quantity = int(input("Masukkan Kuantitas: "))
            main_system.add_to_cart(cart, product_id, quantity, cursor)
            print("")
        elif choice == "3":
            main_system.display_cart(cart, cursor)
            total = main_system.calculate_total(cursor, cart)
            print(f"Total: {total}")
            print("")
        elif choice == "4":
            main_system.display_cart(cart, cursor)
            total = main_system.calculate_total(cursor, cart)
            print(f"Total: {total}")

            payment_amount = int(input("Enter payment amount: "))
            change = main_system.calculate_change(total, payment_amount)
            print(f"Kembalian: {change}")
            cart = []
            print("")
        elif choice == "5":
            break

display()
conn.close()