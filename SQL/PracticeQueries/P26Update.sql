-- ============================================
-- CREATE DATABASE
-- ============================================

CREATE DATABASE mobile_store;

USE mobile_store;

-- ============================================
-- CREATE TABLE
-- ============================================

CREATE TABLE mobiles (
    mobile_id INT PRIMARY KEY,
    brand VARCHAR(50),
    model VARCHAR(100),
    stock INT
);

-- ============================================
-- INSERT DATA
-- ============================================

INSERT INTO mobiles VALUES
(1, 'Samsung', 'Galaxy S25', 15),
(2, 'Apple', 'iPhone 16', 10),
(3, 'OnePlus', 'OnePlus 14', 20);

-- ============================================
-- VIEW DATA
-- ============================================

SELECT * FROM mobiles;

-- ============================================
-- UPDATE STOCK AFTER SALES
-- ============================================

UPDATE mobiles
SET stock = 8
WHERE mobile_id = 2;

-- ============================================
-- VIEW UPDATED DATA
-- ============================================

SELECT * FROM mobiles;
