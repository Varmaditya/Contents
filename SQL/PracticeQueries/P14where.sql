-- Switch to world database
-- This query displays countries from Asia

USE world;

SELECT Name, Continent
FROM country
WHERE Continent = 'Asia';
