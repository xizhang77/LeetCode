# -*- coding: utf-8 -*-

'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ans = []
        a, b = list(a), list(b)

        p, q = len(a) - 1, len(b) - 1
        res = 0
        
        while p >= 0 and q >= 0:
            temp = int(a[p]) + int(b[q]) + res
            res = temp/2
            ans += [ str(temp%2) ]
            p -= 1
            q -= 1
        
        while p >= 0:
            temp = int(a[p]) + res
            res = temp/2
            ans += [ str(temp%2) ]
            p -= 1
            
        while q >= 0:
            temp = int(b[q]) + res
            res = temp/2
            ans += [ str(temp%2) ]
            q -= 1
        
        if res:
            ans += [ str(res) ]
        
        return "".join( ans[::-1] )