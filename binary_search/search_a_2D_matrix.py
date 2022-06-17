import numpy as np


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        array = set(np.array(matrix).flatten())
        if target in array:
            return True
        else:
            return False
