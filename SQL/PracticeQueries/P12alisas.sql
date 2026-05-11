-- AS keyword is used to give temporary names
-- to columns in the output

USE sakila;

SELECT first_name AS "First Name",
       last_name AS "Last Name"
FROM actor;
