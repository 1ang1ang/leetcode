# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','o','i','u','A','E','O','I','U']
        vowIdx = []
        for i in range(len(s)):
            c = s[i]
            if c in vowels:
                vowIdx.append(i)
        sList = list(s)
        for idx in range(int(len(vowIdx) / 2)):
            sList[vowIdx[idx]],sList[vowIdx[~idx]] = sList[vowIdx[~idx]],sList[vowIdx[idx]]
        return "".join(sList)
print(Solution.reverseVowels(Solution, "leetcode"))