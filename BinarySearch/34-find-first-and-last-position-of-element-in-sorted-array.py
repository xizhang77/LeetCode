# -*- coding: utf-8 -*-

'''
Given an array of integers nums sorted in ascending order, 
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

# Time: O(logn)
class Solution(object):
    def binarySearch(self, nums, target):
        i, j = 0, len(nums) - 1
        
        while i <= j:
            mid = i + (j-i)/2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        return i
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [ -1, -1 ]
        left = self.binarySearch( nums, target )
        
        if left >= len(nums) or left < 0 or nums[left] != target:
            return [-1, -1]
        else:
            return [ left, self.binarySearch( nums, target + 1) - 1]