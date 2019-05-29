# -*- coding: utf-8 -*-

'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MIN = - 2**31
        MAX = 2**31 - 1 
        if x < 0:
            temp = list(str(x))[1:]
            while temp[-1] == '0':
                temp.pop()
            ans = - int( "".join(temp[::-1]) )
            return ans if ans >= MIN else 0
        elif x > 0:
            temp = list(str(x))
            while temp[-1] == '0':
                temp.pop()
            ans = int( "".join(temp[::-1]) )
            return ans if ans <= MAX else 0
        else:
            return x