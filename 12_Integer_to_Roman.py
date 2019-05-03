# -*- coding: utf-8 -*-

'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: 3
Output: "III"

Example 2:
Input: 4
Output: "IV"

Example 3:
Input: 9
Output: "IX"

Example 4:
Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Example 5:
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

'''

'''
Keypoints: hashMap
'''

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        hashMap = {1:{1: 'I', 4: 'IV', 5: 'V', 9: 'IX'}, 
                   2:{1: 'X', 4: 'XL', 5: 'L', 9: 'XC'}, 
                   3:{1: 'C', 4: 'CD', 5: 'D', 9: 'CM'}, 
                   4:{1: 'M'} }
        
        flag = 1000
        ans = ""
        
        while num:
            res = num / flag
            num = num % flag
            
            if res:
                key = len( str(flag) )
                if res in hashMap[ key ]:
                    ans += hashMap[ key ][ res ]
                elif res <= 3:
                    ans += hashMap[ key ][ 1 ] * res
                else:
                    ans += hashMap[ key ][ 5 ] + hashMap[ key ][ 1 ] * (res - 5)
            
            flag = flag/10
        
        
        return ans