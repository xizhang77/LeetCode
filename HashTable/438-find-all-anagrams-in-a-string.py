# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''

# Solution 1
from collections import defaultdict
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        window = defaultdict( int )
        check = defaultdict( int )

        for i in range( len(p) - 1 ):
            window[ s[i] ] += 1
            check[ p[i] ] += 1
        check[ p[-1] ] += 1
        
        ans = []
        n = len(p)
        for i in range(n-1, len(s)):
            window[ s[i] ] += 1
            if window == check:
                ans.append( i - n + 1 )
            
            window[ s[i-n+1] ] -= 1
            if window[ s[i-n+1] ] == 0:
                del window[ s[i-n+1] ]
        
        return ans

# Solution 2 [slower version]
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