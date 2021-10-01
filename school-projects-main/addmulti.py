print("""This is a simple script that adds and projects the sum of two numbers
It also multiplies the same two numbers and projects their product.""")

def addmulti():
    x = float(input("Please type 1st number: "))
    y = float(input("Please type 2nd number: "))
    s = x+y
    m = x*y
    print(f"The sum of these two numbers is {s}, their product is {m}.")
    x = (str(input("Would you like to try again? Y/N: ")))
    if x == ("Y") or x == ("y"):
        addmulti()
    else:
        exit()


addmulti()