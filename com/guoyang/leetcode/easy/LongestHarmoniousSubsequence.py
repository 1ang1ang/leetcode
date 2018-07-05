# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/longest-harmonious-subsequence/description/

class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        numVsCnt = {}
        for num in nums:
            numVsCnt[num] = numVsCnt.get(num,0) + 1
        result = {}

        for key,val in numVsCnt.items():
            if numVsCnt.get(key,0) == 0 or numVsCnt.get(key + 1,0) == 0:
                continue
            result[key] = numVsCnt.get(key,0) + numVsCnt.get(key + 1,0)
        if len(result) == 0:
            return 0
        return max(result.values())
print(Solution.findLHS(Solution, [1,1,1,1]))
print(Solution.findLHS(Solution, [1,3,2,2,5,2,3,7]))
print(Solution.findLHS(Solution, []))