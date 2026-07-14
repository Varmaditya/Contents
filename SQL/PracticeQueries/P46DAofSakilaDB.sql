-- SUBQUERIES
-- NESTED QUERIES

USE sakila;

-- Movies longer than average movie length
SELECT title, length
FROM film
WHERE length > (
    SELECT AVG(length)
    FROM film
);

-- Customers who paid more than average payment
SELECT customer_id, amount
FROM payment
WHERE amount > (
    SELECT AVG(amount)
    FROM payment
);

-- Movie having maximum rental duration
SELECT title, rental_duration
FROM film
WHERE rental_duration = (
    SELECT MAX(rental_duration)
    FROM film
);

-- Customers who made highest payment
SELECT customer_id, amount
FROM payment
WHERE amount = (
    SELECT MAX(amount)
    FROM payment
);

-- Films whose rental rate is greater than average rental rate
SELECT title, rental_rate
FROM film
WHERE rental_rate > (
    SELECT AVG(rental_rate)
    FROM film
);

-- Nested Query
-- Find customer details whose payment is maximum
SELECT *
FROM customer
WHERE customer_id = (
    SELECT customer_id
    FROM payment
    WHERE amount = (
        SELECT MAX(amount)
        FROM payment
    )
    LIMIT 1
);

-- Nested Query
-- Find film having longest duration
SELECT *
FROM film
WHERE length = (
    SELECT MAX(length)
    FROM film
);

-- Subquery using IN
-- Customers who have made payments
SELECT first_name, last_name
FROM customer
WHERE customer_id IN (
    SELECT customer_id
    FROM payment
);

-- Films available in inventory
SELECT title
FROM film
WHERE film_id IN (
    SELECT film_id
    FROM inventory
);

-- Customers who paid more than $10
SELECT first_name, last_name
FROM customer
WHERE customer_id IN (
    SELECT customer_id
    FROM payment
    WHERE amount>10
);

-- Customers who rented movies from Store 1
SELECT
first_name,
last_name
FROM customer
WHERE store_id = (
    SELECT store_id
    FROM store
    WHERE store_id=1
);

-- Movie titles having same rental duration
-- as "ACADEMY DINOSAUR"
SELECT title, rental_duration
FROM film
WHERE rental_duration = (
    SELECT rental_duration
    FROM film
    WHERE title='ACADEMY DINOSAUR'
);

-- Movies having replacement cost greater
-- than average replacement cost
SELECT title, replacement_cost
FROM film
WHERE replacement_cost > (
    SELECT AVG(replacement_cost)
    FROM film
);

-- Films having rental rate equal to
-- minimum rental rate
SELECT title, rental_rate
FROM film
WHERE rental_rate = (
    SELECT MIN(rental_rate)
    FROM film 
);
