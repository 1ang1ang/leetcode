# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0
        for row in range(len(grid)):
            subGrid = grid[row];
            for col in range(len(subGrid)):
                if grid[row][col] == 1:
                    sum=0
                    if col -1 >= 0:
                        sum += grid[row][col -1 ]
                    if col + 1 < len(subGrid):
                        sum += grid[row][col + 1]
                    if row - 1 >= 0:
                        sum += grid[row - 1][col]
                    if row + 1 < len(grid):
                        sum += grid[row + 1][col]
                    cnt = cnt + 4 - sum
        return cnt
print(Solution.islandPerimeter(Solution,
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))