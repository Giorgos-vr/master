import numpy as num

print("""Το πρόγραμμα αυτό εμφανίζει παραδείγματα τυχαίων διανυσμάτων και πινάκων
με την χρήση των βιβλιοθηκών της numpy: rand(), randn() και randint()\n""")

input("Πατήστε ENTER για να επιλέξετε το παράδειγμα που θέλετε να δείτε.\n")

def main():
    class menu:
        def rand_func1():
            result = num.random.rand(3)
            print(result)
        
        def rand_func2():
            result = num.random.rand(2,3)
            print(result)

        def randn_func1():
            result = num.random.randn(3)
            print(result)
        
        def randn_func2():
            result = num.random.randn(2,3)
            print(result)

        def randint_func1():
            result = int(num.random.randint(1,11,1))
            print(result)
        
        def randint_func2():
            result = num.random.randint(1,101,6)
            print(result)
        
        def randint_func3():
            result = num.random.randint(1,101 ,(2 , 3))
            print(result)

    
    print("""\nΓια να δείτε ένα διάνυσμα 3 τυχαίων αριθμών με την μέθοδο rand() επιλέξετε 1
Για να δείτε έναν πίνακα (2x3) με 6 τυχαία στοιχεία με την μέθοδο rand() επιλέξτε 2
(σημ. η rand() δημιουργεί τυχαίους ομοιόμορφα κατανεμημένους αριθμούς μεταξύ του 0 και του 1).

Για να δείτε ένα διάνυσμα 3 τυχαίων αριθμών με την μέθοδο randn() επιλέξτε 3
Για να δείτε έναν πίνακα (2x3) με 6 τυχαία στοιχεία με την μέθοδο randn() επιλέξτε 4
(σημ. η randn() παράγει τυχαίους αριθμούς από την κανονική κατανομή).

Για να δείτε μια τυχαία τιμή σε εύρος (1, 10) με την μέθοδο randint() επιλέξτε 5
Για να δείτε ένα τυχαίο διάνυσμα 6 αριθμών μεταξύ του 1, 100 με την μέθοδο randint() επιλέξτε 6
Για να δείτε ένα πίνακα 6 στοιχείων (2x3) μεταξύ του 1, 100 με την μέθοδο randint() επιλέξτε 7
(σημ. η randint() παράγει τυχαίους ακέραιους αριθμούς εντός ενός συγκεκριμένου εύρους.\n""")

    selection = int(input("Επιλογή; "))
    if selection == 1:
        menu.rand_func1()
    elif selection == 2:
        menu.rand_func2()
    elif selection == 3:
        menu.randn_func1()
    elif selection == 4:
        menu.randn_func2()
    elif selection == 5:
        menu.randint_func1()
    elif selection == 6:
        menu.randint_func2()
    elif selection == 7:
        menu.randint_func3()
    else:
        print("invalid selection")
     
    rep = input("\nΘα θέλατε να δείτε κάποιο άλλο παράδειγμα; Υ/Ν: ")
    if rep == ('Y') or rep == ('y') or rep == ('Υ') or rep == ('υ'):
        main()
    else:
        exit()



if __name__ == "__main__":
    main()
