#!/usr/bin/python3
"""We are importing MySQLdb module from Python library to aid our
        transactions"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(
        host='localhost', user=username, passwd=password,
        port=3306, db=db_name)
    curs = db.cursor()

    select_query = "SELECT * FROM states WHERE BINARY name LIKE 'N%'"
    curs.execute(select_query)
    result = curs.fetchall()
    for row in result:
        print(row)
    curs.close()
    db.close()
