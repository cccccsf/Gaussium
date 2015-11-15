import numpy as np

"""
NAME
    Matrix

SYNOPSIS
    __init__(self, matrix_size)
    int matrix_size

    create_matrix(self, element)
    Element element
    np.matrix matrix

DESCRIPTION
    A class with a create_matrix method that takes in a matrix element calculator and builds the matrix for it for the
    desired matrix_size. For example taking in the orbital overlap matrix element calculator it will build the orbital
    overlap matrix. The point of this class is to reduced repeating code. I have purposely made the class calculate go
    through all values of i, j so that I can check that that element.calculate(i, j) produces a symmetric matrix. It is
    slightly less efficient but not by much as most of the time is spend on the two electron repulsion integrals.

ARGUMENTS
    def __init__(self, matrix_size)
    matrix_size Input:  initialise the object with the length of the basis set.
    
    def create_matrix(self, element)
    element     Input:  an object with a calculate method that calculates the matrix element for the position i, j.
    matrix      Output: an numpy matrix, e.g. the overlap matrix.

SEE ALSO
    density_matrix_element.py
    g_matrix_element.py
    kinetic_energy_element.py
    nuclear_attraction_element.py
    orbital_overlap_element.py
    two_electron_repulsion_element.py

DIAGNOSTICS
    None, as long as this object and the element objects are correctly initialised.
"""


class Matrix:

    def __init__(self, matrix_size):
        self.matrix_size = matrix_size

    def create_matrix(self, element):
        matrix = []
        for i in range(self.matrix_size):
            matrix_row = []
            for j in range(self.matrix_size):
                element_ij = element.calculate(i, j)
                matrix_row.append(element_ij)
            matrix.append(matrix_row)
        matrix = np.matrix(matrix)
        return matrix
