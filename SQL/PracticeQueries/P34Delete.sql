-- CREATE DATABASE
CREATE DATABASE university_records;

USE university_records;

-- CREATE STUDENT TABLE
CREATE TABLE university_students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100),
    course VARCHAR(50),
    semester INT,
    status VARCHAR(20)
);

-- INSERT SAMPLE DATA
INSERT INTO university_students VALUES
(1, 'Arjun', 'Computer Science', 4, 'Active'),
(2, 'Neha', 'Mechanical', 2, 'Dropped'),
(3, 'Rohan', 'Electronics', 6, 'Active'),
(4, 'Priya', 'Civil', 3, 'Dropped'),
(5, 'Amit', 'Computer Science', 8, 'Graduated');

-- VIEW STUDENT RECORDS
SELECT * FROM university_students;

-- DELETE DROPPED STUDENTS
DELETE FROM university_students
WHERE status = 'Dropped';

-- VIEW UPDATED RECORDS
SELECT * FROM university_students;
