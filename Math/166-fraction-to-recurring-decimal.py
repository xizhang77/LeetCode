# -*- coding: utf-8 -*-

'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''


class Solution(object):
    def devide(self, b, a):
        div = int( b/a )
        mod = b - div*a
        
        return div, mod
        
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ans = "-" if numerator*denominator < 0 else ""
        numerator = abs( numerator )
        denominator = abs( denominator )
        
        div, mod = self.devide( numerator, denominator )
        if mod == 0:
            return ans + str( div )
        
        ans += str( div ) + "."
        
        _map = {}
        _map[ mod ] = len( ans )
        
        while mod:
            mod *= 10
            div, mod = self.devide( mod, denominator )
            ans += str(div)
            
            if mod in _map:
                idx = _map[ mod ]
                ans = ans[:idx] + "(" + ans[idx:] + ")"
                return ans
            
            _map[mod] = len(ans)
        
        return ans
        