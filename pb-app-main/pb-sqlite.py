import sqlite3 as sl
from sqlite3 import Error
import os




file_path = os.path.join("data")
os.makedirs(file_path, exist_ok=True)
db = os.path.join(file_path, "pb.db")

def create_connection(db):
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
    

def add_data(con, entry):
    sql = ''' INSERT INTO PB(name,number_primary,number_secondary,email,anniversary)
    VALUES(?,?,?,?,?) '''
    cur = con.cursor()
    cur.execute(sql, entry)
    con.commit()
    print (f"Contact added successfully, entry id is #{cur.lastrowid}")
    

def search(con, query):
    sql = '''SELECT * FROM pb WHERE number_primary LIKE ? OR number_secondary LIKE ? OR name LIKE ? OR email LIKE ?'''
    cur = con.cursor()
    cur.execute(sql, query)
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No results found!")
    else:
        for row in rows:
            print(row)
                      
def update_data(con, query):
    sql = ''' UPDATE PB SET name = ? ,
                            number_primary = ? ,
                            number_secondary = ? ,
                            email = ? ,
                            anniversary = ?
                        WHERE id = ?'''
    cur = con.cursor()
    cur.execute(sql, query)
    con.commit()
    print ("Contact updated successfully!")

def delete_entry(con, query):
    sql = 'DELETE FROM pb WHERE id=?'
    cur = con.cursor()
    cur.execute(sql, (query,))
    con.commit()
    print ("Contact successfully deleted!")

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
            wild = "%"
            entry = str(input("Search:\n"))
            data = (f"{wild}{entry}{wild}", f"{wild}{entry}{wild}", f"{wild}{entry}{wild}", f"{wild}{entry}{wild}");
            search(con, data)
            loop = input("Press Enter to go back to the main menu...")
            menu()
                
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
            wild = "%"
            print("Search for the contact you wish to update and make a note of its id number.")
            entry = str(input("Search:\n"))
            data = (f"{wild}{entry}{wild}", f"{wild}{entry}{wild}", f"{wild}{entry}{wild}", f"{wild}{entry}{wild}");
            search(con, data)
            while True:
                try:
                    selection = int(input("Please enter the id number of the contact you wish to update:\n"))
                    break
                except:
                    print("invalid selection")
                    loop = input("Press Enter to go back to the main menu...")
                    menu()
            print("Please enter the new details.")
            name = str(input("Name (mandatory)?\n"))
            number_primary = str(input("Primay number (mandatory)?\n"))
            number_secondary = str(input("Secontary number (optional)?\n"))
            email = str(input("Email (optional)?\n"))
            date = str(input("Important date (eg birthday, optional)?\n"))
            data = (name, number_primary, number_secondary, email, date, selection)
            with con:
                update_data(con, data)
            loop = input("Press Enter to continue.")
            menu()

        elif selection == 5:
            wild = "%"
            print("Search by name, number or email for the contact you wish to delete and make a note of its id number.")
            entry = str(input("Search:\n"))
            data = (f"{wild}{entry}{wild}", f"{wild}{entry}{wild}", f"{wild}{entry}{wild}", f"{wild}{entry}{wild}");
            search(con, data)
            while True:
                try:
                    selection = int(input("Please enter the id number of the contact you wish to delete:\n"))
                    break
                except:
                    print("invalid selection")
                    loop = input("Press Enter to go back to the main menu...")
                    menu()
            confirm = str(input("Are you sure you wish to delete this? Y/N?\n"))
            if confirm == ('Y') or confirm == ('y') or confirm == ('Υ') or confirm == ('υ'):
                delete_entry(con, selection)
                loop = input("Press Enter to return to the main menu.")
                menu()
            else:
                loop = input("Selection cancelled!\nPress Enter to return to the main menu.")
                menu()


        elif selection == 6:
                exit()
        
        else:
            print("Invalid selection")
            loop = input("Press Enter to continue ...")
            menu()
            



    menu()


if __name__ == '__main__':
    main()