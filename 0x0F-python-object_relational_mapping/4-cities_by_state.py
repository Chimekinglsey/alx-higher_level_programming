#!/usr/bin/python3
"""
We are using INNER JOIN. First we select the colums we want to return, in this
case, cities.id, cities.name, states.name FROM the tables containing these
columns which is `cities` but state name is found in states table. So, we have
to use INNER JOIN  `states` but what we want from states table is the column
where the state_id column in cities matches with `id` column in states
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(host='localhost',
                         user=username, passwd=password,
                         port=3306, db=db_name)
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name\
                           FROM cities INNER JOIN states\
                           ON cities.state_id=states.id\
                           ORDER BY cities.id;"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
