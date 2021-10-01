print ("This program will convert Fahrenheit degrees to Celsius.")
def f2cconv():
    f = (float(input("Please define F to proceed: ")))
    c = (f - 32) * 5 / 9
    print(f"{f} in Fahrenheit is equal to {c} in Celsius.")
    x = (str(input("Would you like to make another conversion? Y/N: ")))
    if x == ("Y") or x == ("y"):
        f2cconv()
    else:
        exit()


f2cconv()