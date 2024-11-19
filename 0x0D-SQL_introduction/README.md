0x0D. SQL - Introduction
This project is part of the ALX Software Engineering Program and introduces SQL and basic database operations. Below is a summary of the tasks, their purpose, and the SQL scripts involved.

Learning Objectives
By completing this project, you will learn:

What a database is and why it’s important.
What SQL stands for and its uses.
Common SQL commands such as SELECT, INSERT, UPDATE, DELETE, etc.
How to perform simple queries and manipulate data in a relational database.
Requirements
All scripts are written for MySQL 8.0.
SQL scripts are executable using:
bash

cat [filename.sql] | mysql -hlocalhost -uroot -p [database_name]
Files should start with a comment explaining the script’s functionality.
Tasks
Mandatory Tasks
0. List databases
Description: Lists all databases on a MySQL server.
Script: 0-list_databases.sql
1. Create a database
Description: Creates a new database named hbtn_0c_0.
Script: 1-create_database_if_missing.sql
2. Delete a database
Description: Deletes the database hbtn_0c_0 if it exists.
Script: 2-remove_database.sql
3. List tables
Description: Lists all tables in a given database.
Script: 3-list_tables.sql
4. First table
Description: Creates a new table first_table with id and name columns.
Script: 4-first_table.sql
5. Full description
Description: Displays the full structure of first_table.
Script: 5-full_table.sql
6. List all in table
Description: Lists all rows in the table first_table.
Script: 6-list_values.sql
7. Insert value
Description: Inserts a new row into first_table.
Script: 7-insert_value.sql
8. Count 89
Description: Counts all rows in first_table with an id equal to 89.
Script: 8-count_89.sql
9. Full creation
Description: Creates a new table second_table with multiple columns.
Script: 9-full_creation.sql
10. List by best
Description: Lists all rows in second_table, ordered by score in descending order.
Script: 10-top_score.sql
11. Select the best
Description: Selects only the rows with the highest score in second_table.
Script: 11-best_score.sql
12. Cheating is bad
Description: Updates the name of a row with id = 89 to BestSchool.
Script: 12-no_cheating.sql
Advanced Tasks
13. Delete record
Description: Deletes rows from second_table where the score is less than or equal to 5.
Script: 13-delete_records.sql
14. Average
Description: Calculates the average score of all rows in second_table.
Script: 14-average.sql
15. Number by score
Description: Displays the number of rows for each score in second_table.
Script: 15-group_by_score.sql
16. Say my name
Description: Lists all rows from second_table where name is not NULL or empty.
Script: 16-no_empty_name.sql
17. Go to UTF8
Description: Converts the character set of second_table to utf8mb4.
Script: 17-change_charset.sql
18. Temperatures #0
Description: Creates a table temperatures to store city temperature data.
Script: 18-temperatures.sql
19. Temperatures #1
Description: Inserts multiple rows of data into the temperatures table.
Script: 19-temperatures_data.sql
20. Temperatures #2
Description: Lists cities with their average summer temperature, sorted in descending order.
Script: 20-summer_temperatures.sql

Usage
Clone this repository:
bash
git clone https://github.com/Shighi/alx-higher_level_programming.git
Navigate to the directory:
bash

cd alx-higher_level_programming/0x0D-SQL_introduction
Execute any script by running:
bash

cat [script_name].sql | mysql -hlocalhost -uroot -p [database_name]

Author
This project was completed as part of the ALX Software Engineering Program. Authored by Shighi.

Feel free to customize this further based on your preferences!

