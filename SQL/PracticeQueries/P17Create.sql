-- CREATE DATABASE FOR ONLINE SHOP
CREATE DATABASE ecommerce_db;

-- USE THE DATABASE
USE ecommerce_db;

-- CREATE PRODUCTS TABLE
-- This table stores product information
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2),
    stock INT,
    launch_date DATE
);

-- SHOW ALL TABLES
SHOW TABLES;

-- DISPLAY TABLE STRUCTURE
DESC products;
