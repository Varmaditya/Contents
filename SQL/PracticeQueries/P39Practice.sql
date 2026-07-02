-- Select Database
USE world;

-- View Complete Table
SELECT *
FROM city;

-- View Selected Columns
SELECT Name, District, Population
FROM city;

-- Indian Cities
SELECT *
FROM city
WHERE CountryCode='IND';

-- Cities With Large Population
SELECT Name, Population
FROM city
WHERE Population > 5000000;

-- Sort Cities
SELECT Name, Population
FROM city
ORDER BY Population DESC
LIMIT 15;

-- Distinct Country Codes
SELECT DISTINCT CountryCode
FROM city;

-- Alias Example
SELECT Name AS City_Name,
District AS State_Name
FROM city;

-- Insert Practice City
INSERT INTO city
VALUES(
5000,
'Mega City',
'IND',
'Maharashtra',
100000
);

-- Verify Insert
SELECT *
FROM city
WHERE ID=5000;

-- Update Population
UPDATE city
SET Population=250000
WHERE ID=5000;

-- Verify Update
SELECT *
FROM city
WHERE ID=5000;

-- Add Column
ALTER TABLE city
ADD Metro VARCHAR(20);

DESC city;

-- Modify Column
ALTER TABLE city
MODIFY Metro VARCHAR(50);

-- Rename Column
ALTER TABLE city
RENAME COLUMN Metro
TO Metro_System;

DESC city;

-- Drop Column
ALTER TABLE city
DROP COLUMN Metro_System;

DESC city;

-- Delete Practice City
DELETE
FROM city
WHERE ID=5000;

-- Verify Delete
SELECT *
FROM city
WHERE ID=5000;

-- Remove All Records (Practice Only)
TRUNCATE TABLE city;

-- Verify Table
SELECT *
FROM city;