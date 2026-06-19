-- ============================================
-- CREATE DATABASE
-- ============================================

CREATE DATABASE hotel_reservation;

USE hotel_reservation;

-- ============================================
-- CREATE TABLE
-- ============================================

CREATE TABLE rooms (
    room_id INT PRIMARY KEY,
    guest_name VARCHAR(100),
    room_type VARCHAR(50),
    nights INT
);

-- ============================================
-- INSERT DATA
-- ============================================

INSERT INTO rooms VALUES
(101, 'Arjun', 'Standard', 2),
(102, 'Sneha', 'Deluxe', 3),
(103, 'Karan', 'Suite', 1);

-- ============================================
-- VIEW DATA
-- ============================================

SELECT * FROM rooms;

-- ============================================
-- UPGRADE ROOM TYPE
-- ============================================

UPDATE rooms
SET room_type = 'Premium Deluxe'
WHERE room_id = 102;

-- ============================================
-- VIEW UPDATED DATA
-- ============================================

SELECT * FROM rooms;
