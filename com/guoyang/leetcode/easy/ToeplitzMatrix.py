# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        row = len(matrix)
        if row == 0:
            return True
        col = len(matrix[0])
        for i in range(row - 1):
            for j in range(col - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True

# help(range)
print(Solution.isToeplitzMatrix(Solution,
                                [
                                    [11, 74, 0, 93],
                                    [40, 11, 74, 7]]
                                ))
print(Solution.isToeplitzMatrix(Solution,
                                [
                                    [1, 2, 3, 4],
                                    [5, 1, 2, 3],
                                    [9, 5, 1, 2]
                                ]
                                ))