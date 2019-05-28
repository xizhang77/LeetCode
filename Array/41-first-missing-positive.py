# -*- coding: utf-8 -*-

'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.


'''

# Time: O(n); Space: O(1)
# Attention: using while loop instead of for loop to match the space requirment
# If we use for loop here, the memory requirment is O(n) instead of O(1)
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        check = set(nums)
        
        i = 1
        while i <= max(1, max(check) + 1):
            if i not in check:
                return i
            i += 1
