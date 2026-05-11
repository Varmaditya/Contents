-- This query shows customers belonging to store 1

USE sakila;

SELECT first_name, last_name, store_id
FROM customer
WHERE store_id = 1;
