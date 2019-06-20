# -*- coding: utf-8 -*-

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, 
otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
'''

class Solution(object):
    def linear(self, nums, target):
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return True
            i += 1
        
        return False
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        
        if nums[0] == nums[-1]:
            return self.linear( nums, target )
        
        i, j = 0, len(nums) - 1
        
        while i <= j:
            if nums[i] == nums[j]:
                return self.linear( nums[i:j+1], target )
            
            mid = i + (j-i)/2
            
            if nums[mid] == target:
                return True
            if nums[mid] > nums[j]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        
        return False