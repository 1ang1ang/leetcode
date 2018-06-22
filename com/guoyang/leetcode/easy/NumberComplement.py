# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/number-complement/description/

class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        ret=0
        for c in bin(num)[2:]:
            ret = ret * 2 + abs(int(c) - 1)
        return ret

print(Solution.findComplement(Solution, 5))