# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyList = []
        keyList.append(set('qwertyuiop'))
        keyList.append(set('asdfghjkl'))
        keyList.append(set('zxcvbnm'))
        ret = []
        for word in words:
            tmp = set(str(word).lower())
            for key in keyList:
                if tmp <= key:
                    ret.append(word)
                    break
        return ret
print(Solution.findWords(Solution, ["Hello", "Alaska", "Dad", "Peace"]))