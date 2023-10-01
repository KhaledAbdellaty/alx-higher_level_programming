#!/usr/bin/python3
"""
Define a function to divide the matrix elements

"""


def matrix_divided(matrix, div):
    """Returns a new matrix
    Args:
        matrix (list of list): integers/floats
        div (int/float): the matrix should be divided by div number
    """

    if not isinstance(matrix, list) or not \
       [isinstance(row, list) for row in matrix]:
        raise TypeError('matrix must be a matrix '
                        '(list of lists) of integers/floats')

    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    else:
        new_matrix = []
        for i in range(len(matrix)):
            new_list = []

            if len(matrix[0]) != len(matrix[i]):
                raise TypeError('Each row of the matrix '
                                'must have the same size')
            for j in matrix[i]:
                if not isinstance(j, (int, float)):
                    raise TypeError('matrix must be a matrix '
                                    '(list of lists) of integers/floats')
                new_list.append(round(j / div, 2))

            new_matrix.append(new_list)
    return new_matrix
