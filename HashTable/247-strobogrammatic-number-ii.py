# -*- coding: utf-8 -*-

'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

Example:

Input:  n = 2
Output: ["11","69","88","96"]
'''

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        hashmap = { "0":"0", "1":"1", "6":"9", "8":"8", "9":"6" }
        
        if n%2:
            ans = [ '0', '1', '8' ]
        else:
            ans = [ '' ]
            
        if n <= 1:
            return ans
        
        while n > 1:
            temp = []
            for val in ans:
                for key in hashmap:
                    if (n == 2 or n == 3) and key == '0':
                        continue
                    temp.append( hashmap[key] + val + key )
            ans = temp
            n -= 2
        
        
        return ans
        