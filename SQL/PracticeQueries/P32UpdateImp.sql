CREATE DATABASE warning_demo;

USE warning_demo;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary INT
);

INSERT INTO employees VALUES
(1,'Aman',50000),
(2,'Priya',60000),
(3,'Rahul',70000);

SELECT * FROM employees;

UPDATE employees
SET salary = 100000;

SELECT * FROM employees;
