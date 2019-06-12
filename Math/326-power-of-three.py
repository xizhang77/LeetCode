# -*- coding: utf-8 -*-

'''
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
'''

# Time: O( log_3 n )
class Solution1(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        
        if n == 1:
            return True
        
        if n % 3:
            return False
        
        return self.isPowerOfThree( n/3 )

# Solution 2: Pure math
import math
class Solution2(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n <= 0:
            return False
        
        d = round( math.log(n, 10)/math.log(3, 10) )

        return 3**d == n