/*
Customers and Products Analysis Using SQL
Program 1: Database Setup and Data Exploration
*/

-- Step 1 : Create Database
CREATE DATABASE RetailAnalytics;

-- Step 2 : Use Database
USE RetailAnalytics;

-- Step 3 Import CSV Files
/*
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
Using MySQL Workbench
1. Right Click Database
2. Table Data Import Wizard
3. Select CSV File
4. Choose Create New Table
5. Finish

Import the following CSV files
customers.csv
products.csv
orders.csv
order_items.csv
order_payments.csv
*/

-- Step 4 View All Tables
SHOW TABLES;

-- Step 5 Understand Table Structure
DESCRIBE customers;

DESCRIBE products;

DESCRIBE orders;

DESCRIBE order_items;

DESCRIBE order_payments;

-- Step 6 View Sample Records
SELECT * FROM customers LIMIT 10;

SELECT * FROM products LIMIT 10;

SELECT * FROM orders LIMIT 10;

SELECT * FROM order_items LIMIT 10;

SELECT * FROM order_payments LIMIT 10;

-- Step 7 Count Records
SELECT COUNT(*) AS TotalCustomers
FROM customers;

SELECT COUNT(*) AS TotalProducts
FROM products;

SELECT COUNT(*) AS TotalOrders
FROM orders;

SELECT COUNT(*) AS TotalOrderItems
FROM order_items;

SELECT COUNT(*) AS TotalPayments
FROM order_payments;

-- Step 8 Display Column Information
SHOW COLUMNS FROM customers;

SHOW COLUMNS FROM products;

SHOW COLUMNS FROM orders;

SHOW COLUMNS FROM order_items;

SHOW COLUMNS FROM order_payments;

-- Step 9 Verify Database
SELECT DATABASE();

-- Step 10 Explore Distinct Values
SELECT DISTINCT customer_city
FROM customers
LIMIT 20;

SELECT DISTINCT payment_type
FROM order_payments;

SELECT DISTINCT order_status
FROM orders;

-- Step 11 Ready for Analysis

/*
Congratulations!
The Retail Analytics Database has been successfully prepared.
The imported dataset is now ready for Customer & Product Exploration
where we will begin answering real business questions using SQL.
*/
