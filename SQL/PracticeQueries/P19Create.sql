-- CREATE DATABASE FOR MOVIE PLATFORM
CREATE DATABASE movies_db;

-- USE THE DATABASE
USE movies_db;

-- CREATE MOVIES TABLE
-- This table stores movie details
CREATE TABLE movies (
    movie_id INT PRIMARY KEY,
    movie_name VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    release_date DATE,
    rating DECIMAL(3,1)
);

-- SHOW ALL TABLES
SHOW TABLES;

-- DISPLAY TABLE STRUCTURE
DESC movies;
