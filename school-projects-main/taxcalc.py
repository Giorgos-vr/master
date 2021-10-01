print("This program will calculate yearly taxes due based on monthly income and tax percentage.")


def taxfunc():                                                                    # function to calculate yearly tax
    monthly = (str(input("Monthly income: ")))                                    # input variable to be used later
    tax = (str(input("Tax percentage: ")))                                        # input variable to be used later
    month = float(''.join(filter(str.isdigit, monthly)))                          # filter usable data from user input
    taxfrac = float(''.join(filter(str.isdigit, tax)))                            # filter usable data from user input
    taxdue = (month * 12) * taxfrac / 100                                         # calculate yearly tax (flat tax)
    print(f"Tax due is {taxdue} of your local currency")                          # RESULTS!!!
    repeat = (str(input('Would you like to make another calculation? Y/N: ')))    # repeat loop
    if repeat == ('Y') or repeat == ('y') or repeat == ('Υ') or repeat == ('υ'):  # rep parameters incl Greek variants
        taxfunc()                                                                 # function callback
    else:                                                                         # unconditional loop termination
        exit()


taxfunc()
