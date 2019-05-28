# -*- coding: utf-8 -*-

'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

# Time: O(n^2); Extra Space: O(1)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        
        ans = []
        
        i = 0
        while i < len( nums ):
            if nums[i] > 0:
                break
                
            j, k = i + 1, len(nums) - 1 
            while j < k:
                if nums[j] + nums[k] < - nums[i]:
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j += 1
                elif nums[j] + nums[k] > - nums[i]:
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    k -= 1
                else:
                    ans.append( [nums[i], nums[j], nums[k] ])
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1
                    k -= 1
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            i += 1
            
        return ans