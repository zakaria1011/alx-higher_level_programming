#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def filter_states(username, password, database):
    """Filter and display states with names starting with N."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    username, password, database = sys.argv[1:4]
    filter_states(username, password, database)
