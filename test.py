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
        5. Keluar\n""")

        choice = input("Masukkan pilihan Anda: \n")
        
        if choice == "1":
            main_system.display_products(cursor)
            print("")
        elif choice == "2":
            product_id = int(input("Masukkan ID Produk: "))
            quantity = int(input("Masukkan Kuantitas: "))
            main_system.add_to_cart(cart, product_id, quantity)
            print("")
        elif choice == "3":
            total = main_system.calculate_total(cursor, cart)
            print(f"Total: {total}")
            print("")
        elif choice == "4":
            main_system.complete_purchase(cursor, cart)
            cart = []
            print("")
        elif choice == "5":
            break

display()
conn.close()