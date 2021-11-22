import numpy as num


def bubble_sort():
    list = num.random.randint(1, 101, 10)
    list_length = len(list)
    print (f"Αρχική λίστα:\n{list}\n")

    for x in range(list_length - 1):
        for y in range(list_length - 1 - x):
            if list[y + 1] < list[y]:
                list[y], list[y + 1] = list[y + 1], list[y]

    print(f"Ταξινομημένη λίστα:\n{list}")

    rep = input("\nΘα θέλατε να ταξινομηθεί μια καινούργια λίστα; Υ/Ν: ")
    if rep == ('Y') or rep == ('y') or rep == ('Υ') or rep == ('υ'):
        bubble_sort()
    else:
        exit()
                
                

bubble_sort()