# -*- coding: utf-8 -*-

'''
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
'''

# Solution 1, Beat 86% (Code is not elegant)
# Time: O(n); Space: O(1)
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        count = 0
        for j in range( len(nums) ):
            if nums[i] == nums[j]:
                if i == 0:
                    count += 1
                    i += 1
                elif i - 1 >= 0 and nums[i-1] == nums[i] and count < 2:
                    count += 1
                    i += 1
                elif i - 1 >= 0 and nums[i-1] != nums[i]:
                    count = 1
                    i += 1
            else:
                nums[i] = nums[j]
                if i - 1 >= 0 and nums[i-1] == nums[i] and count < 2:
                    count += 1
                    i += 1
                elif i - 1 >= 0 and nums[i-1] != nums[i]:
                    count = 1
                    i += 1
        return i


# [More elegant version]
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        
        for j in range( len(nums) ):
            if nums[i] != nums[j]:
                nums[i] = nums[j]
            
            if i < 2 or nums[i] != nums[i-2]:
                i+= 1
        
        return i