# -*- coding: utf-8 -*-

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# Solution 1: Two pointer 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortNum = sorted( nums )
        
        i, j = 0, len(nums) - 1
        
        while i < j:
            temp = sortNum[i] + sortNum[j]
            if temp < target:
                i += 1
            elif temp > target:
                j -= 1
            else:
                if sortNum[i] != sortNum[j]:
                    return sorted([ nums.index(sortNum[i]), nums.index(sortNum[j])])
                else:
                    return sorted([idx for idx in range( len(nums)) if nums[idx] == sortNum[i]])