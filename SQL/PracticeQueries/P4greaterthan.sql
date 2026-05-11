-- This query displays films where rental duration
-- is greater than 5 days

USE sakila;

SELECT title, rental_duration
FROM film
WHERE rental_duration > 5;
