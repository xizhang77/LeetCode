# -*- coding: utf-8 -*-

'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees 
(looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented 
as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
'''

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        check = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        
        new = ""
        
        for char in num:
            if char not in check:
                return False
            new = check[ char ] + new

        return num == new