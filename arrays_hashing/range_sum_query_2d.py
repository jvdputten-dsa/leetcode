from itertools import accumulate
import numpy as np


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = self.cum_sum_matrix(np.array(matrix))

    def cum_sum_matrix(self, matrix):
        for i, row in enumerate(matrix):
            matrix[i] = np.cumsum(row)
        matrix = matrix.transpose()
        for j, col in enumerate(matrix):
            matrix[j] = np.cumsum(col)
        return matrix.transpose()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        res = self.matrix[row2, col2]
        if row1:
            res -= self.matrix[row1 - 1, col2]
        if col1:
            res -= self.matrix[row2, col1 - 1]
        if row1 and col1:
            res += self.matrix[row1 - 1, col1 - 1]

        return res