# this is a simple phone book script that uses a PY dictionary in order to store and retrieve name:number pairs.
# hit works using a menu with 5 options: read, add, delete, search_and_edit and exit.


print("""This is a phonebook app
please select from the following five options to proceed
""")

phonebook = {}


# menu defined as a function in order to facilitate loop callbacks

def menu():
    selection = (input("""1:View phonebook
2:Add contact
3:Delete contact
4:Search for a contact and if necessary edit it
5:Exit

What would you like to to?"""))

# simple, if it's empty it's empty if it's not it's not

    if selection == "1":
        if len(phonebook) == 0:
            print("Phonebook is empty, please add a contact first.")
            loop = input("Press Enter to continue ...")
            menu()

        else:
            for i in sorted(phonebook):
                print("Name: ", i, "Number: ", phonebook[i])
            loop = input("Press Enter to continue ...")
            menu()

# contacts are stored as "last, first:number", phone numbers are inserted as str in order
# to allow special characters such as + for numbers in international format (eg +44 for the UK etc)

    elif selection == "2":
        first = (str(input("First name: ")))
        last = (str(input("Last name: ")))
        num = (str(input("Number? ")))
        phonebook.update({last + ", " + first: num})
        loop = input("Contact saved, press Enter to continue.")
        menu()

# search by key and delete, if-else exit loops should prevent user from accidentally deleting the wrong contact

    elif selection == "3":
        search = (str(input("Please type the exact name of the contact wish to delete: ")))
        if search in phonebook.keys():
            print("Name: ", search, "Number: ", phonebook[search])
            edit = (str(input("Is this the contact you are looking for? Y/N")))
            if edit == "N" or edit == "n":
                menu()
            if edit == "Y" or edit == "y":
                confirm = (str(input("Are you sure you want to delete this contact? Y/N")))
                if confirm == "Y" or confirm == "y":
                    phonebook.pop(search)
                    print("Contact deleted successfully.")
                    loop = input("Press Enter to continue.")
                    menu()
                if confirm == "N" or confirm == "n":
                    menu()
        else:
            print("Contact not found.")
            loop = input("Press Enter to continue.")
            menu()

# simple: find contact, confirm, add new, delete old

    elif selection == "4":
        search = (str(input("Please type the exact name of the contact you are looking for: ")))
        if search in phonebook.keys():
            print("Name: ", search, "Number: ", phonebook[search])
            edit = (str(input("Do you wish to edit this contact? Y/N")))
            if edit == "N" or edit == "n":
                menu()
            if edit == "Y" or edit == "y":
                phonebook.pop(search)
                first = (str(input("First name: ")))
                last = (str(input("Last name: ")))
                num = (str(input("Number? ")))
                phonebook.update({last + ", " + first: num})
                loop = input("Contact updated, press Enter to continue.")
                menu()
        else:
            print("Contact not found.")
            loop = input("Press Enter to continue.")
            menu()

# BYE!!!

    elif selection == "5":
        loop = input("Thank you for using phonebook app, please press Enter to exit.")
        exit()

    else:
        print("Invalid selection.")
        loop = input("Press Enter to continue ...")
        menu()


menu()
