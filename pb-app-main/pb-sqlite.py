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
    except Error:
        pass
    finally:
        if con is None:
            con.close()

def view_all(con):
    curs = con.cursor()
    curs.execute("SELECT * FROM pb")
    rows = curs.fetchall()

    for row in rows:
        print(row)
    

def add_data(con, db):
    sql = ''' INSERT INTO PB(name,number_primary,number_secondary,email,anniversary)
    VALUES(?,?,?,?,?) '''
    cur = con.cursor()
    cur.execute(sql, db)
    con.commit()
    print (f"Contact added successfully, entry id is #{cur.lastrowid}")
    loop = input("Press Enter to continue.")
    

def search_name(con, query):
    sql = '''SELECT * FROM pb WHERE name LIKE ?'''
    cur = con.cursor()
    cur.execute(sql, query)
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No results found!")
    else:
        for row in rows:
            print(row)

def search_number(con, query):
    sql = '''SELECT * FROM pb WHERE number_primary LIKE ? OR number_secondary LIKE ?'''
    cur = con.cursor()
    cur.execute(sql, query)
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No results found!")
    else:
        for row in rows:
            print(row)

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

    print ("""This is v0.2 of my phonebook app
it should have the same functionality as the first one except this time
using SQLite3 instead of an empty dictionary thus offering permanent storage...
hopefully...
    
""")

    loop = input("Press Enter to continue ...")
    
    def menu():

        print("""Press 1 to view all entries.
Press 2 to search for a specific contact.
Press 3 to add a new contact.
Press 4 to edit an existing contact.
Press 5 to delete a contact.
Press 6 to exit.""")

        while True:
            try:
                selection = int(input("What would you like to do? "))
                break
            except:
                print("invalid selection")
                loop = input("Press Enter to view the menu...")
                menu()


        
        if selection == 1:
            view_all(con)
            loop = input("Press Enter to continue ...")
            menu()

        elif selection == 2:
            def sel2():
                print("""Press 1 to search by Name.
Press 2 to search by Number.
Press 3 to search by Email.
Press 4 to go back to the main menu.""")
                while True:
                    try:
                        selection = int(input("What would you like to do? "))
                        break
                    except:
                        print("invalid selection")
                        loop = input("Press Enter to go back to the menu...")
                        sel2()


                if selection == 1:
                    wild = "%"
                    name = str(input("Name:\n"))
                    data = (f"{wild}{name}{wild}",);
                    search_name(con, data)
                    loop = input("Press Enter to go back to the menu...")
                    menu()
                elif selection == 2:
                    wild = "%"
                    name = str(input("Number:\n"))
                    data = (f"{wild}{name}{wild}", f"{wild}{name}{wild}");
                    search_number(con, data)
                    loop = input("Press Enter to go back to the menu...")
                    menu()
                elif selection == 3:
                    pass
                elif selection == 4:
                    menu()
            sel2()
                
        elif selection == 3:
                name = str(input("Name (mandatory)?\n"))
                number_primary = str(input("Primay number (mandatory)?\n"))
                number_secondary = str(input("Secontary number (optional)?\n"))
                email = str(input("Email (optional)?\n"))
                date = str(input("Important date (eg birthday, Optional)?\n"))
                data = (name, number_primary, number_secondary, email, date);
                add_data(con, data)
                menu()
        elif selection == 4:
                pass
        elif selection == 5:
                pass
        elif selection == 6:
                exit()
        
        else:
            print("Invalid selection")
            loop = input("Press Enter to continue ...")
            menu()
            



    menu()
    


    

        #with con:
            #data = ('Nick','0002','2000','nick@mail.com','1985-03-26',2)
            #update_data(con, data)




if __name__ == '__main__':
    main()