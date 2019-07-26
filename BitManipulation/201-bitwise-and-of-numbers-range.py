# -*- coding: utf-8 -*-

'''
Given a range [m, n] where 0 <= m <= n <= 2147483647, 
return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0
'''

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n or m == 0:
            return m
        
        if len( bin(m) ) != len( bin(n) ):
            return 0
        
        a, b = bin(m)[2:], bin(n)[2:]
        
        i = 0
        while i < len(a) - 1 and a[i] == b[i]:
            i += 1
        
        return int( a[:i]+'0'*(len(a) - i), 2 )