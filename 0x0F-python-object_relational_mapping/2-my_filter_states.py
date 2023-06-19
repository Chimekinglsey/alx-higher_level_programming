#!/usr/bin/python3
"""
This scripts takes four arguments and performs SQL operationsonthem
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    name_searched = argv[4]

    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
        port=3306, db=db_name)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY state.name =
    {}.format(name_searched) ORDER BY state.id"
    cursor.execute(query)
    result = cursor.all()
    for row in result:
        print(row)
    cursor.close()
    db.close()
