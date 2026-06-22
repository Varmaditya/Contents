CREATE DATABASE streaming_service;

USE streaming_service;

CREATE TABLE subscribers (
    subscriber_id INT PRIMARY KEY,
    subscriber_name VARCHAR(100),
    plan_type VARCHAR(30),
    remaining_days INT
);

INSERT INTO subscribers VALUES
(1,'Rohan','Premium',120),
(2,'Neha','Basic',45),
(3,'Aman','Premium',80),
(4,'Priya','Basic',60);

SELECT * FROM subscribers;

UPDATE subscribers
SET remaining_days = remaining_days + 30
WHERE plan_type = 'Premium';

UPDATE subscribers
SET remaining_days = remaining_days + 15
WHERE plan_type = 'Basic';

SELECT * FROM subscribers;
