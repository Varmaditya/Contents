CREATE DATABASE store_pricing;

USE store_pricing;

CREATE TABLE inventory (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2)
);

INSERT INTO inventory VALUES
(1,'Laptop','Electronics',60000),
(2,'Mouse','Accessories',500),
(3,'Keyboard','Accessories',1200),
(4,'Monitor','Electronics',15000);

SELECT * FROM inventory;

UPDATE inventory
SET price = price * 1.15
WHERE category = 'Electronics';

UPDATE inventory
SET price = price * 1.08
WHERE category = 'Accessories';

SELECT * FROM inventory;
