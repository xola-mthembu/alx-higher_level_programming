-- 8-cities_of_california_subquery.sql: Lists all cities in California.

SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;

