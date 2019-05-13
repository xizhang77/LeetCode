# -*- coding: utf-8 -*-

'''
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
'''

# Solution 1: Bit Manipulation

class Solution1(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        
        for num in nums[1:]:
            ans ^= num
        
        return ans

# Solution 2: Hash Table / Set

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = set()
        
        for num in nums:
            if num not in temp:
                temp.add( num )
            else:
                temp.remove( num )
        
        return list(temp)[0]