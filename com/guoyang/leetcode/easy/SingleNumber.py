# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in range(int(len(nums) / 2)):
            if nums[i * 2] != nums[i * 2+1]:
                return nums[i * 2]
        return nums[len(nums) - 1]
    def singleNumber2(self, nums):
        a=0
        for num in nums:
            a ^= num
        return a
print(Solution.singleNumber2(Solution,[1,0,1]))
print(Solution.singleNumber2(Solution,[4,1,2,1,2]))