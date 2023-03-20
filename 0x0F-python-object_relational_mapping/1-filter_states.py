#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    username, password, db_name = sys.argv[1:]

    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=db_name,
        port=3306)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

