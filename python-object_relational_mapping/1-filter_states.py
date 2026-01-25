#!/usr/bin/python3
"""
List all states with a name starting with N (upper case)
from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    query = """
        SELECT * FROM states
        WHERE BINARY name LIKE 'N%'
        ORDER BY id ASC
    """

    cursor.execute(query)

    for row in cursor:
        print(row)

    cursor.close()
    db.close()
