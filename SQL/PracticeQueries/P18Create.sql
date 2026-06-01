-- CREATE DATABASE FOR HOSPITAL SYSTEM
CREATE DATABASE hospital_db;

-- SELECT THE DATABASE
USE hospital_db;

-- CREATE PATIENTS TABLE
-- This table stores patient details
CREATE TABLE patients (
    patient_id INT PRIMARY KEY,
    patient_name VARCHAR(100) NOT NULL,
    age INT,
    disease VARCHAR(100),
    admission_date DATE
);

-- VIEW TABLES INSIDE DATABASE
SHOW TABLES;

-- VIEW TABLE DESIGN
DESC patients;
