/*
CUSTOMERS AND PRODUCTS ANALYSIS USING SQL
PROGRAM 2: Customer & Product Exploration using SQL

Manager's Task:
The management team wants to understand
the available customer, product, order,
and payment data before performing
business analysis.

Write SQL queries to answer the
following business questions.
*/

USE RetailAnalytics;

-- ====================================================
-- SECTION A : CUSTOMER ANALYSIS
-- ====================================================

-- Task 1 Display all customer records.
SELECT * FROM customers;

-- Task 2 Display only Customer ID, City and State.
SELECT customer_id, customer_city, customer_state
FROM customers;

-- Task 3 Display unique customer cities.
SELECT DISTINCT customer_city
FROM customers;

-- Task 4 Display unique customer states.
SELECT DISTINCT customer_state
FROM customers;

-- Task 5 Find customers belonging to São Paulo.
SELECT * FROM customers
WHERE customer_city = 'sao paulo';

-- Task 6 Find customers from Rio de Janeiro.
SELECT * FROM customers
WHERE customer_city = 'rio de janeiro';

-- Task 7 Display customers from São Paulo OR Rio de Janeiro.
SELECT * FROM customers
WHERE customer_city IN ('sao paulo','rio de janeiro');

-- Task 8 Display customers whose city starts with 's'.
SELECT * FROM customers
WHERE customer_city LIKE 's%';

-- Task 9 Display customers whose city ends with 'a'.
SELECT * FROM customers
WHERE customer_city LIKE '%a';

-- Task 10 Display first 20 customers.
SELECT * FROM customers LIMIT 20;

-- ====================================================
-- SECTION B : PRODUCT ANALYSIS
-- ====================================================

-- Task 11 Display all products.
SELECT * FROM products;

-- Task 12 Display Product Category Names.
SELECT product_category_name FROM products;

-- Task 13 Display unique product categories.
SELECT DISTINCT product_category_name FROM products;

-- Task 14 Display products having category names starting with 'c'.
SELECT * FROM products
WHERE product_category_name LIKE 'c%';

-- Task 15 Display products whose category contains the word 'fashion'.
SELECT * FROM products
WHERE product_category_name LIKE '%fashion%';

-- Task 16 Display products having weight between 500 and 1500 grams.
SELECT * FROM products
WHERE product_weight_g BETWEEN 500 AND 1500;

-- Task 17 Display products weighing more than 5000 grams.
SELECT * FROM products
WHERE product_weight_g > 5000;

-- Task 18 Display products with missing category names.
SELECT * FROM products
WHERE product_category_name IS NULL;

-- Task 19 Display products ordered by weight.
SELECT * FROM products
ORDER BY product_weight_g;

-- Task 20 Display top 15 heaviest products.
SELECT * FROM products
ORDER BY product_weight_g DESC
LIMIT 15;

-- ====================================================
-- SECTION C : ORDER ANALYSIS
-- ====================================================

-- Task 21 Display all orders.
SELECT * FROM orders;

-- Task 22 Display delivered orders.
SELECT * FROM orders
WHERE order_status = 'delivered';

-- Task 23 Display cancelled orders.
SELECT * FROM orders
WHERE order_status = 'canceled';

-- Task 24 Display shipped orders.
SELECT * FROM orders
WHERE order_status = 'shipped';

-- Task 25 Display orders placed in 2018.
SELECT * FROM orders
WHERE order_purchase_timestamp LIKE '2018%';

-- Task 26 Display orders placed during January 2018.
SELECT * FROM orders
WHERE order_purchase_timestamp LIKE '2018-01%';

-- Task 27 Display first 30 orders.
SELECT * FROM orders
LIMIT 30;

-- Task 28 Display orders sorted by purchase date.
SELECT * FROM orders
ORDER BY order_purchase_timestamp;

-- Task 29 Display latest 20 orders.
SELECT * FROM orders
ORDER BY order_purchase_timestamp DESC
LIMIT 20;

-- Task 30 Display orders whose status is either delivered or shipped.
SELECT * FROM orders
WHERE order_status IN ('delivered','shipped');

-- ====================================================
-- SECTION D : PAYMENT ANALYSIS
-- ====================================================

-- Task 31 Display all payment records.
SELECT * FROM order_payments;

-- Task 32 Display unique payment methods.
SELECT DISTINCT payment_type
FROM order_payments;

-- Task 33 Display payments made using credit card.
SELECT * FROM order_payments
WHERE payment_type = 'credit_card';

-- Task 34 Display payments greater than 500.
SELECT * FROM order_payments
WHERE payment_value > 500;

-- Task 35 Display payments between 100 and 500.
SELECT * FROM order_payments
WHERE payment_value BETWEEN 100 AND 500;

-- Task 36 Display payments sorted from highest to lowest.
SELECT * FROM order_payments
ORDER BY payment_value DESC;

-- ====================================================
-- SECTION E : MIXED BUSINESS QUESTIONS
-- ====================================================

-- Task 37 Display products having NULL weight.
SELECT * FROM products
WHERE product_weight_g IS NULL;

-- Task 38 Display orders with non-null delivered dates.
SELECT * FROM orders
WHERE order_delivered_customer_date IS NOT NULL;

-- Task 39 Display first 10 records from every table for quick inspection.
SELECT * FROM customers LIMIT 10;

SELECT * FROM products LIMIT 10;

SELECT * FROM orders LIMIT 10;

SELECT * FROM order_payments LIMIT 10;

-- Task 40 Prepare a summary of available data. 
SELECT COUNT(*) AS TotalCustomers
FROM customers;

SELECT COUNT(*) AS TotalProducts
FROM products;

SELECT COUNT(*) AS TotalOrders
FROM orders;

SELECT COUNT(*) AS TotalPayments
FROM order_payments;


/*
Congratulations!
You have successfully explored the Retail Analytics
database by retrieving customer, product, order,
and payment information.
*/
