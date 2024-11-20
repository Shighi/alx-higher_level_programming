-- Use the correct database
USE hbtn_0c_0;

-- Display the maximum temperature for each state in the table temperatures
-- Results are sorted by state name in ascending order
SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
