# -*- coding: utf-8 -*-

'''
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
'''

# Time: O(logn); Space: O(1)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i, j = 0, x
        
        while i <= j:
            mid = i + (j-i)/2
            if mid*mid < x:
                i = mid + 1
            elif mid*mid > x:
                j = mid - 1
            else:
                return mid
        
        return j