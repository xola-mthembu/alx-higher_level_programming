-- 3-force_name.sql: Creates table force_name if it doesn't already exist.

-- Create the table only if it doesn't exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);

