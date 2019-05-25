# -*- coding: utf-8 -*-

'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

'''

# Solution 1: LTE...
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n = len(s1), len(s2)
        i = p = q = 0
        
        for i in range( len(s3) ):
            if p < m and q < n and s1[p] == s2[q] == s3[i]:
                return self.isInterleave( s1[p+1:], s2[q:], s3[i+1:] ) or self.isInterleave( s1[p:], s2[q+1:], s3[i+1:] )
            elif p < m and s1[p] == s3[i]:
                p += 1
            elif q < n and s2[q] == s3[i]:
                q += 1
            else:
                return False
        
        return (p==m) and (q==n)


# Solution 2: DP
# Time * Space: O(m*n)
from collections import Counter
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if Counter(s1) + Counter(s2) != Counter(s3):
            return False
        
        m, n = len(s1), len(s2)
        
        dp = [ [False] * (n+1) for _ in range(m+1)]
        
        dp[0][0] = True
        
        for i in range(1, m+1):
            dp[i][0] = (s1[:i] == s3[:i])
        for j in range(1, n+1):
            dp[0][j] = (s2[:j] == s3[:j])
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                    dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[-1][-1]