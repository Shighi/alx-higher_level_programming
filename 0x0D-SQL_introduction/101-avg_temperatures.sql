-- Display the average temperature for each city in the table temperatures
-- Results are sorted by average temperature in descending order
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
