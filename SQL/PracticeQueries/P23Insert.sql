-- CREATE DATABASE FOR AIRLINE
CREATE DATABASE airline_booking;

USE airline_booking;

-- CREATE FLIGHTS TABLE
CREATE TABLE flights (
    flight_id INT PRIMARY KEY,
    airline_name VARCHAR(100),
    source_city VARCHAR(50),
    destination_city VARCHAR(50),
    ticket_price DECIMAL(10,2)
);

-- INSERT FLIGHT DATA
INSERT INTO flights VALUES
(501, 'IndiGo', 'Mumbai', 'Delhi', 6500.00),
(502, 'Air India', 'Bangalore', 'Kolkata', 7200.00),
(503, 'Vistara', 'Chennai', 'Hyderabad', 4800.00);

-- VIEW ALL FLIGHTS
SELECT * FROM flights;

-- VIEW AIRLINE NAME AND PRICE
SELECT airline_name, ticket_price
FROM flights;
