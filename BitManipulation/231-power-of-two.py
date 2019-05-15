# -*- coding: utf-8 -*-

'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false
'''

# Solution 1: Bit Manipulation
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mask = 1
        
        for i in range(32):
            if n ^ mask == 0:
                return True
            mask <<= 1
        
        return False

# Solution 2: Math [ Corner case: n = 0]
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        while n > 1 and n%2 == 0:
            n = n/2
        
        return n == 1