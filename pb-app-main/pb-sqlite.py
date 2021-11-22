import sqlite3 as sl
from sqlite3 import Error
import os




file_path = os.path.join("data")
os.makedirs(file_path, exist_ok=True)
db = os.path.join(file_path, "pb.db")

def create_connection(db):
    #create a database connection to a SQLite database
    con = None
    try:
        con = sl.connect(db)
        return con
    except Error as e:
        print(e)
    return con

def create_table(con, db):
    try:
        curs = con.cursor()
        curs.execute(db)
    except Error as err:
        print(err)
    finally:
        if con is None:
            con.close()

def add_data(con, db):

    sql = ''' INSERT INTO PB(name,number_primary,number_secondary,email,anniversary)
    VALUES(?,?,?,?,?) '''
    cur = con.cursor()
    cur.execute(sql, db)
    con.commit()
    print (cur.lastrowid)

def update_data(con, db):
    sql = ''' UPDATE PB SET name = ? ,
                            number_primary = ? ,
                            number_secondary = ? ,
                            email = ? ,
                            anniversary = ?
                        WHERE id = ?'''
    cur = con.cursor()
    cur.execute(sql, db)
    con.commit()


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

    with con:
        data = ('Nick','0002','2000','nick@mail.com','1985-03-26',2)
        data2 = ('John','0004','','john@mail.com','2005-05-26');
        add_data(con, data2)
        update_data(con, data)




if __name__ == '__main__':
    main()