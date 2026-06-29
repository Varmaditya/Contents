-- MODIFYING A HOSPITAL DATABASE
-- CREATE DATABASE
CREATE DATABASE hospital_care;

USE hospital_care;

-- CREATE PATIENT TABLE
CREATE TABLE patients(
    patient_id INT PRIMARY KEY,
    patient_name VARCHAR(100) NOT NULL,
    age INT,
    gender CHAR(1),
    disease VARCHAR(100),
    doctor_name VARCHAR(100),
    admission_date DATE
);

-- INSERT SAMPLE DATA
INSERT INTO patients VALUES
(101,'Rahul Sharma',32,'M','Fever','Dr. Mehta','2025-01-15'),
(102,'Priya Patel',26,'F','Diabetes','Dr. Shah','2025-02-11'),
(103,'Aman Verma',45,'M','Hypertension','Dr. Khan','2025-03-10'),
(104,'Sneha Gupta',38,'F','Asthma','Dr. Shah','2025-04-08'),
(105,'Rohan Singh',29,'M','Migraine','Dr. Kumar','2025-05-05');

SELECT * FROM patients;

DESC patients;

-- ADD EMAIL AND PHONE
ALTER TABLE patients
ADD email VARCHAR(100);

ALTER TABLE patients
ADD phone VARCHAR(15);

DESC patients;

-- UPDATE NEW DETAILS
UPDATE patients
SET email='rahul@gmail.com',
phone='9876543210'
WHERE patient_id=101;

UPDATE patients
SET email='sneha@gmail.com',
phone='9123456789'
WHERE patient_id=104;

UPDATE patients
SET email='rohan@gmail.com',
phone='9011223344'
WHERE patient_id=105;

SELECT * FROM patients;

-- MODIFY PHONE SIZE
ALTER TABLE patients
MODIFY phone VARCHAR(20);

DESC patients;

-- RENAME COLUMN
ALTER TABLE patients
RENAME COLUMN doctor_name
TO consulting_doctor;

DESC patients;

-- DROP GENDER COLUMN
ALTER TABLE patients
DROP COLUMN gender;

SELECT * FROM patients;

-- ADD BLOOD GROUP
ALTER TABLE patients
ADD blood_group CHAR(3);

DESC patients;

-- RENAME TABLE
ALTER TABLE patients
RENAME TO hospital_patients;

SHOW TABLES;

SELECT * FROM hospital_patients;

-- REMOVE ALL RECORDS
TRUNCATE TABLE hospital_patients;

SELECT * FROM hospital_patients;

-- DELETE TABLE
DROP TABLE hospital_patients;

SHOW TABLES;

DROP DATABASE hospital_care;
