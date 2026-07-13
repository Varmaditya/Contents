-- BUSINESS REPORTS
-- Topics:
-- GROUP BY, HAVING, Filtering Grouped Data

USE sakila;

-- NUMBER OF MOVIES IN EACH RATING
SELECT rating,
COUNT(*) AS Total_Movies
FROM film
GROUP BY rating;

-- AVERAGE MOVIE LENGTH FOR EACH RATING
SELECT rating, AVG(length) AS Average_Length
FROM film
GROUP BY rating;

-- LONGEST MOVIE IN EACH RATING
SELECT rating, MAX(length) AS Longest_Movie
FROM film
GROUP BY rating;

-- SHORTEST MOVIE IN EACH RATING
SELECT rating, MIN(length) AS Shortest_Movie
FROM film
GROUP BY rating;

-- TOTAL RENTAL RATE OF EACH RATING
SELECT rating, SUM(rental_rate) AS Total_Rental_Rate
FROM film
GROUP BY rating;

-- NUMBER OF MOVIES FOR EACH RENTAL DURATION
SELECT rental_duration,
COUNT(*) AS Total_Movies
FROM film
GROUP BY rental_duration
ORDER BY rental_duration;

-- RATINGS HAVING MORE THAN 200 MOVIES
SELECT rating,
COUNT(*) AS Total_Movies
FROM film
GROUP BY rating
HAVING COUNT(*) > 200;

-- RENTAL DURATIONS HAVING MORE THAN 150 MOVIES
SELECT rental_duration,
COUNT(*) AS Total_Movies
FROM film
GROUP BY rental_duration
HAVING COUNT(*) > 150;

-- RATINGS HAVING AVERAGE MOVIE LENGTH
-- GREATER THAN 110 MINUTES
SELECT rating, AVG(length) AS Average_Length
FROM film
GROUP BY rating
HAVING AVG(length) > 110;

-- RENTAL DURATIONS HAVING MAXIMUM MOVIE
-- LENGTH GREATER THAN 180 MINUTES
SELECT rental_duration, MAX(length) AS Longest_Movie
FROM film
GROUP BY rental_duration
HAVING MAX(length) > 180;

-- SORT GROUPED RESULTS
SELECT rating,
COUNT(*) AS Total_Movies
FROM film
GROUP BY rating
ORDER BY Total_Movies DESC;

-- TOP 3 RATINGS HAVING HIGHEST NUMBER OF MOVIES
SELECT rating,
COUNT(*) AS Total_Movies
FROM film
GROUP BY rating
ORDER BY Total_Movies DESC
LIMIT 3;

-- STAFF WHO HANDLED MORE THAN 7000 PAYMENTS
SELECT staff_id,
COUNT(*) AS Total_Payments
FROM payment
GROUP BY staff_id
HAVING COUNT(*) > 7000;

-- CUSTOMERS WHO PAID MORE THAN $150
SELECT customer_id, SUM(amount) AS Total_Paid
FROM payment
GROUP BY customer_id
HAVING SUM(amount) > 150
ORDER BY Total_Paid DESC;
