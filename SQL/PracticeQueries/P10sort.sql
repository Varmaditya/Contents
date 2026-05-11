-- DESC means descending order
-- Highest rental rates will appear first

USE sakila;

SELECT title, rental_rate
FROM film
ORDER BY rental_rate DESC;
