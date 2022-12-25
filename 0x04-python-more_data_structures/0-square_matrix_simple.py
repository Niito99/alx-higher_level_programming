#!/usr/bin/python3

def square_matrix_simple(matrix = []):
    check_len = len(matrix)
    general_matrix = []
    for x in range(0, check_len):
        general_matrix.append(list())
    k = 0

    for i in matrix:
        for j in i:
            value = j * j
            general_matrix[k].append(value)
        k += 1
    
    return general_matrix
