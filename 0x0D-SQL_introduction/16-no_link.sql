-- List all records with a name value in the table second_table
-- Results are sorted by score in descending order
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
