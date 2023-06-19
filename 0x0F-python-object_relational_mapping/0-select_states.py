#!/usr/bin/python3
import MySQLdb
from sys import argv

"""We are importing MySQLdb module from Python library to aid our
        transactions"""
user = argv[1]
password = argv[2]
db_name = argv[3]

db = MySQLdb.connect(
    host='localhost', user=user, passwd=password,
    port=3306, db=db_name)
curs = db.cursor()

select_query = "SELECT * FROM states ORDER BY id ASC"
result = cursor.execute(select_query).fetchall()
for row in result:
    print(row)
cursor.close()
db.close()
