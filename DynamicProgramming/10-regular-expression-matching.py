# -*- coding: utf-8 -*-

'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''


'''
这道题我最初是用递归做的，但在python环境里如果不pruning会LTE，说明这道题本质考的不是递归…
【最初的递归解法可以在Previous Folder里找到，这次刷题主要训练DP…】
'''

# Solution 1: DP
# Time & Space: O(m*n)


'''
两种情况
1. p[i-1] != '*': dp[i][j] = dp[i-1][j-1] && isEqual( s[j-1], p[i-1] ) (两个char完全相同或p == '.')
2. p[i-1] == '*': 
	dp[i][j] = 	dp[i-2][j] (前一个char重复0次) +
				dp[i][j-1] && isEqual( s[j-1], p[i-2] )  (前一个char重复1~N次)
'''

class Solution(object):
    def isEqual(self, char1, char2):
        return (char1 == char2 or char2 == '.' )
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return s == ""
        
        m, n = len(s), len(p)
        
        dp = [ [False] * (m + 1) for _ in range( n + 1 ) ]
        
        dp[0][0] = True
        
        for i in range( 1, n + 1 ):
            for j in range( m + 1 ):
                if p [ i - 1 ] != '*' and j >= 1:
                    dp[i][j] = dp[i-1][j-1] and self.isEqual(s[j-1], p[i-1] )
                elif p[ i - 1 ] == '*':
                    dp[i][j] = ( i >= 2 and dp[i-2][j]) or ( j >= 1 and dp[i][j-1] and self.isEqual( s[j-1], p[i-2] ) )

        return dp[-1][-1]
