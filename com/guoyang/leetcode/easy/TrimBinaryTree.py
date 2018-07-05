# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/trim-a-binary-search-tree/description/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if root == None:
            return root
        if root.val < L:
            return Solution.trimBST(Solution,root.right, L,R)
        elif root.val > R:
            return Solution.trimBST(Solution,root.left, L,R)

        root.left = Solution.trimBST(Solution,root.left, L,R)
        root.right = Solution.trimBST(Solution, root.right, L, R)
        return root
node = TreeNode(3)
left = TreeNode(1)
left.right = TreeNode(2)
node.left = left
node.right = TreeNode(4)
print(Solution.trimBST(Solution , node , 3 , 4))