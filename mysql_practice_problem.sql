create database online_book_store;
use online_book_store;
create table books(book_id int primary key,title varchar(30),author_id int references author(author_id),price float,publication_year int);
create table author(author_id int primary key,author_name varchar(30),country varchar(30));
create table orders(order_id int primary key,book_id int references books(book_id),customer_name varchar(30),order_date varchar(30));
insert into books values(101,"THE GIRL ON TH TRAIN",1000,250.00,2017);
insert into books values(102,"AADUJEEVITHAM",1040,366.00,2016);
insert into books values(103,"WINGS OF FIRE",1028,200.00,2013);
insert into author values(1000,"RUSKIN BOND","india");
insert into author values(1040,"BENYAMIN","india");
insert into author values(1028,"A P J ABDULKALAM","india");
insert into orders values(1007,101,"Anjana","8/07/23");
insert into orders values(1008,101,"Sruthi","8/07/23");
insert into orders values(1009,102,"Keerthy","8/07/23");
insert into orders values(1010,102,"Sneha","8/07/23");
insert into orders values(1011,103,"Dilna","8/07/23");
select * from books;
select * from author;
select * from orders;
alter table books add(genre varchar(30));
alter table orders add(quantity int);
select * from books inner join author where books.author_id=author.author_id;
select * from orders inner join books where orders.book_id=books.book_id;