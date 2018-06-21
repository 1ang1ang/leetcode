# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        cnt=0
        for c in S:
            if J.find(c) > -1:
                cnt += 1
        return cnt


print(Solution.numJewelsInStones(Solution,J="B", S="aAAbbbb"))