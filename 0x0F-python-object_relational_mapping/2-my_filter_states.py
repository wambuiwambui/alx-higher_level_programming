#!/usr/bin/python3


import MySQLdb
import sys

# connect to MySQL server
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
state_name = sys.argv[4]
db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query to retrieve all states matching the input name
query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)
cursor.execute(query)

# fetch all rows and print the data
rows = cursor.fetchall()
for row in rows:
    print(row)

# disconnect from server
db.close()
