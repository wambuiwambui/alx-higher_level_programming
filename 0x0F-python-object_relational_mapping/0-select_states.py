#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) == 4:
        # Open database connection
        db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
        
        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # execute SQL query using execute() method.
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch a single row using fetchone() method.
        rows = cursor.fetchall()

        # Iterate through the rows and print the results
        for row in rows:
            print(row)

        # disconnect from server
        db.close()
    else:
        print("Usage: {} username password database".format(sys.argv[0]))
