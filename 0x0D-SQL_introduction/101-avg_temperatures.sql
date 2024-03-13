-- Create the table 'temperatures' if it doesn't exist
CREATE TABLE IF NOT EXISTS temperatures (
  city VARCHAR(256),
  avg_temp DECIMAL(6, 4)
);

-- Insert the temperature data into the 'temperatures' table
INSERT INTO temperatures (city, avg_temp) VALUES
  ('Tucson', 126.2941),
  ('Pismo beach', 94.5196),
  ('San Jose', 84.0833),
  ('Phoenix', 83.7010),
  ('Sonoma', 81.4804),
  ('San Francisco', 72.5588),
  ('Peoria', 65.4118),
  ('Naperville', 57.3186),
  ('Chicago', 42.0098);

-- Query the 'temperatures' table to retrieve the city and avg_temp columns
SELECT city, avg_temp FROM temperatures ORDER BY avg_temp DESC;

