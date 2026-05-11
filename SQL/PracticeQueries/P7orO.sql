-- OR operator checks multiple conditions
-- Any one condition can be true

USE sakila;

SELECT first_name, last_name
FROM actor
WHERE first_name = 'NICK'
OR last_name = 'GUINESS';
