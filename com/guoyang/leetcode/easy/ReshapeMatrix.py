# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/reshape-the-matrix/description/


class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        l = []
        for i in nums:
            for j in i:
                l.append(j)
        if r * c != len(l):
            return nums
        ret = []
        for idx in range(int(len(l)/c)):
            row = int(idx / c)
            ret.append(l[idx * c:idx * c + c])
        return ret
print(Solution.matrixReshape(Solution, [[1,2],
 [3,4],[5,6]],2,3))