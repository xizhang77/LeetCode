# -*- coding: utf-8 -*-

'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == sorted(nums):
            return 0
        
        i = 0
        while i + 1 < len(nums) and nums[i] <= nums[i+1]:
            i += 1
        
        j = len(nums) - 1
        while j - 1 >= 0 and nums[j-1] <= nums[j]:
            j -= 1
        
        submin, submax = min(nums[i:j+1]), max(nums[i:j+1])
        
        while i - 1 >= 0 and submin < nums[i - 1]:
            i -= 1
        
        while j + 1 < len(nums) and submax > nums[ j + 1 ]:
            j += 1
        
        return j-i+1