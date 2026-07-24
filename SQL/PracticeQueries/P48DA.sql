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
SELECT * FROM olist_customers_dataset;

-- Task 2 Display only Customer ID, City and State.
SELECT customer_id, customer_city, customer_state
FROM olist_customers_dataset;

-- Task 3 Display unique customer cities.
SELECT DISTINCT customer_city
FROM olist_customers_dataset;

-- Task 4 Display unique customer states.
SELECT DISTINCT customer_state
FROM olist_customers_dataset;

-- Task 5 Find customers belonging to São Paulo.
SELECT *
FROM olist_customers_dataset
WHERE customer_city = 'sao paulo';

-- Task 6 Find customers from Rio de Janeiro.
SELECT *
FROM olist_customers_dataset
WHERE customer_city = 'rio de janeiro';

-- Task 7 Display customers from São Paulo OR Rio de Janeiro.
SELECT *
FROM olist_customers_dataset
WHERE customer_city IN ('sao paulo','rio de janeiro');

-- Task 8 Display customers whose city starts with 's'.
SELECT *
FROM olist_customers_dataset
WHERE customer_city LIKE 's%';

-- Task 9 Display customers whose city ends with 'a'.
SELECT *
FROM olist_customers_dataset
WHERE customer_city LIKE '%a';

-- Task 10 Display first 20 customers.
SELECT *
FROM olist_customers_dataset
LIMIT 20;


-- ====================================================
-- SECTION B : PRODUCT ANALYSIS
-- ====================================================

-- Task 11 Display all products.
SELECT * FROM olist_products_dataset;

-- Task 12 Display Product Category Names.
SELECT product_category_name
FROM olist_products_dataset;

-- Task 13 Display unique product categories.
SELECT DISTINCT product_category_name
FROM olist_products_dataset;

-- Task 14 Display products having category names starting with 'c'.
SELECT *
FROM olist_products_dataset
WHERE product_category_name LIKE 'c%';

-- Task 15 Display products whose category contains the word 'fashion'.
SELECT *
FROM olist_products_dataset
WHERE product_category_name LIKE '%fashion%';

-- Task 16 Display products having weight between 500 and 1500 grams.
SELECT *
FROM olist_products_dataset
WHERE product_weight_g BETWEEN 500 AND 1500;

-- Task 17 Display products weighing more than 5000 grams.
SELECT *
FROM olist_products_dataset
WHERE product_weight_g > 5000;

-- Task 18 Display products with missing category names.
SELECT *
FROM olist_products_dataset
WHERE product_category_name IS NULL;

-- Task 19 Display products ordered by weight.
SELECT *
FROM olist_products_dataset
ORDER BY product_weight_g;

-- Task 20 Display top 15 heaviest products.
SELECT *
FROM olist_products_dataset
ORDER BY product_weight_g DESC
LIMIT 15;

-- ====================================================
-- SECTION C : ORDER ANALYSIS
-- ====================================================

-- Task 21 Display all orders.
SELECT * FROM olist_orders_dataset;

-- Task 22 Display delivered orders.
SELECT *
FROM olist_orders_dataset
WHERE order_status = 'delivered';

-- Task 23 Display cancelled orders.
SELECT *
FROM olist_orders_dataset
WHERE order_status = 'canceled';

-- Task 24 Display shipped orders.
SELECT *
FROM olist_orders_dataset
WHERE order_status = 'shipped';

-- Task 25 Display orders placed in 2018.
SELECT *
FROM olist_orders_dataset
WHERE order_purchase_timestamp LIKE '2018%';


-- Task 26 Display orders placed during January 2018.
SELECT *
FROM olist_orders_dataset
WHERE order_purchase_timestamp LIKE '2018-01%';

-- Task 27 Display first 30 orders.
SELECT *
FROM olist_orders_dataset
LIMIT 30;

-- Task 28 Display orders sorted by purchase date.
SELECT *
FROM olist_orders_dataset
ORDER BY order_purchase_timestamp;

-- Task 29 Display latest 20 orders.
SELECT *
FROM olist_orders_dataset
ORDER BY order_purchase_timestamp DESC
LIMIT 20;

-- Task 30 Display orders whose status is either delivered or shipped.
SELECT *
FROM olist_orders_dataset
WHERE order_status IN ('delivered','shipped');

-- ====================================================
-- SECTION D : PAYMENT ANALYSIS
-- ====================================================

-- Task 31 Display all payment records.
SELECT * FROM olist_order_payments_dataset;

-- Task 32 Display unique payment methods.
SELECT DISTINCT payment_type
FROM olist_order_payments_dataset;

-- Task 33 Display payments made using credit card.
SELECT *
FROM olist_order_payments_dataset
WHERE payment_type = 'credit_card';

-- Task 34 Display payments greater than 500.
SELECT *
FROM olist_order_payments_dataset
WHERE payment_value > 500;


-- Task 35 Display payments between 100 and 500.
SELECT *
FROM olist_order_payments_dataset
WHERE payment_value BETWEEN 100 AND 500;

-- Task 36 Display payments sorted from highest to lowest.
SELECT *
FROM olist_order_payments_dataset
ORDER BY payment_value DESC;

-- ====================================================
-- SECTION E : MIXED BUSINESS QUESTIONS
-- ====================================================

-- Task 37 Display products having NULL weight.
SELECT *
FROM olist_products_dataset
WHERE product_weight_g IS NULL;

-- Task 38 Display orders with non-null delivered dates.
SELECT *
FROM olist_orders_dataset
WHERE order_delivered_customer_date IS NOT NULL;

-- Task 39 Display first 10 records from every table for quick inspection.
SELECT * FROM olist_customers_dataset LIMIT 10;

SELECT * FROM olist_products_dataset LIMIT 10;

SELECT * FROM olist_orders_dataset LIMIT 10;

SELECT * FROM olist_order_payments_dataset LIMIT 10;

-- Task 40 Prepare a summary of available data. 
SELECT COUNT(*) AS TotalCustomers
FROM olist_customers_dataset;

SELECT COUNT(*) AS TotalProducts
FROM olist_products_dataset;

SELECT COUNT(*) AS TotalOrders
FROM olist_orders_dataset;

SELECT COUNT(*) AS TotalPayments
FROM olist_order_payments_dataset;


/*
Congratulations!
You have successfully explored the Retail Analytics
database by retrieving customer, product, order,
and payment information.
*/
