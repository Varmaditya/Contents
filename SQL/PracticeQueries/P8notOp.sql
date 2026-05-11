-- NOT operator reverses a condition
-- This query shows customers not belonging to store 1

USE sakila;

SELECT first_name, last_name, store_id
FROM customer
WHERE NOT store_id = 1;
