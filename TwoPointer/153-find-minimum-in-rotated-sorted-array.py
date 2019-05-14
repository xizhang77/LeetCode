# -*- coding: utf-8 -*-

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1
Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0
'''

# Solution 1, cannot handle corner cases (using min function at the end to overcome)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        
        # no rotation
        if nums[i] < nums[j]:
            return nums[i]
        
        while j - i > 1:
            mid = (i+j)/2
            
            if nums[mid-1] >= nums[mid] and nums[mid] <= nums[mid+1]:
                return nums[mid]
            
            if nums[mid] > nums[i]:
                i = mid
            else:
                j = mid
                
        return min( nums[i], nums[j] )


# Solution 2 [More elegent way]

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        
        while i <= j:
            if nums[i] <= nums[j]:
                return nums[i]
            
            mid = (i+j)/2
            
            if nums[i] > nums[mid]:
                j = mid
            else:
                i = mid + 1