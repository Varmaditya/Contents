-- This query displays cities sorted by population
-- from highest to lowest

USE world;

SELECT Name, Population
FROM city
ORDER BY Population DESC
LIMIT 10;
