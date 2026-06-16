-- CREATE DATABASE FOR LIBRARY
CREATE DATABASE library_system;

USE library_system;

-- CREATE BOOKS TABLE
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    author VARCHAR(100),
    genre VARCHAR(50),
    publish_year INT
);

-- INSERT BOOK DATA
INSERT INTO books VALUES
(1, 'Atomic Habits', 'James Clear', 'Self Help', 2018),
(2, 'The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 1937),
(3, 'Clean Code', 'Robert Martin', 'Programming', 2008);

-- VIEW ALL BOOKS
SELECT * FROM books;

-- VIEW BOOK TITLE AND AUTHOR
SELECT title, author
FROM books;
