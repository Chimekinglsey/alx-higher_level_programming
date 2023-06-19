#!/usr/bin/python3
import MySQLdb
from sys import argv

"""We are importing MySQLdb module from Python library to aid our
        transactions"""
if __name__ == '__main__':
    user = argv[1]
    password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(
        host='localhost', user=user, passwd=password,
        port=3306, db=db_name)
    curs = db.cursor()

    select_query = "SELECT * FROM states ORDER BY id ASC"
    curs.execute(select_query)
    result = curs.fetchall()
    for row in result:
        print(row)
    curs.close()
    db.close()
