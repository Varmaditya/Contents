-- CREATE DATABASE
CREATE DATABASE hotel_management;

USE hotel_management;

-- CREATE BOOKINGS TABLE
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY,
    guest_name VARCHAR(100),
    room_number INT,
    booking_date DATE,
    payment_status VARCHAR(20)
);

-- INSERT SAMPLE DATA
INSERT INTO bookings VALUES
(201, 'Rahul Sharma', 101, '2025-07-01', 'Paid'),
(202, 'Anjali Patel', 102, '2025-07-02', 'Pending'),
(203, 'Karan Singh', 103, '2025-07-03', 'Paid'),
(204, 'Sneha Gupta', 104, '2025-07-04', 'Cancelled'),
(205, 'Rohit Verma', 105, '2025-07-05', 'Pending');

-- VIEW ALL BOOKINGS
SELECT * FROM bookings;

-- DELETE CANCELLED BOOKINGS
DELETE FROM bookings
WHERE payment_status = 'Cancelled';

-- VIEW UPDATED BOOKINGS
SELECT * FROM bookings;
