-- MODIFYING A UNIVERSITY DATABASE
CREATE DATABASE university_portal;

USE university_portal;

CREATE TABLE faculty(
    faculty_id INT PRIMARY KEY,
    faculty_name VARCHAR(100),
    department VARCHAR(50),
    qualification VARCHAR(50),
    salary DECIMAL(10,2),
    joining_date DATE
);

INSERT INTO faculty VALUES
(101,'Dr. Sharma','Computer Science','PhD',90000,'2018-05-10'),
(102,'Dr. Mehta','Physics','PhD',85000,'2017-08-22'),
(103,'Dr. Khan','Mathematics','M.Tech',78000,'2020-02-14'),
(104,'Dr. Patel','Chemistry','PhD',88000,'2019-01-30'),
(105,'Dr. Verma','English','MA',65000,'2021-07-18');

SELECT * FROM faculty;

DESC faculty;

-- ADD EMAIL & EXPERIENCE
ALTER TABLE faculty
ADD email VARCHAR(100);

ALTER TABLE faculty
ADD experience INT;

DESC faculty;

-- UPDATE EXPERIENCE
UPDATE faculty SET experience=8 WHERE faculty_id=101;
UPDATE faculty SET experience=10 WHERE faculty_id=102;
UPDATE faculty SET experience=5 WHERE faculty_id=103;
UPDATE faculty SET experience=7 WHERE faculty_id=104;
UPDATE faculty SET experience=4 WHERE faculty_id=105;

SELECT * FROM faculty;

-- MODIFY QUALIFICATION
ALTER TABLE faculty
MODIFY qualification VARCHAR(100);

DESC faculty;

-- RENAME COLUMN
ALTER TABLE faculty
RENAME COLUMN faculty_name
TO professor_name;

DESC faculty;

-- REMOVE JOINING DATE
ALTER TABLE faculty
DROP COLUMN joining_date;

SELECT * FROM faculty;

-- ADD OFFICE NUMBER
ALTER TABLE faculty
ADD office_no VARCHAR(20);

DESC faculty;

-- RENAME TABLE
ALTER TABLE faculty
RENAME TO professors;

SHOW TABLES;

SELECT * FROM professors;

TRUNCATE TABLE professors;

SELECT * FROM professors;

DROP TABLE professors;

SHOW TABLES;

DROP DATABASE university_portal;
