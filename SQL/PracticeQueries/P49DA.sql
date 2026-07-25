/*
CUSTOMERS AND PRODUCTS ANALYSIS USING SQL
PROGRAM 3: Business Performance Analysis

Manager's Assignment: Prepare analytical reports using
Aggregate Functions, GROUP BY and HAVING.
*/

USE RetailAnalytics;

-- =====================================================
-- SECTION A : OVERALL BUSINESS STATISTICS
-- =====================================================

-- Task 1 : Total Customers
SELECT COUNT(*) AS Total_Customers
FROM customers;

-- Task 2 : Total Products
SELECT COUNT(*) AS Total_Products
FROM products;

-- Task 3 : Total Orders
SELECT COUNT(*) AS Total_Orders
FROM orders;

-- Task 4 : Total Payments
SELECT COUNT(*) AS Total_Payments
FROM order_payments;

-- Task 5 : Total Revenue
SELECT SUM(payment_value) AS Total_Revenue
FROM order_payments;

-- Task 6 : Average Payment
SELECT AVG(payment_value) AS Average_Payment
FROM order_payments;

-- Task 7 : Highest Payment
SELECT MAX(payment_value) AS Highest_Payment
FROM order_payments;

-- Task 8 : Lowest Payment
SELECT MIN(payment_value) AS Lowest_Payment
FROM order_payments;

-- =====================================================
-- SECTION B : CUSTOMER ANALYSIS
-- =====================================================

-- Task 9 : Customers by State
SELECT customer_state,
COUNT(*) AS Total_Customers
FROM customers
GROUP BY customer_state
ORDER BY Total_Customers DESC;

-- Task 10 : Customers by City
SELECT customer_city,
COUNT(*) AS Total_Customers
FROM customers
GROUP BY customer_city
ORDER BY Total_Customers DESC
LIMIT 20;

-- Task 11 : States having more than 500 customers
SELECT customer_state,
COUNT(*) AS Total_Customers
FROM customers
GROUP BY customer_state
HAVING COUNT(*) > 500;

-- =====================================================
-- SECTION C : PRODUCT ANALYSIS
-- =====================================================

-- Task 12 : Products by Category
SELECT product_category_name,
COUNT(*) AS Total_Products
FROM products
GROUP BY product_category_name
ORDER BY Total_Products DESC;

-- Task 13 : Average Product Weight
SELECT AVG(product_weight_g)
AS Average_Weight
FROM products;

-- Task 14 : Maximum Product Weight
SELECT MAX(product_weight_g)
AS Heaviest_Product
FROM products;

-- Task 15 : Categories having more than 100 products
SELECT product_category_name,
COUNT(*) AS Total_Products
FROM products
GROUP BY product_category_name
HAVING COUNT(*) > 100;

-- =====================================================
-- SECTION D : ORDER ANALYSIS
-- =====================================================

-- Task 16 : Orders by Status
SELECT order_status,
COUNT(*) AS Total_Orders
FROM orders
GROUP BY order_status
ORDER BY Total_Orders DESC;

-- Task 17 : Order Status having more than 1000 orders
SELECT order_status,
COUNT(*) AS Total_Orders
FROM orders
GROUP BY order_status
HAVING COUNT(*) > 1000;

-- =====================================================
-- SECTION E : PAYMENT ANALYSIS
-- =====================================================

-- Task 18 : Payment Methods Used
SELECT payment_type,
COUNT(*) AS Total_Transactions
FROM order_payments
GROUP BY payment_type
ORDER BY Total_Transactions DESC;

-- Task 19 : Revenue by Payment Method
SELECT payment_type, SUM(payment_value) AS Revenue
FROM order_payments
GROUP BY payment_type
ORDER BY Revenue DESC;

-- Task 20 : Average Payment by Payment Method
SELECT payment_type, AVG(payment_value) AS Average_Payment
FROM order_payments
GROUP BY payment_type;

-- Task 21 : Highest Payment by Payment Method
SELECT payment_type, MAX(payment_value) AS Highest_Payment
FROM order_payments
GROUP BY payment_type;

-- Task 22 : Lowest Payment by Payment Method
SELECT payment_type, MIN(payment_value) AS Lowest_Payment
FROM order_payments
GROUP BY payment_type;

-- Task 23 : Payment Methods generating
-- more than ₹100000 revenue

SELECT payment_type, SUM(payment_value) AS Revenue
FROM order_payments
GROUP BY payment_type
HAVING SUM(payment_value) > 100000;

-- Task 24 : Payment Methods having average payment greater than ₹200
SELECT payment_type, AVG(payment_value) AS Average_Payment
FROM order_payments
GROUP BY payment_type
HAVING AVG(payment_value) > 200;

/*
Congratulations!
You have successfully prepared
business reports using

COUNT()
SUM()
AVG()
MIN()
MAX()
GROUP BY
HAVING

These reports help management
understand the overall performance
of the business.

Next Program:

Advanced Customer & Sales Analytics
using JOINs and Subqueries.
*/
