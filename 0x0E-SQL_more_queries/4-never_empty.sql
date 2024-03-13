-- 4-never_empty.sql: Creates table id_not_null with specific default and non-null constraints.

-- Create the table only if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);

