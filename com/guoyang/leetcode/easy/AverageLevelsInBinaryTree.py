# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ret=[]
        # ret.append(root.val)

root = TreeNode(3)
root.left = TreeNode(9)
right = TreeNode(20)
right.left = TreeNode(15)
right.right = TreeNode(7)
root.right = right
print(Solution.averageOfLevels(Solution,root))