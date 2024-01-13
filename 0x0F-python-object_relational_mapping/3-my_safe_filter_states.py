#!/usr/bin/python3
"""Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument, but safe from MySQL
injections!"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(argv) != 5:
        sys.exit(1)
    else:
        # Get the arguments
        username = argv[1]
        password = argv[2]
        database = argv[3]
        state_name = argv[4]

        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )

        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        db.close()
