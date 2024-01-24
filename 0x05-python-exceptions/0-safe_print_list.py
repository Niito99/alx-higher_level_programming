#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            a += 1
        print("\n")

    except IndexError:
        print("Index doesn't exist in the array")

    return a
