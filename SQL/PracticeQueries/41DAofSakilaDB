-- MOVIE CATALOG ANALYSIS

-- Select Database
USE sakila;

-- VIEW COMPLETE FILM TABLE
SELECT *
FROM film;

-- DISPLAY ONLY REQUIRED COLUMNS
SELECT title, release_year, rating, rental_rate
FROM film;

-- MOVIES STARTING WITH LETTER 'A'
SELECT title
FROM film
WHERE title LIKE 'A%';

-- MOVIES ENDING WITH LETTER 'N'
SELECT title
FROM film
WHERE title LIKE '%N';

-- MOVIES CONTAINING THE WORD 'LOVE'
SELECT title
FROM film
WHERE title LIKE '%LOVE%';

-- SECOND LETTER IS 'A'
-- UNDERSCORE REPRESENTS ONE CHARACTER
SELECT title
FROM film
WHERE title LIKE '_A%';

-- MOVIE TITLES HAVING EXACTLY FIVE LETTERS
SELECT title
FROM film
WHERE title LIKE '_____';

-- RENTAL RATE BETWEEN 2 AND 4
SELECT title, rental_rate
FROM film
WHERE rental_rate BETWEEN 2 AND 4;

-- MOVIE LENGTH BETWEEN 90 AND 120 MINUTES
SELECT title, length
FROM film
WHERE length BETWEEN 90 AND 120;

-- MOVIES RATED G, PG OR PG-13
SELECT title, rating
FROM film
WHERE rating IN ('G','PG','PG-13');

-- MULTIPLE CONDITIONS
SELECT title, rating, rental_rate
FROM film
WHERE rating='PG'
AND rental_rate < 3;

-- MULTIPLE CONDITIONS USING OR
SELECT title, rating
FROM film
WHERE rating='R'
OR rating='NC-17';

-- NOT CONDITION
SELECT title, rating
FROM film
WHERE rating <> 'PG';

-- ORDER BY TITLE
SELECT title
FROM film
ORDER BY title ASC;

-- LONGEST MOVIES FIRST
SELECT title, length
FROM film
ORDER BY length DESC;

-- ORDER BY MULTIPLE COLUMNS
SELECT title, rating, rental_rate
FROM film
ORDER BY rating ASC, rental_rate DESC;

-- TOP 10 LONGEST MOVIES
SELECT title, length
FROM film
ORDER BY length DESC
LIMIT 10;

-- CHEAPEST 15 MOVIES
SELECT title, rental_rate
FROM film
ORDER BY rental_rate ASC
LIMIT 15;

-- FIRST 20 MOVIES
SELECT *
FROM film
LIMIT 20;
