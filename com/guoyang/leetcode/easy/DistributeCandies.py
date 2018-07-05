# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/distribute-candies/description/

class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        l = len(set(candies))
        if l > len(candies) / 2 :
            return int(len(candies) / 2)
        return int(l)
print(Solution.distributeCandies(Solution, [1,1,2,3]))