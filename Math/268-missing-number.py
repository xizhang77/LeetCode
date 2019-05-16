# -*- coding: utf-8 -*-

'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

'''

# Solution 1 : Hash Table / Sorting
# Time: O(n)
# One can also use XOR bit manipulation here
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len( nums )
        nums = set( nums )
        for i in range( n + 1 ):
            if i not in nums:
                return i


# Solution 2: Math
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len (nums)
        return (1+n)*n/2 - sum(nums)