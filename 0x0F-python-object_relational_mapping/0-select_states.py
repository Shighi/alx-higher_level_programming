#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    try:
        # Connect to the MySQL database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )
        
        # Create a cursor object to interact with the database
        cur = db.cursor()
        
        # Execute the SQL query to fetch all states ordered by id
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        
        # Fetch and print all the rows
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as err:
        # Print any errors that occur during database operations
        print(f"Error: {err}")
    finally:
        # Ensure resources are closed
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()

