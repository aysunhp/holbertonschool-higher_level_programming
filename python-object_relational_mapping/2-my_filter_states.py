#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # 4 arguments: mysql username, mysql password, database name, state name
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # SQL query with user input using format
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC;".format(state_name)
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
