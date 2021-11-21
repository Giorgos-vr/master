import sqlite3 as sl
from sqlite3 import Error
import os




file_path = os.path.join("data")
os.makedirs(file_path, exist_ok=True)
db = os.path.join(file_path, "pb.db")

def create_connection(db):
    """ create a database connection to a SQLite database """
    con = None
    try:
        con = sl.connect(db)
        return con
    except Error as e:
        print(e)
    return con

def create_table(con, pb_db):
    try:
        curs = con.cursor()
        curs.execute(pb_db)
    except Error as err:
        print(err)
    finally:
        if con is None:
            con.close()

def main():
    
    pb_db = """CREATE TABLE PB
        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        number_primary TEXT NOT NULL,
        number_secondary TEXT,
        email TEXT,
        anniversary DATE);"""

    con = create_connection(db)

    if con is not None:
        create_table(con, pb_db)

    else:
        print("Error!!!")


if __name__ == '__main__':
    main()