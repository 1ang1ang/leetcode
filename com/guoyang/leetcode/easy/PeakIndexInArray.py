# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/peak-index-in-a-mountain-array/description/

class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in range(len(A)):
            if A[i] > A[i+1]:
                return i

print(help(list.index))
print(Solution.peakIndexInMountainArray(Solution,[0,1,0]))