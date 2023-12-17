#!/usr/bin/python3
"""a script that lists all states with a name
    matching the argument from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    curs = conn.cursor()
    curs.execute("SELECT * FROM states WHERE name LIKE %s", (sys.argv[4], ))
    query_row = curs.fetchall()
    for row in query_row:
        print(row)

    curs.close()
    conn.close()
