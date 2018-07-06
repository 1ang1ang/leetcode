# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums) + 1)) - sum(nums)
print(Solution.missingNumber(Solution, [3,0,1]))