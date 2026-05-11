-- DISTINCT removes duplicate values
-- This query shows unique rental durations

USE sakila;

SELECT DISTINCT rental_duration
FROM film;
