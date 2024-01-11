#!/usr/bin/python3
"""Module contains one function to handle matrices."""


def matrix_divided(matrix, div):
    """A function to divide all elements of a matrix by div.

    Args:
        matrix (list): The matrix.
        div (int or float): The divisor.

    Returns:
        list: The matrix divided.

    Raises:
        TypeError: If matrix is not a list of lists containing int or float.
        TypeError: If sublists are not all the same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) "
                            "of integers/floats")

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")

    div_mat = []
    for submat in matrix:
        submat_div = []
        for e in submat:
            result = round(e / div, 2)
            submat_div.append(result)
        div_mat.append(submat_div)

    return div_mat

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
