-- ============================================
-- CREATE DATABASE
-- ============================================

CREATE DATABASE cricket_tournament;

USE cricket_tournament;

-- ============================================
-- CREATE TABLE
-- ============================================

CREATE TABLE players (
    player_id INT PRIMARY KEY,
    player_name VARCHAR(100),
    team VARCHAR(50),
    runs INT
);

-- ============================================
-- INSERT DATA
-- ============================================

INSERT INTO players VALUES
(1, 'Virat Kohli', 'India', 75),
(2, 'Hardik Pandya', 'India', 60),
(3, 'Joe Root', 'England', 82);

-- ============================================
-- VIEW DATA
-- ============================================

SELECT * FROM players;

-- ============================================
-- UPDATE RUNS AFTER MATCH
-- ============================================

UPDATE players
SET runs = 110
WHERE player_id = 1;

-- ============================================
-- VIEW UPDATED DATA
-- ============================================

SELECT * FROM players;
