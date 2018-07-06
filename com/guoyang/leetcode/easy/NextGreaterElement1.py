# -*- encoding= utf-8 -*-

# 题目url: https://leetcode.com/problems/next-greater-element-i/description/

class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        superMap = {}
        for i in range(len(nums2)):
            superMap[nums2[i]] = i
        ret=[]
        for num1 in nums1:
            flag = False
            for i in range(superMap.get(num1),len(nums2)):
                if nums2[i] > num1:
                    ret.append(nums2[i])
                    flag = True
                    break
            if not flag:
                ret.append(-1)
        return ret
print(Solution.nextGreaterElement(Solution,nums1 = [4,1,2], nums2 = [1,3,4,2]))