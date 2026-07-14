-- SQL JOINS
-- INNER JOIN, LEFT JOIN, RIGHT JOIN, CROSS JOIN, SELF JOIN

USE sakila;

-- INNER JOIN
-- Display customer names with their addresses
SELECT customer.customer_id, customer.first_name, customer.last_name, address.address
FROM customer
INNER JOIN address
ON customer.address_id = address.address_id;

-- INNER JOIN
-- Display city and country names
SELECT city.city, country.country
FROM city
INNER JOIN country
ON city.country_id = country.country_id;

-- INNER JOIN
-- Display film titles with their language
SELECT film.title, language.name AS Language
FROM film
INNER JOIN language
ON film.language_id = language.language_id;

-- LEFT JOIN
-- Display all customers and their payments
-- Even if no payment exists
SELECT customer.customer_id, customer.first_name, payment.amount
FROM customer
LEFT JOIN payment
ON customer.customer_id = payment.customer_id;

-- LEFT JOIN
-- Display all films and inventory records
SELECT film.title, inventory.inventory_id
FROM film
LEFT JOIN inventory
ON film.film_id = inventory.film_id;

-- RIGHT JOIN
-- Display all payments with customer names
SELECT customer.first_name, payment.amount
FROM customer
RIGHT JOIN payment
ON customer.customer_id = payment.customer_id;

-- RIGHT JOIN
-- Display inventory with movie titles
SELECT film.title, inventory.store_id
FROM film
RIGHT JOIN inventory
ON film.film_id = inventory.film_id;

-- CROSS JOIN
-- Generate all possible combinations
-- between stores and staff
SELECT store.store_id, staff.first_name
FROM store
CROSS JOIN staff;

-- CROSS JOIN
-- Cities with all Stores
SELECT city.city, store.store_id
FROM city
CROSS JOIN store
LIMIT 20;

-- SELF JOIN
-- Display staff members working in the
-- same store
SELECT A.first_name AS Staff_1, B.first_name AS Staff_2, A.store_id
FROM staff A
JOIN staff B
ON A.store_id = B.store_id
AND A.staff_id <> B.staff_id;

-- SELF JOIN
-- Compare customers belonging to same store
SELECT A.first_name, B.first_name, A.store_id
FROM customer A
JOIN customer B
ON A.store_id=B.store_id
AND A.customer_id<B.customer_id
LIMIT 20;
