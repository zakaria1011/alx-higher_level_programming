#!/usr/bin/python3
"""Script to list all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def list_states(username, password, database):
    """List all states from the database hbtn_0e_0_usa"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
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
    list_states(username, password, database)
