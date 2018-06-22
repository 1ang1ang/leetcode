# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/reverse-words-in-a-string-iii/description/

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sArr = s.split()
        for i in range(int((len(sArr)))):
            sArr[i] = sArr[i][::-1]
        return " ".join(sArr)
print(Solution.reverseWords(Solution, "Let's take LeetCode contest"))


