# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''
from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m, n = len(s), len(p)
        ans = []
        
        if m < n:
            return ans
        if m == n:
            return [ 0 ] if s == p else ans
        
        check_p = Counter(p)
        check_s = Counter(s[:n-1])
        
        i = 0
        while i <= m - n :
            if i > 0:
                check_s[ s[i-1] ] -= 1
                if check_s[ s[i-1] ] == 0:
                    del check_s[ s[i-1] ]
            if s[i+n-1] not in check_s:
                check_s[ s[i+n-1] ] = 1
            else:
                check_s[ s[i+n-1] ] += 1
            if check_s == check_p:
                ans.append( i )
            i += 1
        return ans