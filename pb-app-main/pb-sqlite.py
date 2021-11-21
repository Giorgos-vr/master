import sqlite3 as sl
from sqlite3 import Error
import os


file_path = os.path.join("data")
os.makedirs(file_path, exist_ok=True)
db = os.path.join(file_path, "pb.db")
con = sl.connect(db)


#with con:
    #con.execute ("""
    #CREATE TABLE PB (
        #id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        #name TEXT,
        #number_primary TEXT,
        #number_secondary TEXT,
        #email TEXT,
        #anniversary DATE
    #) ;
    #""")

#sql = 'INSERT INTO PB (id, name, number_primary, number_secondary, email, anniversary) values (?, ?, ?, ?, ?, ?)'
#data = [(1, 'Bob', '001', '0001','bob@mail.com', '2021-01-01'), (2, 'Mike', '002', '0002', 'mike@mail.com', '2020-01-30')]

#with con:
    #con.executemany(sql, data)

with con:
    data = con.execute('SELECT * FROM pb WHERE id <= 3')
    for row in data:
        print(row)