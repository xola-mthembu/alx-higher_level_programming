-- 5-unique_id.sql: Creates table unique_id with id as unique and a default value.

-- Create the table only if it doesn't exist
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);

