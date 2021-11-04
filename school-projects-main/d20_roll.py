import numpy as num
def roll():
    dice1 = num.random.randint(1,21)
    dice2 = num.random.randint(1,21)

    if dice1 == dice2:
        print(f"ζάρι 1: {dice1} και ζάρι 2: {dice2} \n ΔΙΠΛΕΣ!!!")
    else:
        print(f"ζάρι 1: {dice1} και ζάρι 2: {dice2}")

    rep = input("repeat? Y/N? ")
    if rep == ("Y") or rep == ("y"):
        roll()
    else:
        exit()      

roll()
