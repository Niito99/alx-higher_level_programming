#!/usr/bin/python3

def search_replace(mylist, search, replace):
    k = 0
    for i in mylist:
        if i == search:
            mylist[k] = replace

        k += 1
    return mylist
