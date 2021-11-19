import sqlite3 as sl

con = sl.connect('pb.db')

with con:
    con.execute ("""
    CREATE TABLE PB (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        number_primary TEXT,
        number_secondary TEXT,
        email TEXT,
        anniversary DATE
    ) ;
    """)

