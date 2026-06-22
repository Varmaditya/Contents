-- CREATE DATABASE
CREATE DATABASE salary_revision;

USE salary_revision;

-- CREATE TABLE
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department VARCHAR(50),
    salary DECIMAL(10,2)
);

-- INSERT DATA
INSERT INTO employees VALUES
(101,'Rahul','IT',50000),
(102,'Priya','HR',45000),
(103,'Aman','IT',60000),
(104,'Neha','Sales',55000),
(105,'Karan','HR',48000);

-- VIEW BEFORE UPDATE
SELECT * FROM employees;

-- INCREASE IT SALARIES BY 10%
UPDATE employees
SET salary = salary * 1.10
WHERE department = 'IT';

-- INCREASE HR SALARIES BY 5%
UPDATE employees
SET salary = salary * 1.05
WHERE department = 'HR';

-- VIEW AFTER UPDATE
SELECT * FROM employees;
