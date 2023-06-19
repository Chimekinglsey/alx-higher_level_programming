#!/usr/bin/python3
"""
This scripts takes four arguments and performs
SQL operations on them
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    name_searched = argv[4]

    db = MySQLdb.connect(
        host='localhost', user=username, passwd=password,
        port=3306, db=db_name
    )
    cursor = db.cursor()

    query = "SELECT cities.name FROM cities INNER JOIN states ON \
        cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id"
  store =  cursor.execute(query, (name_searched,))

    result = cursor.fetchall()
    counter = 1
    for row in result:
        print(row[0], end='')
        if counter < store:
            print(end=', ')
        counter += 1
    print("")

    cursor.close()
    db.close()
