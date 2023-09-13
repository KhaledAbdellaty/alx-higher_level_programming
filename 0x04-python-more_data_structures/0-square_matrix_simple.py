#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for i in matrix:
        res = list(map(lambda x: x * x, i))
        new_list.append(res)
    return new_list
