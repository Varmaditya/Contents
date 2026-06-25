-- CREATE DATABASE
CREATE DATABASE shopping_orders;

USE shopping_orders;

-- CREATE ORDERS TABLE
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    product_name VARCHAR(100),
    quantity INT,
    order_status VARCHAR(30)
);

-- INSERT SAMPLE DATA
INSERT INTO orders VALUES
(101, 'Rahul', 'Laptop', 1, 'Delivered'),
(102, 'Priya', 'Smart Watch', 2, 'Cancelled'),
(103, 'Aman', 'Headphones', 1, 'Delivered'),
(104, 'Sneha', 'Keyboard', 1, 'Cancelled');

-- VIEW ALL ORDERS
SELECT * FROM orders;

-- DELETE CANCELLED ORDER
DELETE FROM orders
WHERE order_status = 'Cancelled';

-- VIEW UPDATED TABLE
SELECT * FROM orders;
