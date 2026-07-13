-- CUSTOMER DIRECTORY ANALYSIS

USE sakila;

-- VIEW CUSTOMER TABLE
SELECT *
FROM customer;

-- DISPLAY REQUIRED COLUMNS
SELECT first_name, last_name, email, store_id, active
FROM customer;

-- FIRST NAME STARTING WITH 'M'
SELECT first_name,last_name
FROM customer
WHERE first_name LIKE 'M%';

-- LAST NAME ENDING WITH 'SON'
SELECT first_name,last_name
FROM customer
WHERE last_name LIKE '%SON';

-- EMAIL CONTAINING 'MARY'
SELECT first_name,email
FROM customer
WHERE email LIKE '%MARY%';

-- FIRST NAME HAVING SECOND LETTER 'A'
SELECT first_name
FROM customer
WHERE first_name LIKE '_A%';

-- CUSTOMER IDS BETWEEN 50 AND 100
SELECT customer_id, first_name
FROM customer
WHERE customer_id BETWEEN 50 AND 100;

-- CUSTOMERS FROM STORE 1 OR STORE 2
SELECT first_name, last_name, store_id
FROM customer
WHERE store_id IN (1,2);

-- ACTIVE CUSTOMERS
SELECT first_name,last_name
FROM customer
WHERE active=1;

-- INACTIVE CUSTOMERS
SELECT first_name,last_name
FROM customer
WHERE active=0;

-- CUSTOMERS WHO HAVE CREATE DATE
SELECT first_name, create_date
FROM customer
WHERE create_date IS NOT NULL;

-- LAST UPDATE IS NULL
-- (May return no records depending on data)
SELECT *
FROM customer
WHERE last_update IS NULL;

-- LAST UPDATE IS NOT NULL
SELECT first_name, last_name, last_update
FROM customer
WHERE last_update IS NOT NULL;

-- MULTIPLE CONDITIONS
SELECT first_name, last_name, store_id
FROM customer
WHERE store_id=1
AND active=1;

-- MULTIPLE CONDITIONS USING OR
SELECT first_name, last_name
FROM customer
WHERE first_name LIKE 'A%'
OR first_name LIKE 'B%';

-- SORT BY LAST NAME
SELECT first_name, last_name
FROM customer
ORDER BY last_name ASC;

-- SORT BY STORE THEN FIRST NAME
SELECT first_name, last_name, store_id
FROM customer
ORDER BY store_id ASC,
first_name ASC;

-- FIRST 25 CUSTOMERS 
SELECT *
FROM customer
LIMIT 25;

-- CUSTOMER IDS 100 TO 120
SELECT customer_id, first_name, last_name
FROM customer
WHERE customer_id BETWEEN 100 AND 120
ORDER BY customer_id ASC;

-- FIRST 10 ACTIVE CUSTOMERS
SELECT first_name, last_name
FROM customer
WHERE active=1
LIMIT 10;
