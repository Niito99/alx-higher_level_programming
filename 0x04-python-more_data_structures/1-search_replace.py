#!/usr/bin/python3

def search_replace(mylist, search, replace):
    k = 0
    new_list = []

    for i in mylist:
        new_list.append(i)

    for i in new_list:
        if i == search:
            mylist[new_list.index(i)] = replace

        k += 1
    return new_list
