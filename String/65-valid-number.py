# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/valid-number/
'''

class Solution(object):
    def isFloat(self, s):
        if not s:
            return False
        
        digits = set("0123456789")
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        
        dec = 0
        count = 0
        for char in s:
            if char in digits:
                count += 1
            if char == '.':
                dec += 1
                continue
            if char not in digits:
                print char
                return False

        return count > 0 and dec <= 1
        
    def isInt(self, s):
        if not s:
            return False
        digits = set("0123456789")
        if s[0] == '-' or s[0] == '+':
            s = s[1:]
        
        count = 0
        for char in s:
            if char in digits:
                count += 1
            else:
                return False
            
        return count > 0
        
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        check = set(" 0123456789e-+.")
        
        for char in s:
            if char not in check:
                return False
        
        s = s.strip()
        
        if 'e' in s:
            digits = s.split("e")
            if len(digits) > 2:
                return False
            return self.isFloat( digits[0] ) and self.isInt( digits[1] )
        else:
            return self.isFloat( s )