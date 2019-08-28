# -*- coding: utf-8 -*-

'''
Given a positive integer num, write a function which returns True 
if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''

# Solution 1: Binary Search
# Time: O(log(num))
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
                
        i, j = 1, num
        
        while i <= j:
            mid = int( i + (j-i)/2 )
            if mid ** 2 < num:
                i = mid + 1
            elif mid ** 2 > num:
                j = mid - 1
            else:
                return True
        
        return False

# Solution 2: Brute Force
# Time: O(log(num))

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        i = 1
        while i**2 < num:
            i += 1
        
        return i ** 2 == num