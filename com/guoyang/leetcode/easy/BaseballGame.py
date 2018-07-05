# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/baseball-game/description/

class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        mark = []
        for op in ops:
            if op == "C":
                mark.pop()
            elif op == "D":
                mark.append(2 * mark[-1])
            elif op == "+":
                mark.append(mark[- 1] + mark[- 2])
            else:
                mark.append(int(op))
        return sum(mark)
print(Solution.calPoints(Solution,["5","2","C","D","+"]))