# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for a in A:
            for i in range(int((len(a) + 1) / 2)):
                a[i],a[~i] = a[~i] ^ 1,a[i] ^ 1
        return A

print(Solution.flipAndInvertImage(Solution, [[1,1,0],[1,0,1],[0,0,0]]))


