-- 2-create_read_user.sql: Creates hbtn_0d_2 database and user_0d_2 with SELECT privileges.

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Drop the user if it exists to reset privileges (won't cause an error if the user doesn't exist)
DROP USER IF EXISTS 'user_0d_2'@'localhost';

-- Create the user with the specified password
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege on the hbtn_0d_2 database to the user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the changes immediately
FLUSH PRIVILEGES;

