CREATE DATABASE promotions_db;

USE promotions_db;

CREATE TABLE staff (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    designation VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2)
);

INSERT INTO staff VALUES
(101,'Rahul','Developer','IT',50000),
(102,'Priya','Executive','Sales',45000);

SELECT * FROM staff;

UPDATE staff
SET
    designation = 'Senior Developer',
    salary = 70000,
    department = 'Technology'
WHERE employee_id = 101;

SELECT * FROM staff;
