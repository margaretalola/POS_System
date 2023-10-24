show databases;

create database pos_system;

use pos_system;

create table inventory(
    item_code int primary key,
    item_name varchar(255) null,
    item_price int null,
    item_total int null,
    constraint item_name unique (item_name)
);

insert into inventory (item_code, item_name, item_price, item_total)
values (123, "Buku", 5000, 100),
       (124, "Pulpen", 2500, 250),
       (122, "Penghapus", 4000, 99),
       (121, "Kertas hvs (pack)", 57000, 100),
       (125, "Pensil", 3000, 150);

show tables;

create table kasir(
    no int auto_increment primary key,
    item_code int,
    item_name varchar(255),
    count_items int,
    item_price int null,
    foreign key (item_code) references inventory(item_code)
);

show tables;
