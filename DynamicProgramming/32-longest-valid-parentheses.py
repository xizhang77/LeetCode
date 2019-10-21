# -*- coding: utf-8 -*-

'''
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

'''
# Soluton 1 [Stack & DP] 
# Time & Space: O(n) [Runtime: 48 ms, faster than 41.24%]
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        
        dp = [ False for _ in range(len(s)) ]
        stack = []
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append( i )
                count += 1
            else:
                if count > 0 :
                    idx = stack.pop()
                    dp[ i ] = dp[ idx ] = True
                    count -= 1
        
        ans = 0
        
        i = 0
        while i < len(s):
            count = 0
            while i < len(s) and dp[i]:
                count += 1
                i += 1
            ans = max( ans, count)
            i += 1
        return ans

# Solution 2: Stack
# Time & Space: O(n) [Runtime: 32 ms, faster than 98.95%]
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = ')' + s
        
        ans = 0
        stack = []
        
        for i in range(len(s)):
            if s[i] == ')' and stack and stack[-1][0] =='(':
                idx = stack.pop()[1]
                ans = max(ans, i - stack[-1][1])
            else:
                stack.append( [s[i], i] )

        return ans

# Solution 3: DP
# Time & Space: O(n)

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        dp = [0]*(len(s)+1)
        
        for i in range( len(s) ):
            if s[i] == ")":
                if i >= 1 and s[i-1] == '(':
                    dp[i+1] = dp[i-1] + 2
                elif i >= dp[i] + 1 and s[ i-dp[i]-1 ] == '(':
                    dp[i+1] = dp[i] + dp[i-dp[i]-1] + 2
                ans = max( ans, dp[i+1] )
                # print dp
        
        return ansa