#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = set()
    value = 0
    """ go through all the elements in the list and adds
    them to the set data structure
    the set data structure eliminates duplicates and
    thereby making them unique"""
    for i in my_list:
        uniq.add(i)
    # iterate the set & adds up each element
    for i in uniq:
        value += i

    return value
