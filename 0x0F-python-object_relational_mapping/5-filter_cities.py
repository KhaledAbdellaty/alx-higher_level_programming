#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_0_usa."""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])

    curs = conn.cursor()
    curs.execute('''SELECT cities.id, cities.name, states.name FROM
                 cities INNER JOIN states ON states.id=cities.state_id WHERE
                 states.name=%s ORDER BY cities.id ASC''', (sys.argv[4], ))
    query_row = curs.fetchall()
    for row in query_row:
        print(row[1], end=", ")
    print()

    curs.close()
    conn.close()
