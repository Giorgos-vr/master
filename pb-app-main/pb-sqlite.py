import sqlite3 as sl
from sqlite3 import Error
import os


file_path = os.path.join("data")
os.makedirs(file_path, exist_ok=True)
db = os.path.join(file_path, "pb.db")


def create_db(db):
    conn = None
    try:
        conn = sl.connect(db)
        with conn:
            conn.execute ("""
            CREATE TABLE PB (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                number_primary TEXT NOT NULL,
                number_secondary TEXT,
                email TEXT,
                anniversary DATE
            ) ;
            """)
    except Error:
        pass
    finally:
        if conn:
            conn.close()

        

def create_connection(db):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sl.connect(db)
        data = conn.execute('SELECT * FROM pb WHERE id <= 3')
        for row in data:
            print(row)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_db(db)
    create_connection(db)


#sql = 'INSERT INTO PB (id, name, number_primary, number_secondary, email, anniversary) values (?, ?, ?, ?, ?, ?)'
#data = [(1, 'Bob', '001', '0001','bob@mail.com', '2021-01-01'), (2, 'Mike', '002', '0002', 'mike@mail.com', '2020-01-30')]

#with conn:
    #conn.executemany(sql, data)

