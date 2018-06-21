# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/number-of-lines-to-write-string/description/

import math

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line=1
        used=0
        for s in S:
            if 100 - used >= widths[ord(s) - ord('a')]:
                used += widths[ord(s) - ord('a')]
            else:
                used = widths[ord(s) - ord('a')]
                line += 1
        return line, used

print(Solution.numberOfLines(Solution,[4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],"bbbcccdddaaa"))