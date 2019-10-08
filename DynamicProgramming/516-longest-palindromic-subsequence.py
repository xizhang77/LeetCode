# -*- coding: utf-8 -*-

'''
Given a string s, find the longest palindromic subsequence's length in s. 
You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
'''

# Time & Space: O(n^2)
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        # Running time improved from 2500 to 980 (5% to 85%)
        if s == s[::-1]:
            return len(s)

        n = len(s)
        
        dp = [ [0]*n for _ in range(n) ]
        
        for i in range(n):
            dp[i][i] = 1
        
        for l in range(1, n):
            for i in range( n - l ):
                if s[i] == s[i+l]:
                    dp[i][i+l] = 2 + dp[i+1][i+l-1]
                else:
                    dp[i][i+l] = max(dp[i+1][i+l], dp[i][i+l-1])
        # print dp             
        
        return dp[0][n-1]