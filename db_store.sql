show databases
create database pos_system
use pos_system

CREATE TABLE inventory (
item_code INT PRIMARY KEY,
item_name VARCHAR(255),
item_price DECIMAL(10, 2),
quantity INT
);

INSERT INTO inventory (item_code, item_name, item_price, quantity)
VALUES 
(1, 'Buku', 5000, 100),
(2, 'Pulpen', 2500, 250),
(3, 'Penghapus', 4000, 99),
(4, 'Kertas hvs (pack)', 57000, 100),
(5, 'Pensil', 3000, 150);

CREATE TABLE kasir (
no INT AUTO_INCREMENT PRIMARY KEY,
item_code INT,
item_name VARCHAR(255),
item_price DECIMAL(10, 2),
FOREIGN KEY (item_code) REFERENCES inventory(item_code)
);

CREATE TABLE purchases (
id INT AUTO_INCREMENT PRIMARY KEY,
total DECIMAL(10, 2)
);

CREATE TABLE purchase_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    purchase_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (purchase_id) REFERENCES purchases(id),
    FOREIGN KEY (product_id) REFERENCES inventory(item_code)
);