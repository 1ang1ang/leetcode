# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/array-partition-i/description/

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])

print(Solution.arrayPairSum(Solution, [1,4,2,3]))