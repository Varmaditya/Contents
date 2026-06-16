-- CREATE DATABASE FOR RESTAURANT
CREATE DATABASE restaurant_system;

USE restaurant_system;

-- CREATE MENU TABLE
CREATE TABLE menu_items (
    item_id INT PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(8,2),
    available BOOLEAN
);

-- INSERT MENU DATA
INSERT INTO menu_items VALUES
(101, 'Paneer Pizza', 'Main Course', 299.00, TRUE),
(102, 'Cold Coffee', 'Beverage', 120.00, TRUE),
(103, 'Chocolate Cake', 'Dessert', 180.00, FALSE),
(104, 'Pasta', 'Main Course', 140.00, TRUE),
(105, 'Ice-cream', 'Dessert', 80.00, FALSE);



-- VIEW ALL MENU ITEMS
SELECT * FROM menu_items;

-- VIEW ITEM NAME AND PRICE
SELECT item_name, price
FROM menu_items;
