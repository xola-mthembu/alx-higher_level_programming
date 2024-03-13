-- 1-create_user.sql: Creates user_0d_1 with all privileges and a specified password.

-- Attempt to drop the user if it already exists (won't cause an error if the user doesn't exist)
DROP USER IF EXISTS 'user_0d_1'@'localhost';

-- Create the user with the specified password
CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply the changes immediately
FLUSH PRIVILEGES;

