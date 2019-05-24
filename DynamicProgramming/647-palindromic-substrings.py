# -*- coding: utf-8 -*-

'''
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.

'''

# Solution 1: 2D DP
# Time and Space: O(n^2)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        
        n = len(s)
        
        dp = [ [False] * n for _ in range( n ) ]
        
        count = 0
        for i in range(n):
            dp[i][i] = True
            count += 1
        
        for k in range(1, n):
            for i in range(0, n - k):
                if (k == 1 and s[i] == s[i+k]) or ( k > 1 and s[i] == s[i+k] and dp[i+1][i+k-1] ):
                    dp[i][i+k] = True
                    count += 1
                    
        return count
