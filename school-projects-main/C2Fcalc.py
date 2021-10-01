print("This script will convert Celcius degrees to Fahrenheit")


def c2fconv():
    Celcius = (float(input("Please define C to proceed: ")))
    Fahr = (Celcius * 9 / 5) + 32
    print(f"{Celcius} in Celsius is equal to {Fahr} in Fahrenheit.")
    rep = (str(input("Would you like to make another conversion? Y/N: ")))
    if rep == ("Y") or rep == ("y"):
        c2fconv()
    else:
        exit()


c2fconv()
