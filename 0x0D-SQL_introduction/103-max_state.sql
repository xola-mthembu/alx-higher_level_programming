-- Display the maximum temperature for each state, ordered by state name
SELECT SUBSTRING_INDEX(city, ',', -1) AS state, MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;

