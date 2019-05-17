# -*- coding: utf-8 -*-

'''
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

# Solution 1: Brute Force
# Time: O(n^2); Space: O(n)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 0
        res = ''
        for i in range( len(s) ):
            count = 1
            p, q = i - 1, i + 1
            while p >= 0 and q < len(s) and s[p] == s[q]:
                p -= 1
                q += 1
                count += 2
            if count > maxLen:
                res = s[p+1:q]
                maxLen = count
        
        for i in range( len(s) - 1 ):
            if s[i] != s[i+1]:
                continue
            count = 2
            p, q = i - 1, i + 2 
            while p >= 0 and q < len(s) and s[p] == s[q]:
                p -= 1
                q += 1
                count += 2
            if count > maxLen:
                res = s[p+1:q]
                maxLen = count
        
        return res

# Updated based on Solution 1
class Solution(object):
    def helper(self, s, p, q):
        while p >= 0 and q < len(s) and s[p] == s[q]:
            p -= 1
            q += 1
        return s[p+1:q]
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 0
        res = ''
        for i in range( len(s) ):
            # odd case
            temp = self.helper( s, i, i )
            if len(temp) > maxLen:
                res = temp
                maxLen = len(temp)
            # even case
            temp = self.helper( s, i, i + 1 )
            if len(temp) > maxLen:
                res = temp
                maxLen = len(temp)
                
        return res

# Solution 3: DP
# Time & Space: O(n^2)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        
        dp = [ [False] * n for _ in range(n) ]
        
        iAns = 0
        jAns = 0
        
        for i in range(n):
            dp[i][i] = True
            iAns, jAns = i, i
        
        for i in range( n - 1 ):
            dp[i][i+1] = (s[i] == s[i+1])
            if dp[i][i+1]:
                iAns, jAns = i, i + 1
        
        for ln in range( 3, n + 1 ):
            for i in range( n - (ln - 1) ):
                if dp[i+1][i+ln-2] and s[i]==s[i+ln-1]:
                    dp[i][i+ln-1] = True
                    iAns, jAns = i, i + ln-1
        return s[iAns: jAns + 1]