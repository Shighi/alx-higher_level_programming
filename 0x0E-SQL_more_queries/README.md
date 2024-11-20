0x0E. SQL - More Queries
This project focuses on advanced SQL queries, including joins, aggregate functions, and subqueries. The tasks aim to reinforce concepts of relational databases and data manipulation using MySQL.

Requirements
All SQL scripts should be executed using MySQL 8.0.
Each script should:
Be saved with a .sql file extension.
Run without any syntax errors.
Use a single SELECT statement (where applicable).
The database name will be passed as an argument to the mysql command.
Project Files
Task #	File	Description
0	0-privileges.sql	Lists all privileges of the MySQL users root and user.
1	1-create_user.sql	Creates a new MySQL user with specific privileges.
2	2-create_read_user.sql	Creates a MySQL user with SELECT privilege on a specific table.
3	3-force_name.sql	Creates a table that ensures a NOT NULL constraint on the name column.
4	4-never_empty.sql	Adds a default value of 'Unknown' to the name column of a table.
5	5-unique_id.sql	Creates a table with a unique constraint on the id column.
6	6-states.sql	Lists all rows from a states table sorted by id.
7	7-cities.sql	Lists all rows from a cities table sorted by id.
8	8-cities_of_california.sql	Lists all cities of California.
9	9-cities_by_state.sql	Lists all cities with their corresponding state.
10	10-genre_id_all_shows.sql	Lists all TV shows and their genres.
11	11-genre_id_all_shows.sql	Lists all TV shows and their genre IDs.
12	12-no_genre.sql	Lists all TV shows without any genre linked.
13	13-count_shows_by_genre.sql	Displays the number of TV shows linked to each genre.
14	14-my_genres.sql	Lists all genres associated with the TV show Dexter.
15	15-comedy_only.sql	Lists all TV shows in the Comedy genre.
16	16-shows_by_genre.sql	Lists all TV shows with their corresponding genres (or NULL if no genre).
Usage
To execute a script, use the following command:

bash

mysql -hlocalhost -uroot -p database_name < script_name.sql
Replace database_name with the name of your database.
Replace script_name.sql with the specific script file, e.g., 0-privileges.sql.
Learning Objectives
By completing this project, you should be able to:

Understand and apply SQL concepts such as:
Constraints (NOT NULL, DEFAULT, UNIQUE).
User privileges and management.
Joins and subqueries.
Work with advanced MySQL features like:
Aggregate functions (COUNT, SUM, AVG).
Data sorting and grouping.
Query and manipulate data efficiently in relational databases.
Author
Shighi 
