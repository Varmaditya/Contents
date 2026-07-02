-- Select Database
USE world;

-- View Complete Table
SELECT * FROM country;

-- View Required Columns
SELECT Name, Continent, Population
FROM country;

-- Filter Data
SELECT *
FROM country
WHERE Continent = 'Asia';

-- Multiple Conditions
SELECT Name, Population
FROM country
WHERE Continent='Asia'
AND Population > 50000000;

-- Sort Population
SELECT Name, Population
FROM country
ORDER BY Population DESC
LIMIT 10;

-- Distinct Continents
SELECT DISTINCT Continent
FROM country;

-- Alias Example
SELECT Name AS Country_Name,
Population AS Total_Population
FROM country;

-- Insert Practice Country
INSERT INTO country
VALUES(
'XYZ',
'Clear Land',
'Asia'
'Virtual Region',
1000,
2026,
500000,
75.5,
500000.00,
500000.00,
'People',
'Republic',
9999,
'CG'
);

-- Verify Insert
SELECT *
FROM country
WHERE Code='XYZ';

-- Update Population
UPDATE country
SET Population=750000
WHERE Code='XYZ';

-- Verify Update
SELECT *
FROM country
WHERE Code='XYZ';

-- Add Column
ALTER TABLE country
ADD TourismScore DECIMAL(3,1);

DESC country;

-- Modify Column
ALTER TABLE country
MODIFY TourismScore DECIMAL(4,2);

-- Rename Column
ALTER TABLE country
RENAME COLUMN TourismScore
TO Tourism_Rating;

DESC country;

-- Drop Column
ALTER TABLE country
DROP COLUMN Tourism_Rating;

DESC country;

-- Delete Practice Country
DELETE
FROM country
WHERE Code='XYZ';

-- Verify Delete
SELECT *
FROM country
WHERE Code='XYZ';