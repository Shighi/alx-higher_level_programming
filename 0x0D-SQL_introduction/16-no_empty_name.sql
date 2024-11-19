-- Lists all records from second_table where name is not NULL or empty
SELECT id, name, score FROM second_table WHERE name IS NOT NULL AND name != '';
