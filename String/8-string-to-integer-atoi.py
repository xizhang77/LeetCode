# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/string-to-integer-atoi/
'''

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        
        if not str:
            return 0
        
        MIN, MAX = -2**31, 2**31-1
        
        sign = 1
        if str[0] == '-':
            sign = -1
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        
        i = 0
        while i < len(str) and str[i].isdigit():
            i += 1
        
        if i == 0:
            return 0
        
        ans = sign * int(str[:i])
        if sign > 0:
            return ans if ans <= MAX else MAX
        else:
            return ans if ans >= MIN else MIN