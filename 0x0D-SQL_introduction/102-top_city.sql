-- Display the top 3 cities with the highest average temperature in July and August
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(measure_date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

