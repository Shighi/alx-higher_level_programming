-- Display the top 3 cities with the highest temperatures during July and August
-- Results are sorted by average temperature in descending order
SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE month IN ('July', 'August')
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
