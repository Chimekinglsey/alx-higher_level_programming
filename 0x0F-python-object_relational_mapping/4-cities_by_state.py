#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    argv = sys.argv
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(
        host='localhost',
        user=username, passwd=password,
        port=3306, db=db_name
        )
    cursor = db.cursor()
    query = "SELECT * FROM cities ORDER BY cities.id"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
