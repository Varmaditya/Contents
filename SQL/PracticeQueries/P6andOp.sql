-- AND operator checks multiple conditions
-- Both conditions must be true

USE sakila;

SELECT title, rental_rate, replacement_cost
FROM film
WHERE rental_rate > 2
AND replacement_cost < 20;
