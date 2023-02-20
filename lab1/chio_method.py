#!/usr/bin/python
# -*- coding: utf-8 -*-

from lab1 import Matrix

def chio(matrix, par=1):
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) / par
    else:
        new_matrix = Matrix((len(matrix) - 1, len(matrix) - 1))

        if matrix[0][0] == 0:
            i = 0
            par = -par
            while i < len(matrix):
                if matrix[i][0] != 0:
                    for j in range(len(matrix)):
                        matrix[0][j], matrix[i][j] = matrix[i][j], matrix[0][j]
                    break
                i += 1

        for i in range(len(new_matrix)):
            for j in range(len(new_matrix)):
                new_matrix[i][j] = matrix[0][0] * matrix[i + 1][j + 1] - matrix[i + 1][0] * matrix[0][j + 1]

        par = matrix[0][0] ** (len(matrix) - 2) * par
        return chio(new_matrix, par)
