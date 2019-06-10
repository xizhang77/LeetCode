# -*- coding: utf-8 -*-

'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
'''

'''
当数组中有重复时，二分法可能无法知道到底要舍弃哪个半区，比如[1,0,1,1,1]和[1,1,1,0,1]
这是，只能采用顺序判断，时间复杂度为O(len(subseq))
'''

# Time: worse case O(n)
class Solution(object):
    def solver(self, nums, start, end):
        ans = nums[ start ]
        for i in range(start+1, end+1):
            if nums[i] < ans:
                ans = nums[i]
        return ans
    
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        
        i, j = 0, len(nums) - 1
        
        while i <= j:
            if nums[i] < nums[j]:
                return nums[i]
            if nums[i] == nums[j]:
                return self.solver( nums, i, j )
            
            mid = i + (j-i)/2
            if nums[i] <= nums[mid]:
                i = mid + 1
            else:
                j = mid
                