import numpy as num
def roll():
    dice = num.random.randint(1,21)

    print(dice)
    if dice >= 1 and dice < 5:
        print("Άουτς!")
    if dice >= 5 and dice < 10:
        print("ΩΧ!")
    if dice >= 10 and dice < 15:
        print ("το'σωσες!")
    if dice >= 15:
        print("Μπράβο το αλάνι!")

    rep = input("Νέα ζαριά; Y/N?")
    if rep == ("Y") or rep == ("y"):
        roll()
    else:
        exit()      

roll()
