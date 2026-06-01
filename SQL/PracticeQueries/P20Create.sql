-- CREATE DATABASE FOR COMPANY EMPLOYEES
CREATE DATABASE company_db;

-- SELECT DATABASE
USE company_db;

-- CREATE EMPLOYEES TABLE
-- This table stores employee information
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    joining_date DATE,
    email VARCHAR(100) UNIQUE
);

-- VIEW ALL TABLES INSIDE DATABASE
SHOW TABLES;

-- VIEW TABLE STRUCTURE
DESC employees;
