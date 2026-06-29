-- STEP 1 : CREATE DATABASE
CREATE DATABASE corporate_system;

USE corporate_system;

-- STEP 2 : CREATE EMPLOYEE TABLE
CREATE TABLE employees(
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department VARCHAR(50),
    designation VARCHAR(50),
    salary DECIMAL(10,2),
    joining_date DATE
);

-- STEP 3 : INSERT SAMPLE DATA
INSERT INTO employees VALUES
(101,'Rahul Sharma','IT','Developer',65000,'2022-05-14'),
(102,'Priya Patel','HR','Executive',45000,'2021-09-10'),
(103,'Aman Verma','Finance','Accountant',52000,'2023-01-18'),
(104,'Sneha Kapoor','IT','Tester',48000,'2022-11-08'),
(105,'Rohan Mehta','Sales','Manager',72000,'2020-07-22');

-- VIEW ORIGINAL TABLE
SELECT * FROM employees;

DESC employees;

-- STEP 4 : ADD NEW COLUMNS
-- Company now wants Email and Phone Number
ALTER TABLE employees
ADD email VARCHAR(100);

ALTER TABLE employees
ADD phone VARCHAR(15);

DESC employees;

-- STEP 5 : UPDATE NEW COLUMNS
UPDATE employees
SET email='rahul@company.com',
phone='9876543210'
WHERE employee_id=101;

UPDATE employees
SET email='priya@company.com',
phone='9123456789'
WHERE employee_id=102;

UPDATE employees
SET email='aman@company.com',
phone='9988776655'
WHERE employee_id=103;

SELECT * FROM employees;

-- STEP 6 : MODIFY DATATYPE
-- Company decides phone numbers should support
-- international numbers.
ALTER TABLE employees
MODIFY phone VARCHAR(20);

DESC employees;

-- STEP 7 : RENAME COLUMN
-- HR wants employee_name to become full_name
ALTER TABLE employees
RENAME COLUMN employee_name
TO full_name;

DESC employees;

SELECT * FROM employees;

-- STEP 8 : DROP COLUMN
-- Company no longer stores Designation
ALTER TABLE employees
DROP COLUMN designation;

DESC employees;

SELECT * FROM employees;

-- STEP 9 : ADD ANOTHER COLUMN
-- Store Employee Experience
ALTER TABLE employees
ADD experience INT;

DESC employees;

-- STEP 10 : UPDATE EXPERIENCE
UPDATE employees
SET experience=3
WHERE employee_id=101;

UPDATE employees
SET experience=4
WHERE employee_id=102;

UPDATE employees
SET experience=6
WHERE employee_id=105;

SELECT * FROM employees;

-- STEP 11 : RENAME TABLE
ALTER TABLE employees
RENAME TO company_staff;

SHOW TABLES;

SELECT * FROM company_staff;

-- STEP 12 : REMOVE ALL RECORDS
-- Table remains
TRUNCATE TABLE company_staff;

SELECT * FROM company_staff;

-- STEP 13 : DELETE TABLE
DROP TABLE company_staff;

SHOW TABLES;

-- STEP 14 : DELETE DATABASE
DROP DATABASE corporate_system;
