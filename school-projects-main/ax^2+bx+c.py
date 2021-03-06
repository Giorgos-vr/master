import math as ma

print("Το πρόγραμμα αυτό υπολογίζει την διακρίνουσα του αχ^2+βχ+γ και εμφανίζει τις πιθανές ρίζες.")
input("Πατήστε ENTER για να συνεχίσετε")

def diakrinousa():
    a = input("Εισάγετε το α= ")
    b = input("Εισάγετε το β= ")
    c = input("Εισάγετε το γ= ")
    print (f"Θα προσπαθήσουμε να λύσουμε την εξίσωση: {a}x^2 + {b}x + {c} = 0")
    input("Πατήστε ENTER για να συνεχίσετε")
    a = float(a)
    b = float(b)
    c = float(c)

    if a == 0 :
        if b == 0 :
            if c == 0 :
                print("Υπάρχουν άπειρες λύσεις")
            else :
                print("Δεν υπάρχουν λύσεις")
        else :
            print (f"Οι λύσεις είναι χ1 = χ2 = {- c/b:.3f}")
    else :
        d = b**2 - 4 * a * c
        print(f"H διακρίνουσα είναι {d:.2f}")

        if d < 0 :
            print("Η εξίσωση δεν έχει πραγματικές λύσεις")
        else :
            x1 = (-b + ma.sqrt(d))/(2*a)
            x2 = (-b - ma.sqrt(d))/(2*a)
            print(f"Οι λύσεις είναι: χ1 = {x1:.3f}, χ2 = {x2:.3f}")
    rep = input("\nΘέλετε να κάνετε έναν νέο υπολογισμό; Υ/Ν: ")
    if rep == ('Y') or rep == ('y') or rep == ('Υ') or rep == ('υ'):
        diakrinousa()
    else:
        exit()

diakrinousa()