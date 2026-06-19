-- ============================================
-- CREATE DATABASE
-- ============================================

CREATE DATABASE movie_booking;

USE movie_booking;

-- ============================================
-- CREATE TABLE
-- ============================================

CREATE TABLE tickets (
    ticket_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    movie_name VARCHAR(100),
    seat_no VARCHAR(10),
    price DECIMAL(8,2)
);

-- ============================================
-- INSERT DATA
-- ============================================

INSERT INTO tickets VALUES
(1, 'Rahul', 'Avengers', 'A12', 250.00),
(2, 'Priya', 'Interstellar', 'B05', 300.00),
(3, 'Aman', 'Inception', 'C10', 280.00);

-- ============================================
-- VIEW ORIGINAL DATA
-- ============================================

SELECT * FROM tickets;

-- ============================================
-- UPDATE PRICE OF TICKET 1
-- ============================================

UPDATE tickets
SET price = 350.00
WHERE ticket_id = 1;

-- ============================================
-- VIEW UPDATED DATA
-- ============================================

SELECT * FROM tickets;
