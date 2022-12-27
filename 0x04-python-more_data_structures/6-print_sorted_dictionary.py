#!/usr/bin/python3

def print_sorted_dictionary(a_dictioanary):
    store = []
    for i in a_dictionary:
        store.append(i)

    store.sort()
    num = len(store)
    for i in range(num):
        print("{}: {}\n".format(store[i], a_dictionary[store[i]]))


a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
print_sorted_dictionary(a_dictionary)
