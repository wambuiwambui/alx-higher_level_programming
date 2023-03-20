#!/usr/bin/python3
"""
This script lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Take arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Use a prepared statement to safely search for state names
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the matching rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

