-- List the number of records for each score in the table second_table
-- Results are sorted by the number of records in descending order
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
