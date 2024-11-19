-- Lists all cities with average temperature during Summer, sorted by temperature DESC
SELECT city, country, average_temperature 
FROM temperatures 
WHERE season = 'Summer' 
ORDER BY average_temperature DESC;
