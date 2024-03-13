-- 7-cities.sql: Creates cities table in hbtn_0d_usa database with specified constraints.

-- Ensure the database exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database
USE hbtn_0d_usa;

-- Create the cities table only if it doesn't exist
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_state_id FOREIGN KEY (state_id) REFERENCES states(id)
);

