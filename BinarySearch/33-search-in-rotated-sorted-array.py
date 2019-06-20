# -*- coding: utf-8 -*-

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
# Solution 1
# Time: O(logn)
class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums:
            return -1
        
        if nums[0] == target:
            return 0
        
        if nums[-1] == target:
            return len(nums) - 1
        
        
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = i + (j-i)/2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[j]:
                if nums[mid] < target and nums[j] >= target:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                if nums[mid] > target and nums[i] <= target:
                    j = mid - 1
                else:
                    i = mid + 1
        
        return -1

# Solution 2
# Time: O(logn); Space: O(1)
class Solution2(object):
    def binarySearch(self, nums, target):
        if target < nums[0] or target > nums[-1]:
            return -1
        
        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        
        i, j = 0, len(nums) - 1
        while i < j:
            mid = (i+j)/2
            if nums[ mid ] < target:
                i = mid + 1
            elif nums[ mid ] > target:
                j = mid
            else:
                return mid
        
        return -1
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        if nums[0] <= nums[-1]:
            return self.binarySearch( nums, target )
        
        i, j = 0, len(nums) - 1
        while j - i > 1:
            mid = (i+j)/2
            if nums[ mid ] > nums[i]:
                i = mid
            else:
                j = mid
        
        if target >= nums[0]:
            return self.binarySearch( nums[:j], target )
        else:
            ans = self.binarySearch( nums[j:], target )
            if ans != -1:
                return ans + j
            else:
                return ans
