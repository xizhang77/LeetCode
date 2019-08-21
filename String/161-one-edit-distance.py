# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/one-edit-distance/
'''
# Solution 1: 2D DP [LTE]
# Time and Space: O(n^2) 
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return len(t) == 1
        if not t:
            return len(s) == 1
        if s == t:
            return False
            
        m, n = len(s), len(t)
        
        dp = [ [0]*(n+1) for _ in range(m+1) ]
        
        for i in range(1, m+1):
            dp[i][0] = i
        
        for j in range(1, n+1):
            dp[0][j] = j
            
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                temp = 0 if s[i-1] == t[j-1] else 1
                dp[i][j] = min( dp[i-1][j-1] + temp, dp[i-1][j] + 1, dp[i][j-1] + 1 )
        
        return dp[m][n] == 1

# Solution 2
# Time: O(n); Space: O(1)
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return len(t) == 1
        if not t:
            return len(s) == 1
            
        m, n = len(s), len(t)
        
        if s == t or abs(m - n) > 1:
            return False
        
        if m == n: #have to be replace
            for i in range(m):
                if s[i] != t[i]:
                    return s[:i]+s[i+1:] == t[:i]+t[i+1:]
        else:
            if m < n:
                s, t = t, s
                m, n = n, n
            for i in range(m):
                if i < m - 1:
                    if s[i] != t[i]:
                        return  s[:i]+s[i+1:] == t
                else:
                    return s[:i] == t