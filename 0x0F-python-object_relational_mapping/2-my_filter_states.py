#!/usr/bin/python3
""" state that match the arg """
import MySQLdb
import sys
if __name__ == "__main__":

    username, password, database, state_name = sys.argv[1:]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    cursor = db.cursor()

    query = ("SELECT * FROM states "
             "WHERE name = '{}' "
             "ORDER BY states.id ASC".format(state_name))

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
